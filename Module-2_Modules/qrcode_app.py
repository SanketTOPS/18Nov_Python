import qrcode

#url="https://www.tops-int.com/"

content="Hi, Hello, this is Python secret msg"

qr=qrcode.make(content)
qr.save('new.png')
