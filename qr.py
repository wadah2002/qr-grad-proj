import qrcode
import qrcode.image.svg

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=10,
    border=1,
    image_factory=qrcode.image.svg.SvgPathImage,
)

qr.make(fit=True)
qr.add_data("https://www.ju.edu.sa")

img = qr.make_image(fill_color=(255, 255, 255), back_color=(0, 0, 0))

img.save("test2.svg")
