from PIL import Image
import os


size = 640, 480
folder = 'train-images/2/'

for filename in os.listdir(folder):
    Image.open(folder + filename).convert('RGB').save(folder + filename)
    im = Image.open(folder + filename)
    im_resized = im.resize(size, Image.ANTIALIAS)
    im_resized.save(folder + filename, "JPEG")