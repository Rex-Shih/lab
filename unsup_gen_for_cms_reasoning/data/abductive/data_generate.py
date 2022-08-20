import json
with open('./data/LED/annotation_test.jsonl', 'r') as f:
    j_list = list(f)
f.close()
dialogue = []
event = []
for json_str in j_list:
    result = json.loads(json_str)
    #print(reslut['dialogue'])
    dialogue.append(result['dialogue'])
    event.append(result['events'])
id_list = [6, 14, 24, 27, 37, 40, 41, 44, 46, 51, 52, 54, 57, 58, 60, 62, 64, 65, 66, 69]
#id = 69
#print(dialogue[id])
with open('./augmentation_reveal.json', 'w') as fw:
    aug = 0
    for i in id_list:
        js = {"obs1" : "", "obs2" : ""}
        count = 0
        dia_list = dialogue[i].split('\n')
        if dia_list[-1] == '':
            dia_list = dia_list[:-1]
        lenn = len(dia_list)
        for sent in dia_list:
            sent = sent.replace('S1 :', '')
            sent = sent.replace('S2 :', '')

            sent = sent+"<|endoftext|>"
            if aug<10:
                if count<1:
                    js['obs1']+=sent
                elif count>1:
                    js['obs2']+=sent
                else:
                    js['obs1']+=sent.split(' ')[0]+sent.split(' ')[1]
            else:
                if lenn-count>2:
                    js['obs1']+=sent
                elif lenn-count<2:
                    js['obs2']+=sent
                else:
                    js['obs1']+=sent.split(' ')[0]+sent.split(' ')[1]
            count+=1
        aug+=1
        fw.write(json.dumps(js) + '\n')
        fw.flush()
fw.close()
with open('./augmentation.json', 'w') as fw:
    aug = 0
    for i in id_list:
        js = {"obs1" : "", "obs2" : ""}
        count = 0
        dia_list = dialogue[i].split('\n')
        if dia_list[-1] == '':
            dia_list = dia_list[:-1]
        lenn = len(dia_list)
        for sent in dia_list:
            sent = sent.replace('S1 :', '')
            sent = sent.replace('S2 :', '')

            sent = sent+"<|endoftext|>"
            if aug<10:
                if count<1:
                    js['obs1']+=sent
                elif count>1:
                    js['obs2']+=sent
                #else:
                    #js['obs1']+=sent.split(' ')[0]+sent.split(' ')[1]
            else:
                if lenn-count>2:
                    js['obs1']+=sent
                elif lenn-count<2:
                    js['obs2']+=sent
                #else:
                    #js['obs1']+=sent.split(' ')[0]+sent.split(' ')[1]
            count+=1
        aug+=1
        fw.write(json.dumps(js) + '\n')
        fw.flush()
fw.close()