#Modules Imported
import png
import pyqrcode
import qrcode
from pyqrcode import QRCode

#Link for website
url=input("Please Enter URL : ").strip()

#Creating an instance of qr code 
qr=qrcode.QRCode(version=1,box_size=10,border=5)
qr.add_data(url)
qr.make(fit=1)

#Creating image for the qr code & storing it in img variable
img=qr.make_image(fill="black",back_color='white')
img.show()
