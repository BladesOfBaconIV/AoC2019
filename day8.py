import numpy as np
import matplotlib.pyplot as plt

with open('input.txt', 'r') as f:
    stream = f.readline()

image = np.array(tuple(map(int, stream))).reshape(-1, 6, 25)

nonzero_counts = np.sum(np.count_nonzero(image, axis=2), axis=1)
fewest_zeros_layer = np.argsort(nonzero_counts)[-1]
unique_values, counts = np.unique(image[fewest_zeros_layer], return_counts=True)
value_counts = dict(zip(unique_values, counts))

output_image = np.zeros((6, 25))
image -= 2
for layer in image:
    output_image = np.where(output_image != 0, output_image, layer)

print(f'{(value_counts[1] * value_counts[2])=}')
plt.imshow(output_image)
plt.show()
