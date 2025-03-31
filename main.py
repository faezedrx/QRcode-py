import qrcode

# لینک مورد نظر
# url = "https://www.example.com"

# ساخت QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# اضافه کردن لینک به QR Code
qr.add_data(url)
qr.make(fit=True)

# ایجاد تصویر QR Code
img = qr.make_image(fill="black", back_color="white")

# ذخیره تصویر
img.save("qrcode-j.png")
