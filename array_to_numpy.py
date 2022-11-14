import numpy as np
from PIL import Image

# Create 3d numpy array of zeros, then replace zeros (black pixels) with yellow pxls
## data = np.zeros((5, 4, 3), dtype=np.uint8)
## data[:] = [255, 255, 0]
data = np.zeros((3, 5, 4), dtype=np.uint8)
data[:] = [255, 255, 255, 0] # the ':' access all the data inside the matrix
print(data)

# Make an array path

##data[0:1, 0:2] = [0, 200, 255]
## data[4:5, 3:5] = [255, 0, 100]
data[0:1, 0:2] = [200, 200, 0, 200]
data[1:2, 1:3] = [100, 100, 0, 200]
data[2:3, 2:4] = [0, 0, 0, 200]
data[3:4, 1:3] = [0, 100, 100, 200]
data[4:5, 0:2] = [0, 255, 255, 200]
## data[4:5, 3:5] = [255, 0, 100] # 4:5 is the row and the 3:5 column

img = Image.fromarray(data, 'RGB')
img.save('canvas.png')

