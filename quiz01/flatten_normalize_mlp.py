import numpy as np

image = np.random. rand(4, 4)

# 6. Flatten
def flatten(image):
    return image. flatten()

# 7. Normalization
def normalize(image) :
    return (image - np.min(image)) / (np.max(image) - np.min(image))

# 적용 예시
flattened_image = flatten(image)
normalized_image = normalize(image)

print(image)
print(flattened_image)
print(normalized_image)