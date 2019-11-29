import pandas as pd


# speaker,uttID,utterance,emotion,sentiment,non_con_out,con_out,con_out_mean,match,con_match,EDA,Cor_EDA,all_match
def read_data(data, meld_data=False):
    df_train = pd.read_csv(data)  # load the .csv file, specify the appropriate path
    utt = df_train['utterance'].tolist()  # load the list of utterances
    utt_Emotion = df_train['emotion'].tolist()
    utt_EDAs = df_train['EDA'].tolist()
    # utt_Sentiment = df_train['Sentiment'].tolist()
    utt_Speaker = df_train['speaker'].tolist()

    if meld_data:
        utt_Sentiment = df_train['sentiment'].tolist()
        return utt_Speaker, utt, utt_Emotion, utt_EDAs, utt_Sentiment
    else:
        return utt_Speaker, utt, utt_Emotion, utt_EDAs
