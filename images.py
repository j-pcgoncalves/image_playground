from PIL import Image, ImageFilter

img = Image.open('./pokedex/pikachu.jpg')
filtered_img = img.convert('L')

crooked = filtered_img.rotate(90)
crooked.save('grey.png', 'png')
