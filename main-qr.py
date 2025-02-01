import qrcode
from PIL import Image
app_link = "https://wisewheels.com.pk/"
logo_path = "logo/logo.png"  # Replace with your actual logo path
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Allows for more error correction
    box_size=10,
    border=4,
)
qr.add_data(app_link)
qr.make(fit=True)
qr_img = qr.make_image(fill="black", back_color="white").convert("RGB")
logo = Image.open(logo_path)
logo = logo.convert("RGBA")
logo_size = int(qr_img.size[0] * 0.25)  # 25% of the QR code size
logo = logo.resize((logo_size, logo_size), Image.LANCZOS)
logo_position = (
    (qr_img.size[0] - logo.size[0]) // 2,
    (qr_img.size[1] - logo.size[1]) // 2,
)
qr_img.paste(logo, logo_position, mask=logo.split()[3])  # Use the alpha channel as mask
qr_img.save("./generated-qr/generated.png")
