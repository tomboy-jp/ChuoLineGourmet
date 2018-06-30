# 中央線グルメ傾向調査
中央線沿いにある各駅の飲食店傾向について探ります。

## 手法
```
$ python scrawing.py
```
データについては[食べログ様](https://tabelog.com/)にクローラーを走らせて取得しました。  
純粋にジャンルだけを抜いてきているので、比較的単純なコードとなっております。  
```
$ python summary.py
```
matplotlibとWordCloudを使って可視化するだけです。  
今回は機械学習モデルなどを使用しないシンプルな調査となっております。  
なお食べログ様の仕様で一つの店舗が複数のジャンルを持っています。  
ですので、ジャンル別のすべてのパーセンテージを足しても100にはなりません。

## 総括
全ての駅で居酒屋が1位を占めました。  
カフェとバーが続き、それ以下で各街での特色が出ているようです。

## 中野
![中野ワードクラウド](https://raw.githubusercontent.com/tomboy-jp/ChuoLineGourmet/master/word_cloud/中野.png "中野ワードクラウド")  

![中野グラフ](https://raw.githubusercontent.com/tomboy-jp/ChuoLineGourmet/master/grapf/中野.png "中野グラフ")  
焼鳥とダイニングバーが多めで、パン屋が少ない印象を受けました。  
北口飲み屋街における焼鳥率は一度でも訪れた方なら納得できる結果かと。  
ダイニングバーの比率は意外に思うかも知れませんが、南口マルイ脇のレンガ坂はなかなかのシャレオツ通りで大人な感じのバーがずらりと並んでいます。  
ボンジュールボンの印象の引っ張られたせいか、個人的にパン屋の少なさが新しい気付きでした。  
確かにボンジュールボン以外あまり見かけないですね。  

## 高円寺  
![高円寺ワードクラウド](https://raw.githubusercontent.com/tomboy-jp/ChuoLineGourmet/master/word_cloud/高円寺.png "高円寺ワードクラウド")  

![高円寺グラフ](https://raw.githubusercontent.com/tomboy-jp/ChuoLineGourmet/master/grapf/高円寺.png "高円寺グラフ")  

## 阿佐谷  
![阿佐ヶ谷ワードクラウド](https://raw.githubusercontent.com/tomboy-jp/ChuoLineGourmet/master/word_cloud/阿佐ヶ谷.png "阿佐ヶ谷ワードクラウド")  

![阿佐ヶ谷グラフ](https://raw.githubusercontent.com/tomboy-jp/ChuoLineGourmet/master/grapf/阿佐ヶ谷.png "阿佐ヶ谷グラフ")  

## 荻窪  
![荻窪ワードクラウド](https://raw.githubusercontent.com/tomboy-jp/ChuoLineGourmet/master/word_cloud/荻窪.png "荻窪ワードクラウド")  

![荻窪グラフ](https://raw.githubusercontent.com/tomboy-jp/ChuoLineGourmet/master/grapf/荻窪.png "荻窪グラフ")  

## 西荻窪  
![西荻窪ワードクラウド](https://raw.githubusercontent.com/tomboy-jp/ChuoLineGourmet/master/word_cloud/西荻窪.png "西荻窪ワードクラウド")  

![西荻窪グラフ](https://raw.githubusercontent.com/tomboy-jp/ChuoLineGourmet/master/grapf/西荻窪.png "西荻窪グラフ")  

## 吉祥寺  
![吉祥寺ワードクラウド](https://raw.githubusercontent.com/tomboy-jp/ChuoLineGourmet/master/word_cloud/吉祥寺.png "吉祥寺ワードクラウド")  

![吉祥寺グラフ](https://raw.githubusercontent.com/tomboy-jp/ChuoLineGourmet/master/grapf/吉祥寺.png "吉祥寺グラフ")  

## 三鷹  
![三鷹ワードクラウド](https://raw.githubusercontent.com/tomboy-jp/ChuoLineGourmet/master/word_cloud/三鷹.png "三鷹ワードクラウド")  

![三鷹グラフ](https://raw.githubusercontent.com/tomboy-jp/ChuoLineGourmet/master/grapf/三鷹.png "三鷹グラフ")  
