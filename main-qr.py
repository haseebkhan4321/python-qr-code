import qrcode
from PIL import Image
import os

# Make sure the output directory exists
output_dir = "./generated-qr"
os.makedirs(output_dir, exist_ok=True)

# Data array
apps = [
    {
        "logo": "logo-wm.png",
        "link": "https://www.instagram.com/wisemarketpk/",
        "filename": "wm-instagram.png"
    },
    {
        "logo": "logo-wm.png",
        "link": "https://www.facebook.com/wisemarketpakistan",
        "filename": "wm-facebook.png"
    },
    {
        "logo": "logo-wm.png",
        "link": "https://www.tiktok.com/@wisemarket.com.pk",
        "filename": "wm-tiktok.png"
    },
    # Add more entries as needed
]

for app in apps:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(app["link"])
    qr.make(fit=True)
    qr_img = qr.make_image(fill="black", back_color="white").convert("RGB")

    # Add logo
    logo = Image.open("logo/"+app["logo"]).convert("RGBA")
    logo_size = int(qr_img.size[0] * 0.25)
    logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

    logo_position = (
        (qr_img.size[0] - logo.size[0]) // 2,
        (qr_img.size[1] - logo.size[1]) // 2,
    )
    qr_img.paste(logo, logo_position, mask=logo.split()[3])  # Use alpha as mask

    # Save image
    output_path = os.path.join(output_dir, app["filename"])
    qr_img.save(output_path)

print("QR codes generated successfully.")
