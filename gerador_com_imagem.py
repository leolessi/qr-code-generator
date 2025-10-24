import qrcode
from qrcode.image.styledpil import StyledPilImage

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
qr.add_data("https://www.github.com/")

imagem = qr.make_image(
    image_factory=StyledPilImage,
    embeded_image_path="logo.png",
)

imagem.save("qrcode_logo.png")
