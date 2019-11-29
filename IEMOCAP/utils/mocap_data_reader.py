from IEMOCAP.utils.mocap_utils import *
import csv
import pandas as pd


def get_mocap_data(write=False, read_from_csv=False, csv_file_name="IEMOCAP/mocap_dataset.csv"):

    """
    get_directory_structure("IEMOCAP") - Sorts differently on Windows and Ubuntu,
    hence better to save csv after we read all data, and use that one latter
    :param write: write the csv file
    :param csv_file_name: provide correct path
    :param read_from_csv: read from the written file
    :return: lists of utterances, emo_dialogues, emo_evo, v, a, d, utt_keys
    """

    utterances = []
    emo_dialogues = []
    emo_evo = []
    v, a, d = [], [], []
    utt_keys = []
    file_paths = []
    transcriptions = {}
    emotions = {}
    fieldnames = ['utt_keys', 'utterance', 'emotion', 'v', 'a', 'd', 'emo_evo', 'start', 'end']

    if not read_from_csv:
        if write:
            store_mocap_in_csv = open(csv_file_name, mode='w', newline='')
            writer = csv.DictWriter(store_mocap_in_csv, fieldnames=fieldnames)
            writer.writeheader()

        path_tree = get_directory_structure("IEMOCAP")
        sessions = ['S1', 'S2', 'S3', 'S4', 'S5']
        for session in sessions:
            for text in path_tree['IEMOCAP'][session]["transcriptions"]:
                file_path_utt = "IEMOCAP/" + session + "/transcriptions/" + text
                file_path_emo = "IEMOCAP/" + session + "/EmoEvaluation/" + text
                utts = get_transcriptions(file_path_utt)
                emots = get_emotions(file_path_emo)
                transcriptions[session + '_' + text] = utts
                emotions[session + '_' + text] = emots
                for key in list(utts.keys()):
                    try:
                        emo_dialogues.append(emots[key]['emotion'])
                        emo_evo.append(emots[key]['emo_evo'])
                        v.append(emots[key]['v'])
                        a.append(emots[key]['a'])
                        d.append(emots[key]['d'])
                        utterances.append(utts[key])
                        utt_keys.append(key)
                        if write:
                            writer.writerow(
                                {'utt_keys': key, 'utterance': str(utts[key]), 'emotion': emots[key]['emotion'],
                                 'v': emots[key]['v'], 'a': emots[key]['a'], 'd': emots[key]['d'],
                                 'emo_evo': emots[key]['emo_evo'], 'start': emots[key]['start'], 'end': emots[key]['end']})

                    except KeyError:
                        pass
                file_paths.append(file_path_utt)
        utt_id, speaker_id = get_ids_from_keys(utt_keys)
    else:
        df = pd.read_csv(csv_file_name)
        utterances = df['utterance'].tolist()
        emo_dialogues = df['emotion'].tolist()
        v, a, d = df['v'].tolist(), df['a'].tolist(), df['d'].tolist()
        utt_keys = df['utt_keys'].tolist()

        utt_id, speaker_id = get_ids_from_keys(utt_keys)

    return utterances, emo_dialogues, emo_evo, v, a, d, speaker_id, utt_id


def get_ids_from_keys(utt_keys):
    utt_id, speaker_id = [], []
    for item in utt_keys:
        temp_id = item.split('_')[-1]
        xx = list(item)
        xx.reverse()
        yy = xx[4:]
        yy.reverse()
        temp_ses_id = ''.join(yy+[temp_id[0]])
        speaker_id.append(temp_id[1:])
        utt_id.append(temp_ses_id)
    return utt_id, speaker_id

# utterances, emo_dialogues, emo_evo, v, a, d, speaker_id = get_mocap_data(wirte=False)
# print('debug')
