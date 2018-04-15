Put train_data_complete.json in this directory.

We use fastText and jieba to train word embedding.

please build fastText first.

python3 and jieba are required to run the following:


transform train_data_complete.json to data.txt which used to train word embedding:

```
$ python dataproc.py
$ python dataproc2.py
```


In order to learn word vectors, do:

```
$ ./../fasttext skipgram -input data.txt -output taidi
$ python vectojson.py
$ mv shared_train.json ../../data/shared_train.json
```



train-test split:
```
$ python dataproc3.py
$ python dataproc4.py
$ mv train_data_jieba_25k.json ../../data/data_train.json
$ mv dev_data_jieba_5k.json ../../data/data_pridict.json
```