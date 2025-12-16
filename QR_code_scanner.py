# pip install qrcode
# pip install pillow

import qrcode

#Taking Link as input from user
link_id = input("Enter your link: ")

#Generating QR code
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(link_id)
qr.make(fit=True)

#Creating an image from the QR Code instance
img = qr.make_image(fill='black', back_color='white')


#Saving the image
img.save("link_qr.png")