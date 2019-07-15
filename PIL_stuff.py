from PIL import Image

img = Image.open('/Users/momo/Desktop/face_mic2.png')
img2 = img.resize((512, 512), Image.ANTIALIAS)
print(img2.size)
img2.show()