import qrcode
img = qrcode.make("https://www.youtube.com/channel/UC1CAyQK8Qzg6wGahJZaQDLw")
img.save("mu_youtube.jpg")