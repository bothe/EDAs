import numpy as np

from MELD.utils.read_meld import utt_test_data, utt_dev_data, utt_train_data
from config import *

if elmo_feature_retrieval:
    from elmo_features import get_elmo_embs

    meld_elmo_features_test = get_elmo_embs(utt_test_data, mean=False)
    np.save('features/meld_elmo_features_test', meld_elmo_features_test)
    meld_elmo_features_dev = get_elmo_embs(utt_dev_data, mean=False)
    np.save('features/meld_elmo_features_dev', meld_elmo_features_dev)
    meld_elmo_features_train = get_elmo_embs(utt_train_data, mean=False)
    np.save('features/meld_elmo_features_train', meld_elmo_features_train)
elif predict_with_elmo or predict_with_elmo_mean:
    meld_elmo_features_test = np.load('features/meld_elmo_features_test.npy', allow_pickle=True)
    meld_elmo_features_dev = np.load('features/meld_elmo_features_dev.npy', allow_pickle=True)
    meld_elmo_features_train = np.load('features/meld_elmo_features_train.npy', allow_pickle=True)
# Predict with normal elmo features
if predict_with_elmo:
    from main_swda_elmo_predictor import predict_classes_for_elmo

    concatenated_vectors = np.concatenate(
        (meld_elmo_features_train, meld_elmo_features_dev, meld_elmo_features_test))
    meld_elmo_non_con_out, meld_elmo_con_out, meld_elmo_non_con_out_confs, meld_elmo_con_out_confs, \
    meld_elmo_top_con_out, meld_elmo_top_con_out_confs = predict_classes_for_elmo(concatenated_vectors)

    np.save('model_output_labels/meld_elmo_con_out', meld_elmo_con_out)
    np.save('model_output_labels/meld_elmo_non_con_out', meld_elmo_non_con_out)
    np.save('model_output_labels/meld_elmo_con_out_confs', meld_elmo_con_out_confs)
    np.save('model_output_labels/meld_elmo_non_con_out_confs', meld_elmo_non_con_out_confs)
    np.save('model_output_labels/meld_elmo_top_con_out', meld_elmo_top_con_out)
    np.save('model_output_labels/meld_elmo_top_con_out_confs', meld_elmo_top_con_out_confs)
else:
    meld_elmo_con_out = np.load('model_output_labels/meld_elmo_con_out.npy')
    meld_elmo_non_con_out = np.load('model_output_labels/meld_elmo_non_con_out.npy')
    meld_elmo_con_out_confs = np.load('model_output_labels/meld_elmo_con_out_confs.npy')
    meld_elmo_non_con_out_confs = np.load('model_output_labels/meld_elmo_non_con_out_confs.npy')
    meld_elmo_top_con_out = np.load('model_output_labels/meld_elmo_top_con_out.npy')
    meld_elmo_top_con_out_confs = np.load('model_output_labels/meld_elmo_top_con_out_confs.npy')
# Predict with mean elmo features
if predict_with_elmo_mean:
    from main_swda_elmo_mean import predict_classes_for_elmo_mean

    meld_elmo_features_test_mean = np.array([item.mean(axis=0) for item in meld_elmo_features_test])
    meld_elmo_features_dev_mean = np.array([item.mean(axis=0) for item in meld_elmo_features_dev])
    meld_elmo_features_train_mean = np.array([item.mean(axis=0) for item in meld_elmo_features_train])
    concatenated_mean_vectors = np.concatenate((meld_elmo_features_train_mean, meld_elmo_features_dev_mean,
                                                meld_elmo_features_test_mean))
    meld_elmo_mean_non_con_out, meld_elmo_mean_con_out, meld_elmo_mean_non_con_out_confs, \
    meld_elmo_mean_con_out_confs = predict_classes_for_elmo_mean(concatenated_mean_vectors)

    np.save('model_output_labels/meld_elmo_mean_con_out', meld_elmo_mean_con_out)
    np.save('model_output_labels/meld_elmo_mean_non_con_out', meld_elmo_mean_non_con_out)
    np.save('model_output_labels/meld_elmo_mean_con_out_confs', meld_elmo_mean_con_out_confs)
    np.save('model_output_labels/meld_elmo_mean_non_con_out_confs', meld_elmo_mean_non_con_out_confs)
else:
    meld_elmo_mean_con_out = np.load('model_output_labels/meld_elmo_mean_con_out.npy')
    meld_elmo_mean_non_con_out = np.load('model_output_labels/meld_elmo_mean_non_con_out.npy')
    meld_elmo_mean_con_out_confs = np.load('model_output_labels/meld_elmo_mean_con_out_confs.npy')
    meld_elmo_mean_non_con_out_confs = np.load('model_output_labels/meld_elmo_mean_non_con_out_confs.npy')
