import json

vec = {}
jsdata = {}

with open('taidi_model.vec','r') as f:
	count, dim = f.readline().split()
	print(count,dim)
	for line in f:
		ll = line.split()
		l = list(map(float32,ll[1:]))
		vec[ll[0]] = l
	vec['-NULL-'] = [0.] * int(dim)
	jsdata['word2vec'] = vec

with open('shared_train.json','w') as f:
	json.dump(jsdata, f,ensure_ascii = False)