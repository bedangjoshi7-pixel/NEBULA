# NEBULA

### QR Code & Barcode Scanner

NEBULA is a Python-based QR code and barcode scanner that detects, decodes, and extracts information from QR codes and barcodes.

It also integrates **Google Safe Browsing** to check decoded website URLs against known malicious websites, helping users make more informed decisions before visiting potentially unsafe destinations.

## Features

- **Image Scanning** — Detect QR codes and barcodes from still images.
- **Video Scanning** — Detect and scan codes from video footage and webcam streams.
- **URL Extraction** — Extract website URLs encoded in QR codes.
- **URL Verification** — Check extracted URLs using Google Safe Browsing.
- **Malicious URL Detection** — Identify URLs reported as potentially malicious.
- **User Confirmation** — Ask users for confirmation before opening URLs flagged as unsafe.
- **Barcode Decoding** — Decode supported QR code and barcode formats.

## Built With

- Python
- OpenCV
- Pyzbar
- PySafeBrowsing
- Google Safe Browsing API

## Getting Started

### Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/NEBULA.git
```

### Navigate to the project directory

```bash
cd NEBULA
```

### Install dependencies

```bash
pip install opencv-python pyzbar pysafebrowsing
```

### Configure Google Safe Browsing

NEBULA requires a Google Safe Browsing API key for URL verification.

Obtain an API key through Google Cloud Console and configure it as an environment variable named `SAFE_BROWSING_API_KEY`.

Never publish your API key in the repository.

### Run NEBULA

```bash
python main.py
```

## Project Structure

```text
NEBULA/
│
├── main.py
├── README.md
└── LICENSE
```

## Preview

Screenshots and demonstrations of NEBULA will be added here.

## Future Improvements

- Support for additional barcode formats.
- Improved detection accuracy.
- Scan history.
- Enhanced URL security verification.
- Improved user interface.

---

<p align="center">
  NEBULA — Scan Beyond the Ordinary.
</p>