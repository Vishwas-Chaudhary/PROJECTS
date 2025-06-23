// Drag-and-drop upload logic
const dragDropArea = document.getElementById('drag-drop-area');
const fileInput = document.getElementById('upload-file');

if (dragDropArea && fileInput) {
    // Open file dialog on click
    dragDropArea.addEventListener('click', () => fileInput.click());
    dragDropArea.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ') fileInput.click();
    });

    // Drag events
    ['dragenter', 'dragover'].forEach(evt => {
        dragDropArea.addEventListener(evt, (e) => {
            e.preventDefault();
            e.stopPropagation();
            dragDropArea.classList.add('dragover');
        });
    });
    ['dragleave', 'drop'].forEach(evt => {
        dragDropArea.addEventListener(evt, (e) => {
            e.preventDefault();
            e.stopPropagation();
            dragDropArea.classList.remove('dragover');
        });
    });
    dragDropArea.addEventListener('drop', (e) => {
        if (e.dataTransfer.files && e.dataTransfer.files.length > 0) {
            fileInput.files = e.dataTransfer.files;
            showMessage('upload-message', `${e.dataTransfer.files[0].name} ready to upload!`);
        }
    });
    fileInput.addEventListener('change', (e) => {
        if (fileInput.files && fileInput.files.length > 0) {
            showMessage('upload-message', `${fileInput.files[0].name} ready to upload!`);
        }
    });
}

// File operations
async function fetchFiles() {
    const select = document.getElementById('file-list');
    select.disabled = true;
    select.innerHTML = '<option>Loading files...</option>';
    try {
        const res = await fetch('/files');
        if (!res.ok) throw new Error('Failed to fetch file list');
        const files = await res.json();
        select.innerHTML = '';
        if (files.length === 0) {
            select.innerHTML = '<option value="" disabled>No files available</option>';
            document.getElementById('download-btn').disabled = true;
        } else {
            files.forEach(f => {
                let opt = document.createElement('option');
                opt.value = f;
                opt.textContent = f;
                select.appendChild(opt);
            });
            document.getElementById('download-btn').disabled = false;
        }
    } catch (err) {
        select.innerHTML = '<option value="" disabled>Error loading files</option>';
        showMessage('download-message', 'Error loading file list: ' + err.message, true);
    } finally {
        select.disabled = false;
    }
}

// Message display helper
function showMessage(elementId, message, isError = false) {
    const element = document.getElementById(elementId);
    element.textContent = message;
    element.className = 'message' + (isError ? ' error' : '');
    element.style.opacity = 0;
    element.style.transition = 'opacity 0.5s';
    setTimeout(() => {
        element.style.opacity = 1;
    }, 10);
    if (message) {
        setTimeout(() => {
            element.style.opacity = 0;
            setTimeout(() => {
                element.textContent = '';
                element.className = 'message';
                element.style.opacity = 1;
            }, 500);
        }, 5000);
    }
}

// Event Listeners


document.addEventListener('DOMContentLoaded', () => {
    // Fetch files on page load
    fetchFiles();
    


    // Upload form submission
    document.getElementById('upload-form').addEventListener('submit', async (e) => {
        e.preventDefault();
        const fileInput = document.getElementById('upload-file');
        const passphrase = document.getElementById('upload-passphrase').value;
        
        if (!fileInput.files.length) {
            showMessage('upload-message', 'Please select a file', true);
            return;
        }

        const formData = new FormData();
        formData.append('file', fileInput.files[0]);
        formData.append('passphrase', passphrase);

        const uploadBtn = document.getElementById('upload-btn');
        uploadBtn.disabled = true;
        uploadBtn.textContent = 'Uploading...';

        try {
            const response = await fetch('/upload', {
                method: 'POST',
                body: formData
            });
            
            const result = await response.json();
            if (response.ok) {
                showMessage('upload-message', 'File uploaded and encrypted successfully!');
                fileInput.value = '';
                document.getElementById('upload-passphrase').value = '';
                fetchFiles(); // Refresh file list
                // Show modal popup
                const modal = document.getElementById('modal-popup');
                const msg = document.getElementById('modal-message');
                if (modal && msg) {
                    msg.innerHTML = '<span class="royal-symbol">&#9819;</span> File uploaded & encrypted! <span class="royal-symbol">&#9884;</span>';
                    modal.classList.add('active');
                }
            } else {
                throw new Error(result.error || 'Upload failed');
            }
        } catch (error) {
            showMessage('upload-message', 'Error: ' + error.message, true);
        } finally {
            uploadBtn.disabled = false;
            uploadBtn.textContent = 'Upload & Encrypt';
        }
    });


    

    
    // Download button click
    document.getElementById('download-btn').addEventListener('click', async () => {
        const filename = document.getElementById('file-list').value;
        const passphrase = document.getElementById('download-passphrase').value;
        
        if (!filename) {
            showMessage('download-message', 'Please select a file', true);
            return;
        }
        
        if (!passphrase) {
            showMessage('download-message', 'Please enter a passphrase', true);
            return;
        }

        const downloadBtn = document.getElementById('download-btn');
        downloadBtn.disabled = true;
        downloadBtn.textContent = 'Decrypting...';

        try {
            const response = await fetch(`/download/${filename}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ passphrase })
            });

            if (!response.ok) {
                const error = await response.json();
                throw new Error(error.error || 'Download failed');
            }

            const blob = await response.blob();
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = filename;
            document.body.appendChild(a);
            a.click();
            window.URL.revokeObjectURL(url);
            a.remove();
            
            document.getElementById('download-passphrase').value = '';
            showMessage('download-message', 'File decrypted and downloaded successfully!');
        } catch (error) {
            showMessage('download-message', 'Error: ' + error.message, true);
        } finally {
            downloadBtn.disabled = false;
            downloadBtn.textContent = 'Download & Decrypt';
        }
    });
});
