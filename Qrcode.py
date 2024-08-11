import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data("https://link.springer.com/article/10.1007/s42979-021-00815-1")
qr.make(fit=True)

img = qr.make_image(fill_color="brown", back_color="beige")
img.save("DeepLearningArticle.png")

