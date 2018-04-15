# -*- coding: utf-8 -*-
import json
import codecs
import re
import jieba
from zhon.hanzi import punctuation
import string

regstring = '[' + punctuation + string.punctuation +']+'

with open('train_data_complete.json', 'r') as f:
    json_text = f.read()

data = json.loads(json_text)

for item in data:
    for passage in item['passages']:
        content = passage['content']
        content  = re.sub(regstring, " ",content)
        # re.sub(ur"[%s]+" %punctuation, "", line.decode("utf-8"))
        passage['accute_seg_content'] = ' '.join(list(jieba.cut(content)))
        # passage['all_seg_content'] = ' '.join(jieba.cut(content, cut_all = True))
        # passage['search_seg_content'] = ' '.join(jieba.cut_for_search(content))
    question = item['question']
    question = re.sub(regstring, " ", question)
    item['question'] = {}
    item['question']['question'] = question
    item['question']['accute_seg_question'] = ' '.join(list(jieba.cut(question)))
    # item['question']['all_seg_question'] = ' '.join(jieba.cut(question,cut_all = True))
    # item['question']['search_seg_question'] = ' '.join(jieba.cut_for_search(question))


with open('train_data_complete_jieba.json', 'w') as f:
    json.dump(data,f,ensure_ascii=False)


# regstring = "[\s+\.\!\/\?\-\\_,$%^*()+;:<>\"\']+|[+——！，。？、~@#￥%……&*（）“”《 》：；≤≥【】\[\]①②③④⑤⑥⑦⑧⑨⑩〖〗「」〈〉．＜＞©〔〕～℃＝]+"

# with codecs.open('data.txt', 'w', 'utf-8') as f:
#     for item in data:
#         for passage in item['passages']:
#             string = passage['content']
#             string  = re.sub(regstring.decode("utf8"), "".decode("utf8"),string)
#             f.write(string)

# with codecs.open('data_train.txt', 'w', 'utf-8') as f:
#     for item in data:
#         question = item['question']
#         question = re.sub(regstring.decode("utf8"), "".decode("utf8"),question)
#         for passage in item['passages']:
#             string = passage['content']
#             # print string
#             string = re.sub(regstring.decode("utf8"), "".decode("utf8"),string)
#             # print string
#             string = string + ' || ' + question +' || ' + str(passage['label']) + '\n'
#             f.write(string)
