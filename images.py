from PIL import Image, ImageFilter

img = Image.open('./selfie.jpg')
new_img = img.resize((400, 400))
new_img.save('thumbnail.jpg')


