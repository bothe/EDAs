from collections import Counter

from plot_utils.plot_functions import *
from utils.read_annotated_data import read_data

utt_speaker, utt, utt_emotion, utt_EDAs = read_data('Annotated_EDA_data/eda_iemocap_no_utts_dataset.csv')
colors_emo = ['Green', 'Cyan', 'Blue', 'Black', 'Gray', 'Olive', 'Mediumvioletred', 'Orange', 'Red', 'Brown']
emotions = ['hap', 'exc', 'sur', 'neu', 'xxx', 'fea', 'sad', 'fru', 'ang']
colors_sent = ['Green', 'Black', 'Red']
sentiments = ['positive', 'neutral', 'negative']

tags = sorted(list(Counter(utt_EDAs).keys()))

c = Counter(utt_EDAs)
x = [(i, c[i] / len(utt_EDAs) * 100.0) for i, count in c.most_common()]
print("Number of utterances per dialogue act in percentages")
for item in x:
    print(item[0], round(item[1], 2))

stack_emotions_values = []
for tag in tags:
    if tag is not str:
        pass
    temp_emotion = []
    for i in range(len(utt)):
        if str(utt_EDAs[i]) == str(tag):
            temp_emotion.append(utt_emotion[i])
    data_emotion = Counter(temp_emotion)
    values_emotion = []
    for emotion in emotions:
        values_emotion.append(data_emotion[emotion])

    stack_emotions_values.append(values_emotion)

# save stacked bar graph for Emotion IEMOCAP
plot_bars_plot(stack_emotions_values, emotions, colors_emo, tags,
               test_show_plot=False, data='iemocap', type_of='emotion', plot_sankeys=True)  # , save_eps=True)

print('ran read_annotated_mocap_data.py')
