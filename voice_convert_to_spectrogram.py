import numpy as np
import glob
import librosa
import librosa.feature
import librosa.display
import matplotlib.pyplot as plt
from time import sleep

# healthy or disease
s = "disease"

##### メルスペクトログラムを可視化 #####
def merspectrogram(mer, file_path):
    plt.figure(figsize=(5,5))
    librosa.display.specshow(mer, sr=sr)
    plt.savefig("data/mer_spectrogram_images/{}/{}".format(s, file_path)) # ex 00001.jpg

##### スペクトログラムのMFCCを可視化 #####
def mfccspectrogram(mfcc, file_path):
    plt.figure()
    plt.title("MFCC")
    librosa.display.specshow(mfcc, sr=sr, x_axis="time", y_axis="hz")
    plt.colorbar()
    plt.savefig("data/mfcc_spectrogram_images/{}/{}".format(s, file_path)) # ex 00001.jpg


# wav audio path
voice_data = glob.glob("data/voice_datasets/{}/*".format(s))

for file_path in voice_data:

    ##### 音声ファイル読み込み #####
    y, sr = librosa.load(file_path, sr=44100)


    ##### 短時間フーリエ変換 #####
    # 振幅スペクトログラムを算出
    D = np.abs(librosa.stft(y)) # STFT
    D_dB = librosa.amplitude_to_db(D, ref=np.max)

    # メルスペクトログラムを算出
    S = librosa.feature.melspectrogram(S=D, sr=sr)
    S_dB = librosa.amplitude_to_db(S, ref=np.max)


    ########## MFCCを算出 ##########
    # n_mfccを大きい値にすると、メル周波数スペクトル包絡のより細かい成分まで考慮することができます。
    # ただし、特徴ベクトルとして次元数が増えてしまうこともあり、分析や機械学習で使う場合は12～24くらいの次元数がよく使われます。
    n_mfcc = 20
    mfcc = librosa.feature.mfcc(S=S_dB, sr=sr, n_mfcc=n_mfcc, dct_type=3)

    file_path = file_path.replace(".wav", ".jpg") # パスをwavからjpgに変換
    file_path = file_path.split("/")[-1] # フォルダ名削除
    file_path = file_path.split("\\")[1] # フォルダ名削除
    merspectrogram(S_dB, file_path)
    sleep(0.5)