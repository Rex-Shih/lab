Each line is a jsonl object of a dialogue with the following format:
{
    "DailyDialog_id": Str,
    "split": Str, # ['train', 'valid', 'test'] split in DailyDialog
    "dialog_id": Str, # id in each split
    "dialogue": Str, 
    "events": EventList, 
    "coreferences": List, # a list of cluster_lists, each cluster_list is a list of tokens_id. Note that the 1st cluster must be S1 cluster and the 2nd must be S2. The S1/S2 might be an empty cluster.
    "coreferences_tokens": List, # for human readable, each cluster_list is a list of tokens
}

EventList = [
    # events_per_turn:
    [
        # event:
        {
            "participants": {
                'predicate': EntityDict, 
                'subject': EntityDict,
                'object': EntityDict,
            },
            "event_status": { 
                'polarity': Bool, # 1: positive, 0: negative
                'modality': Bool, # 1: actual, 0: hypothetical
                'time': Str or Dict, # ['before', 'now', 'continuously', 'after', or an EntityDict refers to time in the dialogue
            },
            "event_info":{
                'explicit': Bool, # 1: explicit, 0: implicit
                'frame_name': Str,
                'predicate_class': Str,
            }
        }, {}, ...
    ], [], ...
]


EntityDict = {
    "entity_id": Int, # which is also the index of cluster in the "coreferences" field
    "tokens": Str,
    "token_list": List, # list of tokens
    "group_num": Str,
    "tokens_id": Str
}
if no object: object = {}