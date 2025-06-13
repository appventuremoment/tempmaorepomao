from hy3dgen.rembg import BackgroundRemover
from PIL import Image

image = Image.open('benormal.png').convert("RGBA")
rembg = BackgroundRemover()

image = rembg(image)
image.save('what.png', format='PNG')