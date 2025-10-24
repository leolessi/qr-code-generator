import qrcode

imagem = qrcode.make("https://www.youtube.com/")
imagem.save("qrcode.png")
