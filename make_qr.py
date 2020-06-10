import qrcode

qr = qrcode.QRCode(
    version=2,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=10,
    border=1
)

qr.add_data('https://www.agrex.co.jp')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img.save('test1.png')
