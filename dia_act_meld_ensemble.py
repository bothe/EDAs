import os

from krippendorff import alpha
from scipy.stats import stats
from sklearn.metrics import classification

from MELD.utils.read_meld import *
from dia_act_meld_annotator import *
from utils.ensemble_annotator import convert_predictions_to_indices, ensemble_eda_annotation
from utils.reliability_kappa import fleissKappa

if os.path.exists('assets/tags.npy'):
    tags = np.load('assets/tags.npy')

# Combine training, validation and testing data
utt_Speaker = utt_Speaker_train + utt_Speaker_dev + utt_Speaker_test
utt_data = utt_train_data + utt_dev_data + utt_test_data
utt_id_data = utt_id_train_data + utt_id_dev_data + utt_id_test_data
utt_Emotion_data = utt_Emotion_train_data + utt_Emotion_dev_data + utt_Emotion_test_data
utt_Sentiment_data = utt_Sentiment_train_data + utt_Sentiment_dev_data + utt_Sentiment_test_data

# Evaluation of context model predictions
print('Accuracy comparision between context-based predictions: {}'.format(
    classification.accuracy_score(meld_elmo_con_out, meld_elmo_mean_con_out)))
print('Kappa (Cohen) score between context-based predictions: {}'.format(
    classification.cohen_kappa_score(meld_elmo_con_out, meld_elmo_mean_con_out)))
print(classification.classification_report(meld_elmo_con_out, meld_elmo_mean_con_out))
print('Spearman Correlation between context-based predictions: {}'.format(
    stats.spearmanr(meld_elmo_con_out, meld_elmo_mean_con_out)))
reliability_data = convert_predictions_to_indices(meld_elmo_con_out, meld_elmo_non_con_out, meld_elmo_mean_con_out,
                                                  meld_elmo_mean_non_con_out, meld_elmo_top_con_out, tags)
k_alpha = alpha(reliability_data, level_of_measurement='nominal')
print("Krippendorff's alpha: {}".format(round(k_alpha, 6)))

fleiss_kappa_score = fleissKappa(reliability_data, 5)

# Generate final file of annotations; contains "xx" label for unknown/corrections of EDAs
row = ensemble_eda_annotation(meld_elmo_non_con_out, meld_elmo_mean_non_con_out,
                              meld_elmo_con_out, meld_elmo_mean_con_out, meld_elmo_top_con_out,
                              meld_elmo_non_con_out_confs, meld_elmo_mean_non_con_out_confs,
                              meld_elmo_con_out_confs, meld_elmo_mean_con_out_confs, meld_elmo_top_con_out_confs,
                              utt_Speaker, utt_data, utt_id_data, utt_Emotion_data,
                              sentiment_labels=utt_Sentiment_data, meld_data=True,
                              file_name='meld_emotion', write_final_csv=True)

print('ran dialogue act ensemble for meld, with total {} number of utterances'.format(len(utt_data)))
