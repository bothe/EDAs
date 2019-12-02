from collections import Counter

from plot_utils.plot_functions import plot_bars_plot
from utils.read_annotated_data import read_data

utt_speaker, utt, utt_emotion, utt_EDAs, utt_sentiment = read_data('Annotated_EDA_data/eda_meld_emotion_dataset.csv',
                                                                   meld_data=True)
colors_emo = ['Green', 'Blue', 'Black', 'Olive', 'Mediumvioletred', 'Orange', 'Red', 'White']
emotions = ['joy', 'surprise', 'neutral', 'fear', 'sadness', 'disgust', 'anger', 'White']
colors_sent = ['Limegreen', 'Black', 'Red', 'White']
sentiments = ['positive', 'neutral', 'negative', 'White']

tags = sorted(list(Counter(utt_EDAs).keys()))

c = Counter(utt_EDAs)
x = [(i, c[i] / len(utt_EDAs) * 100.0) for i, count in c.most_common()]
print("Number of utterances per dialogue act in percentages")
for item in x:
    print(item[0], round(item[1], 2))

stack_emotions_values = []
stack_sentiments_values = []
for tag in tags:
    if tag is not str:
        pass
    temp_emotion, temp_sentiment = [], []
    for i in range(len(utt)):
        if str(utt_EDAs[i]) == str(tag):
            temp_emotion.append(utt_emotion[i])
            temp_sentiment.append(utt_sentiment[i])
    data_emotion = Counter(temp_emotion)
    data_sentiment = Counter(temp_sentiment)
    values_emotion, values_sentiment = [], []
    for emotion in emotions:
        values_emotion.append(data_emotion[emotion])
    for sentiment in sentiments:
        values_sentiment.append(data_sentiment[sentiment])

    stack_sentiments_values.append(values_sentiment)
    stack_emotions_values.append(values_emotion)

# save stacked bar graph for Emotion MELD
plot_bars_plot(stack_emotions_values, emotions, colors_emo, tags,
               test_show_plot=False, data='meld', type_of='emotion')  # , save_eps=True) # , save_svg=True)

# save stacked bar graph for Sentiment MELD
plot_bars_plot(stack_sentiments_values, sentiments, colors_sent, tags,
               test_show_plot=False, data='meld', type_of='sentiment')  # , save_eps=True) # , save_svg=True)

print('ran read_annotated_meld_data.py')
