import qrcode
from qrcode.image.pil import PilImage

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data("https://in.pinterest.com/")
qr.make(fit=True)

img = qr.make_image(fill_color="red", back_color="black", image_factory=PilImage)
img.save("tanayDH_P.png")
