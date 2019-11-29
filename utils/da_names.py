EDAs = {
    # 'Statement': ['sd', 'sv'],
    'sd': 'Statement-non-opinion', 'sv': 'Statement-opinion',
    # 'Questions': ['qw', 'qy^d', 'qy', 'qh', 'qo', 'qrr', '^q', 'qw^d', '^g'],
    'qw': 'Wh-Question', 'qw^d': 'Declarative Wh-Question',
    'qy': 'Yes-No-Question', 'qy^d': 'Declarative Yes-No-Question',
    'qh': 'Rhetorical-Question', 'qo': 'Open-question', 'qrr': 'Or-Clause-Question',
    '^q': 'Quotation', '^g': 'Tag-Question',
    # 'Answers': ['nn', 'na', 'ny', 'no', 'ng'],
    'nn': 'No-Answer', 'ng': 'Negative non-no answers',
    'ny': 'Yes-Answer', 'na': 'Affirmative non-yes answers',
    'no': 'Other Answer', 'nd': 'Dispreferred answer',
    # 'Agreement': ['aa', 'ar', 'ad', '^h', 'aap_am', 'arp_nd'],
    'aa': 'Agree or Accept', 'ar': 'Reject', 'aap': 'Accept-part', 'am': 'Maybe',
    'ad': 'Action-directive', '^h': 'Hold before answer or agreement',
    # 'BackwardFunction': ['b', 'bk', 'bh', 'ba', 'bf', 'br', 'bd', '^2'],
    'b': 'Acknowledge (Backchannel)', 'bk': 'Response Acknowledgement',
    'bh': 'Rhetorical Backchannel', 'ba': 'Appreciation or Assessment',
    'bf': 'Reformulate', 'br': 'Signal-non-understanding',
    'bd': 'Downplaying-response', '^2': 'Collaborative Completion',
    # 'ForwardFunction': ['fo_o_fw_"_by_bc', 'fc', 'ft', 'fp', 'fa', 'oo_co_cc', 'fo_o', 'fw'],
    'fo': 'Other Forward Function', 'fc': 'Conventional-closing', 'fp': 'Conventional-opening',
    'ft': 'Thanking', 'fa': 'Apology', 'oo_co_cc': 'Offers, Options, Commits',
    # 'CommInfoStatus': ['%', 'b^m', 't1', 't3'],
    '%': 'Uninterpretable', 'b^m': 'Repeat-phrase',
    't1': 'Self-talk', 't3': '3rd-party-talk',
    # 'Other': ['h', '^q'],
    'h': 'Hedge',
    # 'NonSpeechVerbal': ['x']
    'x': 'Non-verbal',
}


DAs = {
    'Statement': ['sd', 'sv'],
    'Questions': ['qw', 'qy^d', 'qy', 'qh', 'qo', 'qrr', '^q', 'qw^d', '^g'],
    'Answers': ['nn', 'na', 'ny', 'no', 'ng'],
    'Agreement': ['aa', 'ar', 'ad', '^h', 'aap_am', 'arp_nd'],
    'BackwardFunction': ['b', 'bk', 'bh', 'ba', 'bf', 'br', 'bd', '^2'],
    'ForwardFunction': ['fo_o_fw_"_by_bc', 'fc', 'ft', 'fp', 'fa', 'oo_co_cc', 'fo_o', 'fw'],
    'CommInfoStatus': ['%', 'b^m', 't1', 't3'],
    'Other': ['h', '^q'],
    'NonSpeechVerbal': ['x']
}


def highDAClass(da, DAs):
    if da in DAs['Statement']:
        return 'Statement'
    elif da in DAs['Questions']:
        return 'Questions'
    elif da in DAs['Answers']:
        return 'Answers'
    elif da in DAs['Agreement']:
        return 'Agreement'
    elif da in DAs['BackwardFunction']:
        return 'Backward Function'
    elif da in DAs['ForwardFunction']:
        return 'Forward Function'
    elif da in DAs['CommInfoStatus']:
        return 'CommInfoStatus'
    elif da in DAs['Other']:
        return 'Other'
    elif da in DAs['NonSpeechVerbal']:
        return 'NonSpeechVerbal'


DA_names = ['Other Functions', 'Wh-Question', 'Declarative Yes-No-Question ',
            'Yes-No-Question', 'Statement-non-opinion', 'Action-Directive', 'Hedge',
            'Agree/Accept', 'Backchannel', 'Statement-opinion', 'Acknowledge Ans',
            'No Answer', 'Affirmative Answer', 'Backchannel-Que', 'Yes Answers', 'NonSpeech',
            'Uninterpretable', 'Appreciation', 'Reformulate', 'Repeat Phrase',
            'Rhetorical-Question', 'Other Answers', 'Self-talk', 'Open-Question',
            'Hold', 'Or-Clause', 'Open Option', 'Quotation', 'Completion',
            'Signal-non-understand', 'Maybe/Accept-part', 'Downplayer',
            'Tag-Question', 'Conv. Closing', 'Thanking', 'Reject', '3rd-party-talk ',
            'Negative Answer', 'Info-Request', 'Conv. Opening', 'Apology', 'Reject-part']


def returnDAname(da, tag, DA_names):
    return DA_names[tag.index(da)]
