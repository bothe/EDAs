import requests

from utils.da_annotator_helper import lists_to_text, results_from_text_to_lists
from utils.ensemble_annotator import ensemble_eda_annotation

# your lists might look like these ones
speaker_ids = ["A", "B", "A", "B", "A", "B"]
utterances = ["I don't know, ", "Where did you go?", "What?", " Where did you go?", "I went to University.", "Uh-huh."]
utt_ids = ["1", "2", " 3", "4", "5", "6"]
# this is non-mandatory field or list (if you have your own other labels; feel free to edit ensemble_eda_annotation())
# or just pass is_emotion=False
emotions = ["neutral", "surprise", "surprise", "angry", "frustration", "neutral"]

# encode the lists into one long text to send over the server
text = lists_to_text(speaker_ids, utterances, utt_ids, emotions)

# send request to the resting server
link = "http://d55da20d.eu.ngrok.io/"
results = requests.post(link + 'predict_das', json={"text": text}).json()['result']

# convert a long string of the resulted text back to lists
f_kappa_score_text, k_alpha_score_text, _, speaker_id, emotion, \
non_con_out, non_con_out_confs, mean_non_con_out, mean_non_con_out_confs, con_out, con_out_confs, mean_con_out, \
mean_con_out_confs, top_con_out, top_con_out_confs = results_from_text_to_lists(results)

print(k_alpha_score_text)
print(f_kappa_score_text)

# Generate final file of annotations; contains "xx" label for unknown/corrections of EDAs
row = ensemble_eda_annotation(non_con_out, mean_non_con_out, con_out, mean_con_out, top_con_out, non_con_out_confs,
                              mean_non_con_out_confs, con_out_confs, mean_con_out_confs, top_con_out_confs, speaker_id,
                              utterances, speaker_id, emotion, sentiment_labels=[], meld_data=False, is_emotion=True,
                              file_name='your_data_name', write_final_csv=True, write_utterances=True)
