# CNNを用いた睡眠時無呼吸症候群の兆候の推定

# インストール
1. libsndfileをインストール
http://www.mega-nerd.com/libsndfile/

2. モジュールをインストール
pip install -r requirements.txt

# インストール注意事項
1. PillowモジュールでPILが読み込めない場合があるので、site-packagesからファイル名を「`pil`」を「`PIL`」に変更する。

# 結果
種類：呼気吸気データ  
健常者データサイズ：58個  
疾患のある人のデータサイズ：57個  
epoch=200, BatchSize=10  
loss: 0.0663 - accuracy: 0.9737  
Test Accuracy: 0.9736841917037964  

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