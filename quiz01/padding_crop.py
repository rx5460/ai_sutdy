import numpy as np

image = np.random.rand(4, 4)

# 2 & 3. Padding (Zero-padding)
def padding(image, pad_width):
    new_shape = (image.shape[0] + 2 * pad_width, image.shape[1] + 2 * pad_width)
    padded_image = np.zeros(new_shape)
    padded_image[pad_width:-pad_width, pad_width:-pad_width] = image
    return padded_image

# 4. Crop
def crop(image, start_row, start_col, height, width):
    return image[start_row:start_row+height, start_col:start_col+width]

# 적용 예시
padded_image = padding(image, 1)
cropped_image = crop(image, 1, 1, 2, 2)

print(image)
print(padded_image)
print(cropped_image)
