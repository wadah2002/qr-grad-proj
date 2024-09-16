import qrcode
import qrcode.image.svg
from qrcode.image.pilimages import PilImage
from qrcode.image.svg import CircleModuleDrawer


qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=10,
    border=2,
    image_factory=qrcode.image.svg.SvgPathImage,
)

qr.make(fit=True)
qr.add_data("https://www.ju.edu.sa")

img = qr.make_image(image_factory=CircleModuleDrawer(), 
fill_color=(255, 100, 100), back_color=(255, 0, 0))

img.save("test2.svg")
##testing...
