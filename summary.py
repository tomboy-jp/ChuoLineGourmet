import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.ticker import FormatStrFormatter
from wordcloud import WordCloud

font = "/System/Library/Fonts/ヒラギノ明朝 ProN.ttc"
station_name = ["中野", "高円寺", "阿佐ヶ谷", "荻窪", "西荻窪", "吉祥寺", "三鷹"]

def to_grapf(parsentage, title):

    fig = plt.figure(figsize=(20, 10))
    ax = fig.add_subplot(1,1,1)
    ax.bar([x for x in range(20)], parsentage.values[:20], color=cm.Blues(50+20*(c+1)))
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.d%%'))
    plt.title(title)
    plt.xticks([x for x in range(20)], parsentage.index.values[:20], rotation=270)
    fig.subplots_adjust(bottom=0.2)
    plt.savefig("grapf/" + title + ".png")


def to_word_cloud(text, title):

    wordcloud = WordCloud(background_color="white", font_path=font, stopwords=set("その他"), width=600, height=350).generate(text)
    wordcloud.to_file("word_cloud/" + title + ".png")

if __name__ == "__main__":

    try:
        os.mkdir("summary_data")
    except:
        pass

    try:
        os.mkdir("grapf")
    except:
        pass

    try:
        os.mkdir("word_cloud")
    except:
        pass

    for c, i in enumerate(station_name):

        se = pd.read_csv("data/" + i + ".csv")
        li = se.values.tolist()
        counter = []

        for j in li:

            counter += j[0].strip(" ").split("、")

        summary = pd.Series(counter).value_counts(ascending=False)
        summary = summary.drop(index="その他")
        parsentage = summary / len(li) * 100
        parsentage.to_csv("summary_data/" + i + "_sumarry.csv")

        to_grapf(parsentage=parsentage, title=i)
        to_word_cloud(text=" ".join(counter), title=i)
