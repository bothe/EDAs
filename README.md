# EDA: Emotional Dialogue Act Data

----------------------------------------------------

## Introduction

Emotional Dialogue Act data contains dialogue act labels 
for existing emotion multi-modal conversational datasets.

Dialogue act provides an intention and performative function in an utterance of the dialogue.
For example, it can infer a user's intention by distinguishing _Question_, _Answer_, _Request_, _Agree/Reject_, etc.
and performative functions such as _Acknowledgement_, _Conversational-opening or -closing_, _Thanking_, etc.


The aim is to enrich the existing multimodal conversational 
emotion dataset that would help advancing conversational analysis 
and help to build natural dialogue systems.

We chose two popular multimodal emotion datasets: 
Multimodal EmotionLines Dataset (MELD) and 
Interactive Emotional dyadic MOtion CAPture database (IEMOCAP).

MELD contains two labels for each utterance in a dialogue: 
Emotions and Sentiments.

- Emotions -- Anger, Disgust, Sadness, Joy, Neutral, Surprise and Fear.

- Sentiments -- positive, negative and neutral.

IEMOCAP contains only emotion but at two levels: 
Discrete and Fine-grained Dimensional Emotions 

- Discrete Emotions: Anger, Frustration, Sadness, Joy, Excited,
Neutral, Surprise and Fear.

- Fine-grained Dimensional Emotions: Valence, Arousal and Dominance.


## Analysis on EDAs

Our analysis on EDAs reveal association between 
dialogue acts and emotional states in natural-conversational language. 
Please see the graph below from IEMOCAP EDAs:

![IEMOCAP Emotion](figures/iemocap_sankey_emotino_for_html.png)

or bar diagrams (as in paper):

![All Combined Bars for IEMOCAP and MELD](figures/bar_diagrams.png)

Visualizing occurrence of utterances with respect to emotion states 
in the particular dialogue acts. 
IE: IEMOCAP, ME: MELD Emotion and MS: MELD Sentiment.

See bigger size graphs in figures: [IEMOCAP Emotion Sankey](figures/iemocap_sankey_emotion.png), 
[MELD Emotion Sankey](figures/meld_sankey_emotion.png), and [MELD Sentiment Sankey](figures/meld_sankey_sentiment.png).

See bar graphs in figures: [IEMOCAP Emotion Bars](figures/iemocap_bars_emotion.png), 
[MELD Emotion Bars](figures/meld_bars_emotion.png), and [MELD Sentiment Bars](figures/meld_bars_sentiment.png).

<details><summary>Click for Names and other statistics of annotated Dialogue Acts</summary>
<p>
<html>
<head>
<title>LaTeX4Web 1.4 OUTPUT</title>
<style type="text/css">
<!--
 body {color: black;  background:"#FFCC99";  }
 div.p { margin-top: 7pt;}
 td div.comp { margin-top: -0.6ex; margin-bottom: -1ex;}
 td div.comb { margin-top: -0.6ex; margin-bottom: -.6ex;}
 td div.norm {line-height:normal;}
 td div.hrcomp { line-height: 0.9; margin-top: -0.8ex; margin-bottom: -1ex;}
 td.sqrt {border-top:2 solid black;
          border-left:2 solid black;
          border-bottom:none;
          border-right:none;}
 table.sqrt {border-top:2 solid black;
             border-left:2 solid black;
             border-bottom:none;
             border-right:none;}
-->
</style>
</head>
<body>
\begintable[!t]
\begincenter
\begintabularllll
DA                    & Dialogue Act                & IEMO   & MELD   <br>

\hline
sd                    & Statement-non-opinion       & 43.97  & 41.63  <br>

sv                    & Statement-opinion           & 19.93  & 09.34  <br>

qy                    & Yes-No-Question             & 10.3   & 12.39  <br>

qw                    & Wh-Question                 &  7.26  & 6.08   <br>

b                     & Acknowledge (Backchannel)   &  2.89  & 2.35   <br>

ad                    & Action-directive            &  1.39  & 2.31   <br>

fc                    & Conventional-closing        &  1.37  & 3.76   <br>

ba                    & Appreciation or Assessment  &  1.21  & 3.72   <br>

aa                    & Agree or Accept             &  0.97  & 0.50   <br>

nn                    & No-Answer                   &  0.78  & 0.80   <br>

ny                    & Yes-Answer                  &  0.75  & 0.88   <br>

br                    & Signal-non-understanding    &  0.47  & 1.13   <br>
 
\textasciicircumq   & Quotation                   &  0.37  & 0.81   <br>

na                    & Affirmative non-yes answers &  0.25  & 0.34   <br>

qh                    & Rhetorical-Question         &  0.23  & 0.12   <br>

bh                    & Rhetorical Backchannel      &  0.16  & 0.30   <br>

h                     & Hedge                       &  0.15  & 0.02   <br>

qo                    & Open-question               &  0.14  & 0.10   <br>

ft                    & Thanking                    &  0.13  & 0.23   <br>

qy\textasciicircumd & Declarative Yes-No-Question &  0.13  & 0.29   <br>

bf                    & Reformulate                 &  0.12  & 0.19   <br>

fp                    & Conventional-opening        &  0.12  & 1.19   <br>

fa                    & Apology                     &  0.07  & 0.04   <br>

fo                    & Other Forward Function      &  0.02  & 0.05   <br>

\hline
Total                 &                             & 10039  & 13708
\endtabular
<font face=symbol>Ç</font>tionNumber of utterances per DA in respective datasets. All values are in percentages (\%) of the total number of utterances. 
IEMO is for IEMOCAP.
<a name="reftable:EDA_stats_all">

\endcenter
\endtable</body>
</html>

</p>
</details>

## Paper
The pre-print of the article (submitted to LREC 2020) explaining these datasets can be found at - 
https://arxiv.org/abs/1912.00819



## Download the final annotated data
Please visit - https://secure-robots.eu/fellows/bothe/eda/ to download the data.


## Description of the .csv files



| Column Name  | Description                                                                                                        |
|--------------|--------------------------------------------------------------------------------------------------------------------|
| speaker      | Name of the speaker (in MELD) or speaker id (in IEMOCAP)                                                           |
| utt_id       | The index of an utterance in the dialogue, starting from 0 (in Meld) or starting 0 from speaker turn (in IEMOCAP)  |
| utterance    | String of utterance.                                                                                               |
| emotion      | The emotion (neutral, joy, excited, sadness, anger, surprise, fear, frustration, disgust) expressed by the speaker in the utterance.  |
| sentiment    | The sentiment (positive, neutral, negative) expressed by the speaker in the utterance (only in MELD).              |
| eda1         | Emotional dialogue act label from Utterance-level 1 model.                                                         |
| eda2         | Emotional dialogue act label from Utterance-level 2 model.                                                         |
| eda3         | Emotional dialogue act label from Context 1 model.                                                                 |
| eda4         | Emotional dialogue act label from Context 2 model.                                                                 |
| eda5         | Emotional dialogue act label from Context 3 model.                                                                 |
| EDA          | Final emotional dialogue act as an ensemble of all models (eda1, eda2, eda3, eda4, eda5)                           |
| all_match    | Flag to indicate if all EDAs are matching (eda1 = eda2 = eda3 = eda4 = eda5).                                      |
| con_match    | Flag to indicate EDAs matched based on context models.                                                             |
| match        | Flag to indicate EDAs matched based on confidence ranking.                                                         |



### The files
- ```annotated_eda_data/eda_iemocap_no_utts_dataset.csv``` - contains the EDAs in IEMOCAP data, without utterances.
- ```annotated_eda_data/eda_meld_emotion_dataset.csv``` - contains the EDAs in meld data, they are staked (train, dev, test).


## Running the scripts

1. Run ```dia_act_meld_ensemble.py``` or ```dia_act_mocap_ensemble.py``` for respective data,
 to generate and calculate the reliability metrics ensemble of the dialogue acts given that all the labels are stored in ```model_output_labels``` directory.

2. Run ```read_annotated_mocap_data.py``` or ```read_annotated_meld_data.py``` to read, generate the the graph and and calculate the data statistics   

Currently, all the predictions are available in the ```model_output_labels``` directory, hence we skip the following.

3. Run ```dia_act_meld_annotator.py``` or ```dia_act_mocap_annotator.py``` to annotate the datasets; 
given that models exists they will be updated soon.


## Referring to the work

Paper explaining the process of dialogue act annotation:

C. Bothe, C. Weber, S. Magg, S. Wermter. 
Enriching Existing Conversational Emotion Datasets with Dialogue Acts using Neural Annotators
(LREC 2020, submitted)

The original work of datasets:

-IEMOCAP:

Busso, C., Bulut, M., Lee, C.-C., Kazemzadeh, A., Mower, E., Kim, S., Chang, J. N., Lee, S., and Narayanan, S. S. 
IEMOCAP: Interactive emotional dyadic motion capture database.
(Language Resources and Evaluation 2008)

-MELD:

S. Poria, D. Hazarika, N. Majumder, G. Naik, E. Cambria, R. Mihalcea. 
MELD: A Multimodal Multi-Party Dataset for Emotion Recognition in Conversation. 
(ACL 2019).

Chen, S.Y., Hsu, C.C., Kuo, C.C. and Ku, L.W. 
EmotionLines: An Emotion Corpus of Multi-Party Conversations. 
(arXiv preprint arXiv:1802.08379 2018).


