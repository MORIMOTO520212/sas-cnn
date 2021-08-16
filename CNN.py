import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import glob
import keras
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Dense, Dropout, Flatten, Activation, Dropout
from sklearn.model_selection import train_test_split


images = [] # 画像データの配列
labels = [] # すべての正解ラベルの配列
class_name = ['healthy','disease'] # すべてのクラス名

# 画像データのパスを読み込む
data_healthy = glob.glob("data/mfcc_spectrogram_images/healthy/*") # 健常者のデータ
data_bad     = glob.glob("data/mfcc_spectrogram_images/disease/*") # 疾患のある人のデータ

# データセットを作る
for i in range(len(data_healthy)): # 健常者のデータ
  X = np.array((Image.open(data_healthy[i])).resize((96,128))) # 画像データをopenしてリサイズしてnumpy配列にする
  images.append(X) # 画像データを追加
  labels.append([1,0]) # 正解ラベルを追加 One-Hotベクトル

for i in range(len(data_bad)): # 疾患のある人のデータ
  X = np.array((Image.open(data_bad[i])).resize((96,128)))
  images.append(X) # 画像データを追加
  labels.append([0,1]) # 正解ラベルを追加 One-Hotベクトル

# numpy配列にする
images = np.array(images)
labels = np.array(labels)

# データの正規化
images = images.astype('float32') / 255.0 # 0~1に丸める

# トレーニングデータとテストデータを分ける
# test_size - テストデータの割合を0~1の範囲で指定する 0.33で33%
# random_state - 乱数シードを指定してデータの振り分けを固定する
# データはシャッフルされる
train_images, test_images, train_labels, test_labels = train_test_split(images, labels, test_size=0.33, random_state=111)

# CNNモデルを構築
#「Conv2D」を使って「畳み込みニューラルネットワーク」CNNを実装
model = Sequential()

# Conv2D(特徴マップ数, カーネルサイズ, ...)
model.add(Conv2D(32, (3, 3), padding='same',
                 input_shape=train_images.shape[1:])) # 畳み込み層 カーネルサイズ3x3, 特徴マップ32枚
model.add(Activation('relu')) # 活性化関数ReLUを使用する
model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(64, (3, 3), padding='same'))
model.add(Activation('relu'))
model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(2)) # クラスは2個
model.add(Activation('softmax'))

# コンパイル
model.compile(loss="categorical_crossentropy",
            optimizer="SGD",
            metrics=[
                "accuracy",
                #keras.metrics.Recall(),
                #keras.metrics.Precision()
            ])

model.summary()

# 学習する 出力はなしで設定(verbose=0)
# epochs - 学習回数
history = model.fit(train_images, train_labels, batch_size=10, epochs=200, validation_data=(test_images, test_labels))

# 学習モデル保存
model.save("CNN.h5")

metrics = ["loss", "accuracy", "recall", "precision"]

# 正解率の算出
plt.plot(history.history["accuracy"])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.xlabel('epoch')
plt.ylabel('accuracy')
plt.legend(['accuracy', 'val_accuracy'], loc='lower right')
plt.grid()
plt.savefig("accuracy.jpg")
plt.show()

# 損失率の算出
plt.plot(history.history["loss"])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.grid()
plt.savefig("loss.jpg")
plt.show()

# 正解率の評価
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
print("Test Accuracy:", test_acc)

# 予測する
predictions = model.predict(test_images)
print(predictions[0]) # 1枚目のテストデータの予測

# 予測の分布
# x軸, 予測結果
# y軸, 予測結果の標準偏差