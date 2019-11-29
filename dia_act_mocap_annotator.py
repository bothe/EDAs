import numpy as np

from IEMOCAP.utils.mocap_data_reader import get_mocap_data
from config import *

utterances, emotion, emo_evo, v, a, d, speaker_id, utt_id = \
    get_mocap_data(read_from_csv=True, write=True, csv_file_name='IEMOCAP/mocap_dataset_without_utterances.csv')

if elmo_feature_retrieval:
    from elmo_features import get_elmo_embs

    iemocap_elmo_features = get_elmo_embs(utterances, mean=False)
    np.save('features/iemocap_elmo_features', iemocap_elmo_features)
elif predict_with_elmo or predict_with_elmo_mean:
    iemocap_elmo_features = np.load('features/iemocap_elmo_features.npy', allow_pickle=True)
    # iemocap_elmo_mean_features = np.load('features/iemocap_elmo_mean_features.npy', allow_pickle=True)

# Predict with normal elmo features
if predict_with_elmo:
    from main_swda_elmo_predictor import predict_classes_for_elmo

    mocap_elmo_non_con_out, mocap_elmo_con_out, mocap_elmo_non_con_out_confs, mocap_elmo_con_out_confs, \
    mocap_elmo_top_con_out, mocap_elmo_top_con_out_confs = predict_classes_for_elmo(iemocap_elmo_features)
    np.save('model_output_labels/mocap_elmo_con_out', mocap_elmo_con_out)
    np.save('model_output_labels/mocap_elmo_non_con_out', mocap_elmo_non_con_out)
    np.save('model_output_labels/mocap_elmo_con_out_confs', mocap_elmo_con_out_confs)
    np.save('model_output_labels/mocap_elmo_non_con_out_confs', mocap_elmo_non_con_out_confs)
    np.save('model_output_labels/mocap_elmo_top_con_out', mocap_elmo_top_con_out)
    np.save('model_output_labels/mocap_elmo_top_con_out_confs', mocap_elmo_top_con_out_confs)
else:
    mocap_elmo_con_out = np.load('model_output_labels/mocap_elmo_con_out.npy')
    mocap_elmo_non_con_out = np.load('model_output_labels/mocap_elmo_non_con_out.npy')
    mocap_elmo_con_out_confs = np.load('model_output_labels/mocap_elmo_con_out_confs.npy')
    mocap_elmo_non_con_out_confs = np.load('model_output_labels/mocap_elmo_non_con_out_confs.npy')
    mocap_elmo_top_con_out = np.load('model_output_labels/mocap_elmo_top_con_out.npy')
    mocap_elmo_top_con_out_confs = np.load('model_output_labels/mocap_elmo_top_con_out_confs.npy')

# Predict with normal elmo mean features
if predict_with_elmo_mean:
    from main_swda_elmo_mean import predict_classes_for_elmo_mean

    iemocap_elmo_features_mean = np.array([item.mean(axis=0) for item in iemocap_elmo_features])
    mocap_elmo_mean_non_con_out, mocap_elmo_mean_con_out, mocap_elmo_mean_non_con_out_confs, \
    mocap_elmo_mean_con_out_confs = predict_classes_for_elmo_mean(iemocap_elmo_features_mean)

    np.save('model_output_labels/mocap_elmo_mean_con_out', mocap_elmo_mean_con_out)
    np.save('model_output_labels/mocap_elmo_mean_non_con_out', mocap_elmo_mean_non_con_out)
    np.save('model_output_labels/mocap_elmo_mean_con_out_confs', mocap_elmo_mean_con_out_confs)
    np.save('model_output_labels/mocap_elmo_mean_non_con_out_confs', mocap_elmo_mean_non_con_out_confs)
else:
    mocap_elmo_mean_con_out = np.load('model_output_labels/mocap_elmo_mean_con_out.npy')
    mocap_elmo_mean_non_con_out = np.load('model_output_labels/mocap_elmo_mean_non_con_out.npy')
    mocap_elmo_mean_con_out_confs = np.load('model_output_labels/mocap_elmo_mean_con_out_confs.npy')
    mocap_elmo_mean_non_con_out_confs = np.load('model_output_labels/mocap_elmo_mean_non_con_out_confs.npy')
