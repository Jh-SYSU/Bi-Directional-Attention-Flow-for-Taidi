# -*- coding: utf-8 -*-
import json
import codecs
import re
import jieba
from zhon.hanzi import punctuation
import string



# to input format
def dataproc(filename):
    with codecs.open(filename, 'r', 'utf-8') as f:
        json_text = f.read()    
    data = json.loads(json_text)

    x, y, q, idx = [],[],[],[]

    for item in data:
        # question
        q.append(item['question']['accute_seg_question'].split())

        # x [article[context]]
        article,labels,ids = [],[],[]
        for passage in item['passages']:
            article.append(passage['accute_seg_content'].split())
            labels.append(passage['label'])
            ids.append(passage['passage_id'])
        x.append(article)
        y.append(labels)
        idx.append(ids)

    out_data = {'x':x, 'y':y, 'q':q, 'idx':idx}
    print("saving ...")
    with open('xyq'+filename,  'w') as f:
        json.dump(out_data, f, ensure_ascii=False)


dataproc('train_data_jieba_25k.json')
dataproc('dev_data_jieba_5k.json')


# regstring = '[' + punctuation + string.punctuation +']+'

# with codecs.open('train_data_complete.json', 'r', 'utf-8') as f:
#     json_text = f.read()

# data = json.loads(json_text)

# for item in data:
#     for passage in item['passages']:
#         content = passage['content']
#         content  = re.sub(regstring, " ",content)
#         # re.sub(ur"[%s]+" %punctuation, "", line.decode("utf-8"))
#         passage['accute_seg_content'] = ' '.join(jieba.cut(content))
#         # passage['all_seg_content'] = ' '.join(jieba.cut(content, cut_all = True))
#         # passage['search_seg_content'] = ' '.join(jieba.cut_for_search(content))
#     question = item['question']
#     question = re.sub(regstring, " ", question)
#     item['question'] = {}
#     item['question']['question'] = question
#     item['question']['accute_seg_question'] = ' '.join(jieba.cut(question))
#     # item['question']['all_seg_question'] = ' '.join(jieba.cut(question,cut_all = True))
#     # item['question']['search_seg_question'] = ' '.join(jieba.cut_for_search(question))


# with codecs.open('train_data_complete_jieba.json', 'w', 'utf-8') as f:
#     json.dump(data,f,ensure_ascii=False)

# train dev split
####################################################################
# with codecs.open('train_data_complete_jieba.json', 'r', 'utf-8') as f:
#     json_text = f.read()

# data = json.loads(json_text)

# train, dev = [],[]

# for i in range(len(data)):
#     if i%6 == 5:
#         dev.append(data[i])
#     else:
#         train.append(data[i])

# with codecs.open('train_data_jieba_25k.json', 'w', 'utf-8') as f:
#     json.dump(train,f,ensure_ascii=False)

# with codecs.open('dev_data_jieba_5k.json', 'w', 'utf-8') as f:
#     json.dump(dev,f,ensure_ascii=False)
######################################################################

# data to train word embedding
#############################################################
# with codecs.open('data.txt', 'w', 'utf-8') as f:
#     for item in data:
#         for passage in item['passages']:
#             if passage['label'] == 1:
#                 f.write(passage['accute_seg_content']+' ')
#         f.write(item['question']['accute_seg_question']+' ')
#         for passage in item['passages']:
#             if passage['label']==0:
#                 f.write(passage['accute_seg_content']+' ')
##########################################################################

