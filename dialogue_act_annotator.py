import json

import requests

from utils.da_annotator_helper import lists_to_text, results_from_text_to_lists
from utils.ensemble_annotator import ensemble_eda_annotation

your_data_name = "your_data_name"

# your lists might look like these ones
example1 = {"speaker_ids": ["A", "B", "A", "B", "A", "B"],
            "utterances": ["I don't know, ", "Where did you go?", "What?", " Where did you go?",
                           "I went to University.", "Uh-huh."],
            "utt_ids": ["1", "2", " 3", "4", "5", "6"],
            "emotions": ["neutral", "surprise", "surprise", "angry", "frustration", "neutral"],
            "is_emotion": True}
# "emotions" is a non-mandatory field (if you have your own other labels; feel free to edit ensemble_eda_annotation())
# or just pass is_emotion=False that would reflect in "ensemble_eda_annotation()" function below

utterances_ex2 = """So it's interesting, though. 
It's a very complex, uh, situation to go into space. 
Oh, yeah. 
You never think about that, do you really? 
Yeah. 
I would think it would be harder to get up than it would be.. 
Yeah."""

example2 = {"speaker_ids": ["A", "B", "A", "B", "A", "B", "A"],
            "utterances": utterances_ex2.split('\n'),
            "utt_ids": ["1", "2", " 3", "4", "5", "6", "7"],
            "emotions": ["" for item in utterances_ex2.split('\n')],
            "is_emotion": False}

# Switch between the examples
example = example2
# your lists might look like these ones
speaker_ids, utterances, utt_ids = example['speaker_ids'], example['utterances'], example['utt_ids']
is_emotion = example["is_emotion"]
emotions = example['emotions']

# encode the lists into one long text to send over the server
text = lists_to_text(speaker_ids, utterances, utt_ids, emotions)

# Send request to the resting server
try:
    link = "http://3025b4706cbd.eu.ngrok.io/"
    results = requests.post(link + 'predict_das', json={"text": text}).json()['result']

    # convert a long string of the resulted text back to lists
    f_kappa_score_text, k_alpha_score_text, _, speaker_id, emotion, \
    non_con_out, non_con_out_confs, mean_non_con_out, mean_non_con_out_confs, con_out, con_out_confs, mean_con_out, \
    mean_con_out_confs, top_con_out, top_con_out_confs = results_from_text_to_lists(results)

    print(k_alpha_score_text)
    print(f_kappa_score_text)

    # Generate final file of annotations; contains "xx" label for unknown/corrections of EDAs
    row = ensemble_eda_annotation(non_con_out, mean_non_con_out, con_out, mean_con_out, top_con_out, non_con_out_confs,
                                  mean_non_con_out_confs, con_out_confs, mean_con_out_confs, top_con_out_confs,
                                  speaker_id,
                                  utterances, speaker_id, emotion, sentiment_labels=[], meld_data=False,
                                  is_emotion=is_emotion,
                                  file_name=your_data_name, write_final_csv=True, write_utterances=True)

except json.decoder.JSONDecodeError:
    print("The given LINK might be broken if the server is down - please try again")
