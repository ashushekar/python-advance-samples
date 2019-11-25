import numpy as np
kernel = np.array([
    [1, 0, -1],
    [0, 0, 0],
    [-1, 0, 1]
])

image = np.array([
    [22, 12, 89, 34, 67],
    [34, 56, 72, 11, 90],
    [52, 64, 78, 90, 86],
    [54, 96, 72, 12, 53],
    [43, 32, 45, 71, 21]

])

image_padded = np.zeros((image.shape[0] + 2, image.shape[1] + 2))
image_padded[1:-1, 1:-1] = image

output = np.zeros_like(image)
for x in range(image.shape[1]):
    for y in range(image.shape[0]):
        output[y, x] = (kernel * image_padded[y:y+3, x:x+3]).sum()


print(output)
