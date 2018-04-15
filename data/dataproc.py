# -*- coding: utf-8 -*-
import json
import codecs
import re

with codecs.open('train_data_complete.json', 'r', 'utf-8') as f:
    json_text = f.read()

data = json.loads(json_text)

regstring = "[\s+\.\!\/\?\-\\_,$%^*()+;:<>\"\']+|[+——！，。？、~@#￥%……&*（）“”《 》：；≤≥【】\[\]①②③④⑤⑥⑦⑧⑨⑩〖〗「」〈〉．＜＞©〔〕～℃＝]+"

with codecs.open('data.txt', 'w', 'utf-8') as f:
    for item in data:
        for passage in item['passages']:
            string = passage['content']
            string  = re.sub(regstring.decode("utf8"), "".decode("utf8"),string)
            f.write(string)

with codecs.open('data_train.txt', 'w', 'utf-8') as f:
    for item in data:
        question = item['question']
        question = re.sub(regstring.decode("utf8"), "".decode("utf8"),question)
        for passage in item['passages']:
            string = passage['content']
            # print string
            string = re.sub(regstring.decode("utf8"), "".decode("utf8"),string)
            # print string
            string = string + ' || ' + question +' || ' + str(passage['label']) + '\n'
            f.write(string)