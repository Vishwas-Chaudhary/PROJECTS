# CRYPTXFER

A secure file transfer application that allows users to encrypt files with a passphrase before storing them and decrypt them only with the correct passphrase.

## Use Cases

CRYPTXFER can be used in various scenarios where secure file storage and transfer are essential:

- **Personal Cloud Storage**: Securely store sensitive documents before uploading to cloud services
- **Secure File Sharing**: Share encrypted files with colleagues, friends, or family
- **Local Password Manager**: Store sensitive information in encrypted files
- **Secure Backup Solution**: Encrypt important files before backing them up
- **Confidential Business Documents**: Protect trade secrets, financial records, and other sensitive business information
- **Healthcare Information**: Secure patient records or medical files to help maintain HIPAA compliance
- **Academic Research**: Protect research data, especially when collaborating across institutions

## Benefits

- **Enhanced Privacy**: Files remain private even if storage is compromised
- **End-to-End Security**: Data is encrypted on your device before storage
- **No Lock-in**: Your data isn't tied to a specific service provider
- **Self-Hosted**: You maintain complete control over your data
- **Transparent Security**: Open source allows security auditing
- **No Registration Required**: Use immediately without creating accounts
- **Cross-Platform Compatibility**: Works on any device with a web browser
- **Intuitive Interface**: Easy to use for technical and non-technical users alike
- **Content Agnostic**: Encrypt any file type, regardless of content

## Features

- **Secure Encryption**: Files are encrypted using AES-GCM (Advanced Encryption Standard in Galois/Counter Mode)
- **Password Protection**: Files can only be decrypted with the correct passphrase
- **Web Interface**: Easy-to-use browser-based interface
- **Media Support**: Built-in music player for audio files
- **Privacy-Focused**: Files are encrypted before storage, ensuring data remains private

## Technology Stack

- **Backend**: Python with Flask framework
- **Encryption**: AES-GCM via PyCryptodome
- **Frontend**: HTML, CSS, JavaScript

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/cryptxfer.git
   cd cryptxfer
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python app.py
   ```

4. Access the web interface at `http://localhost:5000`

## Usage

### Uploading and Encrypting Files

1. Visit the web interface
2. Click "Choose File" to select the file you want to encrypt
3. Enter a secure passphrase
4. Click "Upload" to encrypt and store the file

### Downloading and Decrypting Files

1. View the list of available encrypted files
2. Click on the file you want to download
3. Enter the same passphrase used during encryption
4. Click "Download" to decrypt and download the file

### Playing Music Files

1. Music files stored in the static/music directory will be available in the media player
2. Use the built-in player controls to listen to your music

## Security

- Files are encrypted using AES-GCM, a highly secure encryption algorithm
- Encryption/decryption is performed using a key derived from your passphrase
- The passphrase is never stored in the system
- Files remain encrypted at rest on the server

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

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This application is designed for personal use. While it uses strong encryption, no security system is 100% foolproof. Always maintain backups of important files and use strong, unique passphrases.

## Future Scope

CRYPTXFER has significant potential for future enhancements:

### Technical Enhancements
- **Mobile Applications**: Native mobile apps for iOS and Android
- **Desktop Applications**: Standalone executables for major operating systems
- **Browser Extensions**: Direct integration with browsers for streamlined workflow
- **End-to-End Encrypted Sharing**: Direct secure sharing between users
- **Multiple Encryption Algorithms**: Support for various encryption methods (RSA, ChaCha20, etc.)
- **Hardware Key Support**: Integration with YubiKey, Ledger, and other hardware security devices
- **Quantum-Resistant Algorithms**: Implementation of post-quantum cryptography

### Feature Enhancements
- **Multi-User Support**: User accounts with varying permission levels
- **File Version History**: Track changes and restore previous versions
- **Scheduled Auto-Deletion**: Set expiration dates for sensitive files
- **Secure Notes**: Built-in encrypted text editor
- **Encrypted Voice Memos**: Support for audio recording and encryption
- **Dead Man's Switch**: Automated file access contingency planning
- **Two-Factor Authentication**: Additional security layer for file access
- **Audit Logging**: Track all access attempts and file operations
- **Directory Encryption**: Support for encrypting entire folders at once

### Integration Possibilities
- **Cloud Service Integration**: Direct encryption before uploading to Dropbox, Google Drive, etc.
- **Email Client Plugins**: Secure attachments directly from email clients
- **Enterprise SSO Integration**: Corporate authentication systems support
- **API Access**: Programmatic access for integration with other applications
