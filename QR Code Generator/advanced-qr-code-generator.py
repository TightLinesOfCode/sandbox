# import modules
import qrcode
from PIL import Image

# taking image which user wants 
# in the QR code center
Logo_link = 'logo.png'

logo = Image.open(Logo_link)

# taking base width
basewidth = 300

# adjust image size
wpercent = (basewidth/float(logo.size[0]))
hsize = int((float(logo.size[1])*float(wpercent)))


# Old code (deprecated)
# logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)

# New code (using LANCZOS resampling)


# logo = logo.resize((basewidth, hsize), Image.Resampling.LANCZOS)

# Other options
# image.thumbnail(size, Image.Resampling.BILINEAR)
# image.thumbnail(size, Image.Resampling.BICUBIC)

logo = logo.resize((basewidth, hsize), Image.Resampling.NEAREST)


new_width, new_height = logo.size

QRcode = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=20
)

# taking url or text
url = 'https://www.atapir.com/'

# adding URL or text to QRcode
QRcode.add_data(url)

# generating QR code
QRcode.make()

# taking color name from e
QRcolor = 'Black'

# adding color to QR code
QRimg = QRcode.make_image(
    fill_color=QRcolor, back_color="white").convert('RGBA')

# set size of QR code
pos = ((QRimg.size[0] - new_width) // 2,
       (QRimg.size[1] - new_height) // 2)
QRimg.paste(logo, pos)

# save the QR code generated
QRimg.save('qr-code-with-logo.png')

print('QR code generated!')