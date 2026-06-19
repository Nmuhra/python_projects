import qrcode

print('Enter the URL to convert:')
url = input()

img = qrcode.make(url)

type(img)

print('Enter the name of your image file:')
img_name = input()

img.save(img_name)