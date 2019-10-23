from urllib import request
from PIL import Image

URL = 'https://www.cwb.gov.tw/Data/satellite/FDK_IR1_CR_2750/FDK_IR1_CR_2750-2019-10-23-12-50.jpg'

fileToSave = request.urlopen(URL)
image1 = Image.open(fileToSave)
image1.save("images\\orig.jpg")
half_dim = (image1.size[0] // 2, image1.size[1] // 2)
small1 = image1.resize(half_dim, Image.ANTIALIAS)
small1.save("images\\small.jpg")
r90 = image1.transpose(Image.ROTATE_90)
r90.save("images\\r90.jpg")
r180 = image1.transpose(Image.ROTATE_180)
r180.save("images\\r180.jpg")
r270 = image1.transpose(Image.ROTATE_270)
r270.save("images\\r270.jpg")
r45 = image1.rotate(45)
r45.save("images\\r45.jpg")