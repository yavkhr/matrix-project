import numpy as np
from PIL import Image
from matrix_project.matrixproj import change_brights_numpy

image = Image.open("pahan.jpg").convert("L")

matrix = np.array(image)
matrix = change_brights_numpy(-200, matrix)


image  = Image.fromarray(matrix)
image.show()
print(matrix)
print(matrix.shape)
print(image)