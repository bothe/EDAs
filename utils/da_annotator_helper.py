

def lists_to_text(speaker_ids, utterances, utt_ids, emotions):
    text = "$$$$".join(speaker_ids) + "?????" + "$$$$".join(utterances) + "?????" + "$$$$".join(
        utt_ids) + "?????" + "$$$$".join(emotions)
    return text


def results_from_text_to_lists(results):
    result_items = results.split('?????')
    f_kappa_score_text = result_items[0]
    k_alpha_score_text = result_items[1]
    overall_data_assessment = result_items[2]
    speaker_id, utt_id, utterance, emotion = [], [], [], []
    swda_elmo_non_con_out, swda_elmo_non_con_out_confs = [], []
    swda_elmo_mean_non_con_out, swda_elmo_mean_non_con_out_confs = [], []
    swda_elmo_con_out, swda_elmo_con_out_confs = [], []
    swda_elmo_mean_con_out, swda_elmo_mean_con_out_confs = [], []
    swda_elmo_top_con_out, swda_elmo_top_con_out_confs = [], []
    for item in result_items[3:]:
        elements = item.split('$$$$')
        speaker_id.append(elements[0]), utt_id.append(elements[1]), utterance.append(elements[2]), emotion.append(
            elements[3])
        swda_elmo_non_con_out.append(elements[4]), swda_elmo_non_con_out_confs.append(float(elements[5]))
        swda_elmo_mean_non_con_out.append(elements[6]), swda_elmo_mean_non_con_out_confs.append(float(elements[7]))
        swda_elmo_con_out.append(elements[8]), swda_elmo_con_out_confs.append(float(elements[9]))
        swda_elmo_mean_con_out.append(elements[10]), swda_elmo_mean_con_out_confs.append(float(elements[11]))
        swda_elmo_top_con_out.append(elements[12]), swda_elmo_top_con_out_confs.append(float(elements[13]))
    return f_kappa_score_text, k_alpha_score_text, overall_data_assessment, speaker_id, emotion, \
           swda_elmo_non_con_out, swda_elmo_non_con_out_confs, swda_elmo_mean_non_con_out, \
           swda_elmo_mean_non_con_out_confs, swda_elmo_con_out, swda_elmo_con_out_confs, swda_elmo_mean_con_out, \
           swda_elmo_mean_con_out_confs, swda_elmo_top_con_out, swda_elmo_top_con_out_confs
