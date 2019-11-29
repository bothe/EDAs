import os

from krippendorff import alpha
from scipy.stats import stats
from sklearn.metrics import classification

from dia_act_mocap_annotator import *
from utils.ensemble_annotator import convert_predictions_to_indices, ensemble_eda_annotation
from utils.reliability_kappa import fleissKappa

if os.path.exists('assets/tags.npy'):
    tags = np.load('assets/tags.npy')

utterances, emotion, emo_evo, v, a, d, speaker_id, utt_id = \
    get_mocap_data(read_from_csv=True, write=True, csv_file_name='IEMOCAP/mocap_dataset_without_utterances.csv')

# Evaluation of context model predictions
print('Accuracy comparision between context-based predictions: {}'.format(
    classification.accuracy_score(mocap_elmo_con_out, mocap_elmo_mean_con_out)))
print('Kappa (Cohen) score between context-based predictions: {}'.format(
    classification.cohen_kappa_score(mocap_elmo_con_out, mocap_elmo_mean_con_out)))
print(classification.classification_report(mocap_elmo_con_out, mocap_elmo_mean_con_out))
print('Spearman Correlation between context-based predictions: {}'.format(
    stats.spearmanr(mocap_elmo_con_out, mocap_elmo_mean_con_out)))
reliability_data = convert_predictions_to_indices(mocap_elmo_con_out, mocap_elmo_non_con_out, mocap_elmo_mean_con_out,
                                                  mocap_elmo_mean_non_con_out, mocap_elmo_top_con_out, tags)
k_alpha = alpha(reliability_data, level_of_measurement='nominal')
print("Krippendorff's alpha: {}".format(round(k_alpha, 6)))

fleiss_kappa_score = fleissKappa(reliability_data, 5)

print('Accuracy comparision between context and non-context predictions elmo: {}% elmo_mean: {}% '
      'context-context: {}% non-non-context: {}%'.format(
    classification.accuracy_score(mocap_elmo_con_out, mocap_elmo_non_con_out),
    classification.accuracy_score(mocap_elmo_mean_con_out, mocap_elmo_mean_non_con_out),
    classification.accuracy_score(mocap_elmo_mean_con_out, mocap_elmo_con_out),
    classification.accuracy_score(mocap_elmo_mean_non_con_out, mocap_elmo_non_con_out)))

# Generate final file of annotations; contains "xx" label for unknown/corrections of EDAs
row = ensemble_eda_annotation(mocap_elmo_non_con_out, mocap_elmo_mean_non_con_out,
                              mocap_elmo_con_out, mocap_elmo_mean_con_out, mocap_elmo_top_con_out,
                              mocap_elmo_non_con_out_confs, mocap_elmo_mean_non_con_out_confs,
                              mocap_elmo_con_out_confs, mocap_elmo_mean_con_out_confs, mocap_elmo_top_con_out_confs,
                              utt_id, utterances, speaker_id, emotion,
                              sentiment_labels=[], meld_data=False,
                              file_name='iemocap_no_utts', write_final_csv=True, write_utterances=False)

print('ran dia_act_mocap_ensemble.py, with total {} number of utterances'.format(len(utterances)))
