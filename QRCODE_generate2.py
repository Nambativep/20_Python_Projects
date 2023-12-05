import qrcode


# Function to convert text to QR code and save it as an image
def convert_text_to_qrcode(text, filename):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    img.save(filename)


# Function to convert a QR code image to text
def convert_qrcode_to_text(image):
    qr = qrcode.QRCode()
    qr_img = qr.make(image)
    qr_img = qr_img.convert("RGB")
    qr_results = qr.decode(qr_img)
    return qr_results[0][0] if qr_results else None


# Example usage
text_to_convert = "Hello, World!"
filename = "qrcode.png"

# Convert text to QR code and save as an image
convert_text_to_qrcode(text_to_convert, Nambative_QRCODE)
print("QR code generated and saved as", Nambative_QRCODE)

# Convert QR code image back to text
result = convert_qrcode_to_text(Nambative_QRCODE)
print("Text decoded from the QR code:", result)
