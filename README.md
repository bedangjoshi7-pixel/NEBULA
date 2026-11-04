# NEBULA

### QR Code & Barcode Scanner

NEBULA is a Python-based QR code and barcode scanner that extracts and displays encoded information from still images and video footage.

It allows users to scan codes from images or videos and identify the website URLs encoded within QR codes. Instead of automatically redirecting users, NEBULA displays the extracted URL, leaving the decision to visit the website entirely up to them.

## Features

- **Image Scanning** — Detect QR codes and barcodes from still images.
- **Video Scanning** — Detect and scan codes from video footage.
- **URL Extraction** — Extract website URLs encoded in QR codes.
- **URL Display** — Display extracted URLs without automatically redirecting users.
- **Barcode Decoding** — Decode supported barcode formats.

## Built With

- Python
- Pyzbar
- OpenCV (if used)

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
pip install opencv-python pyzbar
```

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
- Option to open extracted URLs manually.

---

<p align="center">
  NEBULA — Scan Beyond the Ordinary.
</p>