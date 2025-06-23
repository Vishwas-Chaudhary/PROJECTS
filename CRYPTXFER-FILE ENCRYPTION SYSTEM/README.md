# CRYPTXFER – Secure, Private & Encrypted File Sharing

<p align="center">
  <img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExNzF5emt0eTJ6cXBtd2UzNGpzNTZ5ODF5ZG90aGhzZzJ1YWNtOGE4byZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/077i6AULCXc0FKTj9s/giphy.gif" width="400" height="400" style="margin-right: 70px;" />
  <img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExdjZqOXVuNTR3ZWhrdDFrb2ZmczJvaDZhZmd6NG4yMTU3YnR1b2RxdCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/5wWf7HfQJzA8cze6CWc/giphy.gif" width="400" height="400" />
</p>

**CRYPTXFER** is a lightweight and privacy-first file encryption and sharing tool built for individuals who value **data control**, **security**, and **simplicity**. Whether you're transferring sensitive documents, personal media, or project files — CRYPTXFER ensures they stay **encrypted**, **private**, and **only accessible with your passphrase**.

---

## Features

- **AES encryption**: High-grade symmetric encryption with integrity checks
- **Passphrase protected**: Only the correct phrase can decrypt your files
- **Web-based interface**: Upload, download, and decrypt via browser
- **Universal file support**: Upload and encrypt any file type
- **Self-hosted**: Run locally, no dependency on third-party cloud
- **Stateless design**: Passphrases and keys never leave your machine

---

## How It Works

- Files are encrypted using **AES** before upload.
- Encrypted files are stored in the `encrypted_files/` directory.
- Users must enter the same passphrase to decrypt and access the files.
- The app can directly stream audio from encrypted `.mp3` files.

---

## 🛠Tech Stack

| Layer      | Technology                |
|------------|---------------------------|
| Backend    | Python, Flask,HTTP        |
| Encryption | PyCryptodome (AES)        |
| Frontend   | HTML, CSS, JAVASCRIPT     |

---

## Project Structure

```
CRYPTXFER/
├── app.py                  # Main Flask application
├── encryption.py           # Encryption/decryption functions
├── requirements.txt        # Python dependencies
├── encrypted_files/        # Directory for storing encrypted files
├── static/                 # Static resources (JS, CSS, images)
│   └── music/              # Music files for the media player
└── templates/              # HTML templates
    └── index.html          # Main application interface
```

## Getting Started

```bash
# Clone the repository
git clone https://github.com/Vishwas-Chaudhary/CRYPTXFER.git
cd CRYPTXFER

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py

```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
