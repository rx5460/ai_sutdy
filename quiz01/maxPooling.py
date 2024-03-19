import numpy as np

# 가상의 이미지 데이터 생성 (4x4 픽셀, 흑백)
image = np.random. rand(4, 4)

# 1. Max Pooling
def max_pooling(image, pool_size):
    output_size = np.array(image. shape) // pool_size
    pooled_image = np. zeros(output_size)
    for i in range(output_size[0]):
        for j in range(output_size[1]):
            pooled_image[i, j] = np.max(image[i*pool_size:(i+1)*pool_size, j*pool_size: (j+1)*pool_size])
    return pooled_image

pooled_image = max_pooling(image, 2)

print(image)
print(pooled_image)