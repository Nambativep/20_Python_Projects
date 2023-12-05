import qrcode

features = qrcode.QRCode(version=1, box_size=10, border=3)

(features.
 add_add("https://www.youtube.com/c/NapenaHiTech"))
features.make(fit=True)
generate_image = features.make_image(fill_color="black", back_color="white")
generate_image.save("image2.png")
