# 予測する
import keras
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

test_image = []

# モデルの読み込み
model = keras.models.load_model("cnn_merspectrogram_01.h5")

# テスト画像の読み込み
image_path = "data/mer_spectrogram_images/disease/voice_data_bad_007.jpg"
#image_path = "tmp.jpg"
X = np.array((Image.open(image_path)).resize((224,224)))
test_image = np.array([X])
pred = model.predict(test_image)
print(pred) # 1枚目のテストデータの予測

