import qrcode

url_del_video = "https://gais3r1c.github.io/qr-ringraziamenti/"

# Configurazione del QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(url_del_video)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

nome_file_qr = "qr_ringraziamenti_tesi.png"
img.save(nome_file_qr)
