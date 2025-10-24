# Links:
# - https://www.youtube.com/
# - https://github.com/
# - https://www.instagram.com/
# - https://www.chess.com/
# - https://portalhashtag.com/


import qrcode

imagem = qrcode.make("https://www.youtube.com/")
imagem.save("qrcode.png")
