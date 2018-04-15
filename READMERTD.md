## Requirements
#### General
- Python (verified on 3.5.2. Issues have been reported with Python 2!)
- unzip

#### Python Packages
- tensorflow (verified on 0.12)
- nltk (NLP tools, verified on 3.2.1)
- tqdm (progress bar, verified on 4.7.4)
- jinja2 (for visaulization; if you only train and test, not needed)



## Pre-processing
see `fasttext-taidi/datapreprocess/README.md`


## Training
Before training, it is recommended to first try the following code to verify everything is okay and memory is sufficient:
```
python -m basic.cli --mode train --noload --debug
```

Then to fully train, run:
```
python -m basic.cli --mode train --noload
```

## Test
To test, run:
```
python -m basic.cli mode --predict
```
