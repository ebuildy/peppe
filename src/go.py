import fasttext

# Skipgram model
model = fasttext.skipgram('build/cooking.stackexchange.txt', './models/fr')
print(model.words) # list of words in dictionary

# CBOW model
model = fasttext.cbow('build/cooking.stackexchange.txt', './models/fr')
print(model.words)
