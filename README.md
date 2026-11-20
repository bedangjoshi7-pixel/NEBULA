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

## Documentation & Resources

Here are the official documentation and resources for the technologies used in NEBULA.

- [Python Documentation](https://docs.python.org/3/)
- [OpenCV-Python Tutorials](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)
- [Pyzbar - PyPI](https://pypi.org/project/pyzbar/)
- [Pyzbar - GitHub](https://github.com/NaturalHistoryMuseum/pyzbar)
- [PySafeBrowsing - PyPI](https://pypi.org/project/pysafebrowsing/)
- [PySafeBrowsing - GitHub](https://github.com/Te-k/pysafebrowsing)
- [Google Safe Browsing API](https://developers.google.com/safe-browsing)
- [Python Webbrowser Module](https://docs.python.org/3/library/webbrowser.html)

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

Obtain an API key through Google Cloud Console.

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

NEBULA is an ongoing project, and I plan to expand its functionality over time.

Some planned improvements include:

- **Scan History** — Keep a record of previously scanned QR codes and barcodes.
- **Additional Barcode Formats** — Support more barcode formats.
- **Improved Detection** — Improve scanning performance and detection accuracy.
- **Enhanced URL Security** — Expand URL verification and security checks.
- **User Interface** — Improve the overall user experience and interface.

More features and improvements will be introduced as development continues.

---

<p align="center">
  NEBULA — Scan Beyond the Ordinary.
</p>