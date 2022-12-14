ロボットシステム学のROS2練習リポジトリ

[![test](https://github.com/yutadomen/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/yutadomen/mypkg/actions/workflows/test.yml)

# mypkg
``トピックcountupをtalkerノードとlistenerノードでメッセージの受け渡しを行うパッケージ``

### talker.py(publisher)
* 0.5秒周期で0からの数字をカウントしてトピックcountupを通じて送信する   
* 型は16ビット符号つき整数
* 言語:Python

### listener.py(subscriber)
* トピックcountupからメッセージをもらって表示する
* 言語:Python

## 入力方法その1
パブリッシャ用の端末とサブスクライバ用の端末の2つの端末を使用       
端末1   
```
$ ros2 run mypkg talker
```      
端末2   
```
$ ros2 run mypkg listener
```
### 出力例(端末2の表示)
``                         :                          ``   
``[INFO] [1672468243.054642744] [listener]: Listen: 7``   
``[INFO] [1672468243.554157647] [listener]: Listen: 8``   
``[INFO] [1672468244.054175268] [listener]: Listen: 9``   
``                         :                          ``

## 入力方法その2
実行方法その1のように2つのノードが端末を分けずに1つの端末で2つ同時に立ち上げる      
```
$ ros2 launch mypkg talk_listen.launch.py
```
### 出力例  
``                             :                                   ``   
``[listener-2] [INFO] [1672468781.105783726] [listener]: Listen: 7``   
``[listener-2] [INFO] [1672468781.605847465] [listener]: Listen: 8``  
``[listener-2] [INFO] [1672468782.105999722] [listener]: Listen: 9``   
``                             :                                   ``
## 動作確認済み環境及びバージョン
* Ubuntu 20.04
  * ROS2 foxy

## ライセンス
* このソフトウェアパッケージは、3条項BSDライセンスの下，再頒布および使用が許可されます．
* このパッケージのコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
     * [ryuichiueda/my_slides robosys_2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)
* ⓒ 2022 Yuta Domen


