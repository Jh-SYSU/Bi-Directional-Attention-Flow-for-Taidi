./fasttext skipgram -input data/data/data.txt -output result/taidi -lr 0.025 -dim 100 \
       -ws 5 -epoch 1 -minCount 5 -neg 5 -loss ns -bucket 2000000 \
         -minn 3 -maxn 6 -thread 4 -t 1e-4 -lrUpdateRate 100
