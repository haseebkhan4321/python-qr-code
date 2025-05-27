# 🧾 Python QR Code Generator with Logo Embedding

This project generates QR codes with embedded logos using Python. The input is defined as a Python array of dictionaries, each containing the logo path, the link, and the desired output filename. QR codes are saved in the `generated-qr/` directory.

---

## 📁 Folder Structure

```
python-qr-code/
├── generated-qr/        # Output folder for generated QR PNGs
│   ├── wm-facebook.png
│   ├── wm-instagram.png
│   ├── wm-tiktok.png
│   ├── ww-android.png
│   └── ww-ios.png
│
├── logo/                # Folder for input logo images
│   ├── logo-wm.png
│   └── logo-ww.png
│
├── venv/                # Python virtual environment
│
├── main-qr.py           # Main script to generate QR codes
└── README.md            # This file
```

---

## 🔧 Setup Instructions

### 📦 Requirements

- Python 3.x
- [`qrcode`](https://pypi.org/project/qrcode/)
- [`Pillow`](https://pypi.org/project/Pillow/)

Install dependencies:

```bash
pip install qrcode[pil]
```

---

## ✍️ Configuration

Inside `main-qr.py`, you define the input as a Python array named `apps`:

```python
apps = [
    {
        "logo": "logo/logo-wm.png",
        "link": "https://www.instagram.com/wisemarketpk/",
        "filename": "wm-instagram.png"
    },
    {
        "logo": "logo/logo-wm.png",
        "link": "https://www.facebook.com/wisemarketpakistan",
        "filename": "wm-facebook.png"
    },
    {
        "logo": "logo/logo-wm.png",
        "link": "https://www.tiktok.com/@wisemarket.com.pk",
        "filename": "wm-tiktok.png"
    }
]
```

---

## 🚀 How to Run

```bash
python main-qr.py
```

This will generate the QR codes and save them in the `generated-qr/` folder.

---

## 📸 Output Example

Each QR code will have:
- A white background and black pattern.
- A centered logo from the `logo/` folder.
- A high error correction level to tolerate logo overlay.

---

## 📄 License

MIT License. Free to use and modify.
