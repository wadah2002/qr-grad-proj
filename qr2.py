import qrcode
from qrcode.image.pure import PyPNGImage
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer


def generateQRcode(data, img_path='sample.svg'):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=15,
        border=1,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white",
                        image_factory=StyledPilImage,
                        module_drawer=RoundedModuleDrawer())
    
    img.save(img_path)
    return img_path
