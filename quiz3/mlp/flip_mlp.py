import numpy as np

image = np.random.rand(4, 4)

def flip_image(image, axis):
    # Assuming image is a 2D numpy array
    if axis == 'horizontal':
        # Flip horizontally
        return image[:, ::-1]
    elif axis == 'vertical':
        # Flip vertically
        return image[::-1, :]
    else:
        raise ValueError("Axis must be 'horizontal' or 'vertical'")


flipped_image = flip_image(image, 'horizontal')
print(image)
print(flipped_image)