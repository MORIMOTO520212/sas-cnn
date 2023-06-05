# Discrimination of Sleep Apnea Syndrome(SAS) using Convolutional Neural Network(CNN)

## Summary
I was discriminate SAS of from snoring sound using Machine Learning.  

Machine Learning was used to discriminate suspected SAS from snoring sound.  

The snoring sound was converted to spectrogram  images and training by CNN.  

I discriminated the SAS using the snoring sound data other than training data, it appeared to discriminate with a high probability on the graph, but I actually tried it, it missed it with a probability.  

This is probably due to the small number of training data.  

![accuracy](https://user-images.githubusercontent.com/28892090/136691590-07d3a6de-ccae-41ec-997e-edbb33ee4db1.png)
![recall](https://user-images.githubusercontent.com/28892090/136691597-9e695a19-476a-4abc-8a95-263d24a42c75.png)
![precision](https://user-images.githubusercontent.com/28892090/136691603-b9cecb5e-f2a0-48d1-a487-9df1adee0742.png)

Class label: Health, Disease
Data type: Expiration, Inspiration  
健常者データサイズ：58個  
疾患のある人のデータサイズ：57個  
```
epoch=200, BatchSize=10  
loss: 0.0663 - accuracy: 0.9737  
Test Accuracy: 0.9736841917037964
```

# インストール
1. libsndfileをインストール  
http://www.mega-nerd.com/libsndfile/

2. モジュールをインストール  
pip install -r requirements.txt

# インストール注意事項
1. PillowモジュールでPILが読み込めない場合があるので、site-packagesからファイル名を「`pil`」を「`PIL`」に変更する。

# リファレンス
[1] 音声分類を色々なモデルや特徴量でやってみた  
https://qiita.com/kshina76/items/5686923dee2889beba7c  
[2] numpyでスペクトログラムによる音楽信号の可視化  
https://qiita.com/namaozi/items/dec1575cd455c746f597  
[3] Pythonでのwavファイル操作  
https://qiita.com/Dsuke-K/items/2ad4945a81644db1e9ff  
[4] LibROSA で MFCC（メル周波数ケプストラム係数）を算出して楽器の音色を分析  
https://www.wizard-notes.com/entry/music-analysis/insts-timbre-with-mfcc  
[5] 信号処理とか音楽の分析に大活躍しそうなlibrosa  
https://qiita.com/tom_m_m/items/91ba624dd8507bc0b746  
[6] Pythonの音声処理ライブラリ【LibROSA】で音声読み込み⇒スペクトログラム変換・表示⇒位相推定して音声復元  
スペクトログラムの計算・表示,  スペクトログラムを表示,  
https://qiita.com/lilacs/items/a331a8933ec135f63ab1  
[7] MFCC（メル周波数ケプストラム係数）入門  
LibrosaでMFCCを求める,  
https://qiita.com/tmtakashi_dist/items/eecb705ea48260db0b62  
[8] CNNで蝉の鳴き声を分類する。  
https://qiita.com/kimera0301/items/00936816188c03d84a75  
[9] scikit-learnでデータを訓練用とテスト用に分割するtrain_test_split
https://note.nkmk.me/python-sklearn-train-test-split/  
[10] kerasのConv2D（2次元畳み込み層）について調べてみた  
https://qiita.com/kenichiro-yamato/items/60affeb7ca9f67c87a17  
[11] 機械学習／ディープラーニングにおけるバッチサイズ、イテレーション数、エポック数の決め方  
https://qiita.com/kenta1984/items/bad75a37d552510e4682  
[12] Kerasモデルの保存と読み込み  
https://www.tensorflow.org/guide/keras/save_and_serialize?hl=ja  
[13] [Keras] クラスごとのAccuracy, Precision, Recall, F-measureをmetricsを利用してTensorBoardで確認する  
https://qiita.com/shiita0903/items/838d50598cc28766f84e  
[14] [TensorFlow] Custom Metrics Functionを使っているmodelのリストア方法  
https://qiita.com/tkinjo1/items/51f9e2d0d9c4659bde8a  
