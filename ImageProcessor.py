import glob
import os
from PIL import Image
import numpy
PATH = "./img_align_celeba"
image_count = 0
total_images=202600
train=total_images*.8
for filename in glob.glob(os.path.join(PATH, '*.jpg')):
  image =  Image.open(filename)
  newsize = (224,224)
  image = image.resize(newsize)
  numpyImage = numpy.array(image)
  text = 'up/'
  if(image_count%4==1):
   numpyImage = numpy.flipud(numpyImage)
   text = 'down/'
  if(image_count%4==2):
     numpyImage = numpy.rot90(numpyImage)
     text = 'left/'
  if(image_count%4==3):
     numpyImage = numpy.rot90(numpyImage,3)
     text = 'right/'
  split = 'train/'
  if(image_count>train):
    split = 'validate/'
  finshedImage = Image.fromarray(numpyImage)
  finshedImage.save("./processedImages/"+split+text+str(image_count)+".jpg")
  image_count += 1
print(image_count)
