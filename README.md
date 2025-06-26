# QR Code Scanner & Generator

A modern web application for scanning QR codes and generating QR codes from CSV data.

## Features

- **QR Code Scanner**: Scan QR codes using your device's camera
- **Voice Output**: Hear the scanned data read aloud in a natural voice
- **CSV Upload**: Upload CSV files with student data (Name, Major)
- **QR Code Generation**: Generate QR codes for all students in the CSV
- **Bulk Download**: Download all generated QR codes as a ZIP file
- **Modern UI**: Beautiful, responsive design that works on all devices

## How to Use

### Scanning QR Codes
1. Open the web app in your browser
2. Click "Scan QR Code" button
3. Allow camera access when prompted
4. Point your camera at a QR code
5. The student's name and major will be displayed and read aloud

### Generating QR Codes from CSV
1. Prepare a CSV file with columns: `Name`, `Major`
2. Click "Choose CSV File" and upload your file
3. Click "Generate QR Codes" button
4. Download the ZIP file containing all QR codes

## File Structure

```
├── qr_scanner.html          # Main web application
├── students.csv             # Sample CSV file with student data
├── generate_qr_codes.py     # Python script for generating QR codes
├── qr_code_for_scanner.py   # Python script for generating scanner QR code
└── qr_codes/                # Generated QR code images
```

## Technologies Used

- HTML5, CSS3, JavaScript
- HTML5 QR Code Scanner library
- PapaParse (CSV parsing)
- JSZip (ZIP file generation)
- QRCode.js (QR code generation)
- Web Speech API (Text-to-speech)

## Setup

1. Clone this repository
2. Open `qr_scanner.html` in a web browser
3. For local development, run a simple HTTP server:
   ```bash
   python -m http.server 8000
   ```
4. Access the app at `http://localhost:8000/qr_scanner.html`

## Browser Compatibility

- Chrome (recommended)
- Firefox
- Safari
- Edge

## License

This project is open source and available under the MIT License. 