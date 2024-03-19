import numpy as np
import tensorflow as tf

# 가상의 이미지 데이터 생성 (4x4 픽셀, 흑백)
image = np.random.rand(1, 4, 4, 1)  # TensorFlow와 호환되도록 배치 차원 및 채널 차원을 추가합니다.

# 1. TensorFlow를 사용한 최대 풀링
def max_pooling(image, pool_size):
    input_layer = tf.keras.layers.Input(shape=image.shape[1:])  # 입력 레이어 정의
    max_pool_layer = tf.keras.layers.MaxPooling2D(pool_size=pool_size)(input_layer)  # MaxPooling2D 레이어 추가
    model = tf.keras.Model(inputs=input_layer, outputs=max_pool_layer)  # 모델 생성
    pooled_image = model.predict(image)  # 최대 풀링 수행
    return pooled_image

pooled_image = max_pooling(image, (2, 2))

print("원본 이미지:")
print(image.squeeze())  # 출력을 위해 배치 및 채널 차원을 제거합니다.
print("\n풀링된 이미지:")
print(pooled_image.squeeze())  # 출력을 위해 배치 및 채널 차원을 제거합니다.
