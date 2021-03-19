# -*- coding: utf-8 -*-

# Python QR Code Generator
# Author - yucheng.hu@insight.com

import qrcode.image.svg

image_path = "resources/token_qr.png"

qr_string = "yucheng.hu@insight.com"
print(qr_string)

img = qrcode.make(qr_string)
img.save(image_path)
