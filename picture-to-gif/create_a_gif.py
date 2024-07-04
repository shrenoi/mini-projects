import imageio.v3 
filenames = ['image1.jpg', 'image2.jpg','image1.jpg', 'image2.jpg','image1.jpg', 'image3.jpg','image4.jpg','image5.jpg']
images=[ ]

for i in filenames:
  images.append(imageio.v3.imread(i))

imageio.v3.imwrite('buttercup.gif', images, duration=0.3, loop=0)