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
「焼鳥」と「立ち飲み居酒屋」、「ダイニングバー」が多めで、パン屋が少ない印象を受けました。  
北口飲み屋街における焼鳥率や立ち飲み率は一度でも訪れた方なら納得できる結果かと。  
ダイニングバーの比率は意外に思うかも知れませんが、南口マルイ脇のレンガ坂はなかなかのシャレオツ通りで大人な感じのバーがずらりと並んでいます。  
ボンジュールボンの印象の引っ張られたせいか、個人的にパン屋の少なさが新しい気付きでした。  
確かにボンジュールボン以外あまり見かけないですね。  

## 高円寺  
![高円寺ワードクラウド](https://raw.githubusercontent.com/tomboy-jp/ChuoLineGourmet/master/word_cloud/高円寺.png "高円寺ワードクラウド")  

![高円寺グラフ](https://raw.githubusercontent.com/tomboy-jp/ChuoLineGourmet/master/grapf/高円寺.png "高円寺グラフ")  
概ね中野と似たような傾向になりましたが、「カフェ」や「喫茶店」、「コーヒー専門店」など休憩どころに強い印象です(カフェとコーヒー専門線の基準とは？)。  
住人通しが溜まり場で駄弁っている高円寺の印象そのものですね。  
中野同様に「そば」がランクインしているのも印象的です。


## 阿佐谷  
![阿佐ヶ谷ワードクラウド](https://raw.githubusercontent.com/tomboy-jp/ChuoLineGourmet/master/word_cloud/阿佐ヶ谷.png "阿佐ヶ谷ワードクラウド")  

![阿佐ヶ谷グラフ](https://raw.githubusercontent.com/tomboy-jp/ChuoLineGourmet/master/grapf/阿佐ヶ谷.png "阿佐ヶ谷グラフ")  
まず目に付くのは「中華料理」の多さです。  
体感としてはそういったイメージはなかったので、今度訪れたら意識して観察しようと思います。  
次いで注目したいのは「デリカテッセン」「弁当」の多さ。  
こちらはさもありなんといった感じの結果でして、確かにこの街はパール街を中心にテイクアウトのお店が大変充実しています。  
そうした食べ歩きが楽しめるのが阿佐ヶ谷の魅力かと。  

## 荻窪  
![荻窪ワードクラウド](https://raw.githubusercontent.com/tomboy-jp/ChuoLineGourmet/master/word_cloud/荻窪.png "荻窪ワードクラウド")  
![荻窪グラフ](https://raw.githubusercontent.com/tomboy-jp/ChuoLineGourmet/master/grapf/荻窪.png "荻窪グラフ")  
特筆すべきはラーメンのスコアでしょう。  
都内でも筆頭の激戦区として知られ、春木屋をはじめとして十八番や丸福、久保田、二郎などの有名店が立ち並ぶ荻窪。  
いかにも納得の結果です。  
逆にバーやダイニングバーなどの順位は低めで、和食と中華が充実している模様です。  

## 西荻窪  
![西荻窪ワードクラウド](https://raw.githubusercontent.com/tomboy-jp/ChuoLineGourmet/master/word_cloud/西荻窪.png "西荻窪ワードクラウド")  

![西荻窪グラフ](https://raw.githubusercontent.com/tomboy-jp/ChuoLineGourmet/master/grapf/西荻窪.png "西荻窪グラフ")  
和食多めの荻窪とカフェやスイーツが多めの吉祥寺。  
その二駅を足して二で割ったような印象です。  
数少ないケーキがランクインしているかと思いきや、  
荻窪と同様に魚介・海鮮系が上位にランクインしていたりとなかなかカオスな模様。  
悪く言えば全体的に一貫制がないのですが、よくいえば選択肢の幅が多いのが特徴です。  

## 吉祥寺  
![吉祥寺ワードクラウド](https://raw.githubusercontent.com/tomboy-jp/ChuoLineGourmet/master/word_cloud/吉祥寺.png "吉祥寺ワードクラウド")  

![吉祥寺グラフ](https://raw.githubusercontent.com/tomboy-jp/ChuoLineGourmet/master/grapf/吉祥寺.png "吉祥寺グラフ")  
吉祥寺は想像していた以上に吉祥寺でした。  
カフェ、バー、ダイニングバー、イタリアン、スイーツなど、  
女子力高めのカテゴリが上位を占めながらも焼き鳥屋・ラーメンといった  
おっさん力高めなコンテンツもしっかり揃っているのが吉祥寺。  
公園や東急の裏エリアといったオシャレエリアもあれば、  
ハーモニカ横丁のようなちょっと昭和なエリアもある。  
そんな魅力が多くの人を惹き付けるのでしょう。

## 三鷹  
![三鷹ワードクラウド](https://raw.githubusercontent.com/tomboy-jp/ChuoLineGourmet/master/word_cloud/三鷹.png "三鷹ワードクラウド")  

![三鷹グラフ](https://raw.githubusercontent.com/tomboy-jp/ChuoLineGourmet/master/grapf/三鷹.png "三鷹グラフ")  
全体的に和食度高めの三鷹。  
ラーメンもそこそこ強かったりと荻窪との類似性が高めです。  
実は個人経営の和食系飲み屋が多い三鷹なのですが、結果にもしっかり反映されているようです。  
他、西荻窪と同様にケーキがランクインしているのですが、これは吉祥寺文化の影響でしょう。  

以上、レポでした。
