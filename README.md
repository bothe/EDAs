# EDA: Emotional Dialogue Act Data

----------------------------------------------------

## Introduction

Emotional Dialogue Act data contains dialogue act labels 
for existing emotion datasets.

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


## Paper
The paper explaining these dataset can be found - https://arxiv.org/pdf/xxxx.xxxxx.pdf
(will be available soon)

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
LREC (2020) (submitted)

The original work of datasets:

-IEMOCAP:

Busso, C., Bulut, M., Lee, C.-C., Kazemzadeh, A., Mower, E., Kim, S., Chang, J. N., Lee, S., and Narayanan, S. S. 
IEMOCAP: Interactive emotional dyadic motion capture database.
Language Resources and Evaluation (2008)

-MELD:

S. Poria, D. Hazarika, N. Majumder, G. Naik, E. Cambria, R. Mihalcea. 
MELD: A Multimodal Multi-Party Dataset for Emotion Recognition in Conversation. 
ACL (2019).

Chen, S.Y., Hsu, C.C., Kuo, C.C. and Ku, L.W. 
EmotionLines: An Emotion Corpus of Multi-Party Conversations. 
arXiv preprint arXiv:1802.08379 (2018).


