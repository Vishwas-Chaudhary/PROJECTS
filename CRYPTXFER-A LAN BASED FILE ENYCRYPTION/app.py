from flask import Flask, request, send_file, jsonify, render_template, abort
import os
from io import BytesIO
from werkzeug.utils import secure_filename
from encryption import encrypt, decrypt

app = Flask(__name__)

UPLOAD_FOLDER = 'encrypted_files'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        
        try:
            # Read file content and encrypt it
            file_content = file.read()
            encrypted_content = encrypt(file_content, request.form['passphrase'])
            
            # Save encrypted file
            with open(filepath, 'wb') as f:
                f.write(encrypted_content)
                
            return jsonify({'message': 'File uploaded and encrypted successfully'})
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    return jsonify({'error': 'File upload failed'}), 400

@app.route('/files')
def files():
    try:
        files = [f for f in os.listdir(UPLOAD_FOLDER) if os.path.isfile(os.path.join(UPLOAD_FOLDER, f))]
        return jsonify(files)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/music-files')
def music_files():
    music_folder = os.path.join(app.static_folder, 'music')
    if not os.path.exists(music_folder):
        return jsonify([])
    music_exts = ('.mp3', '.ogg', '.wav')
    music_files = [f'/static/music/{f}' for f in os.listdir(music_folder) if f.lower().endswith(music_exts) and os.path.isfile(os.path.join(music_folder, f))]
    return jsonify(music_files)

@app.route('/download/<filename>', methods=['POST'])
def download(filename):
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    
    if not os.path.exists(filepath):
        return jsonify({'error': 'File not found'}), 404
    
    try:
        data = request.get_json()
        if not data or 'passphrase' not in data:
            return jsonify({'error': 'Passphrase is required'}), 400
            
        # Read and decrypt the file
        with open(filepath, 'rb') as f:
            encrypted_content = f.read()
            
        try:
            decrypted_content = decrypt(encrypted_content, data['passphrase'])
        except Exception as e:
            return jsonify({'error': 'Decryption failed. Invalid passphrase or corrupted file.'}), 400
        
        # Create a file-like object in memory
        file_obj = BytesIO(decrypted_content)
        file_obj.seek(0)
        
        return send_file(
            file_obj,
            as_attachment=True,
            download_name=filename,
            mimetype='application/octet-stream'
        )
    except Exception as e:
        return jsonify({'error': str(e)}), 500



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
