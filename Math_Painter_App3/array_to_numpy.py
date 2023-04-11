import numpy as np
from PIL import Image


# Create 3d numpy array of zeros, then replace zeros (black pixels) with yellow pixels
data = np.zeros((5, 4, 3), dtype=np.uint8)
data[:] = [255, 255, 0]
print(data)

data[0:3, 0:2] = [255, 200, 233]
data[3:4, 1:4] = [45, 3, 233]


img = Image.fromarray(data, "RGB")
img.save("files/canvas.png")


