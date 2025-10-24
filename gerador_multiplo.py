import qrcode
from qrcode.image.styledpil import StyledPilImage

gerar_links = {
    "Youtube": "https://www.youtube.com/",
    "Github": "https://github.com/",
    "Instagram": "https://www.instagram.com/",
    "Chess": "https://www.chess.com/",
    "Hashtag Treinamentos": "https://portalhashtag.com/",
}

for rede_social, link in gerar_links.items():
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(link)

    imagem = qr.make_image(
        image_factory=StyledPilImage,
        embeded_image_path="logo.png",
    )

    imagem.save(f"qrcode_{rede_social}.png")
