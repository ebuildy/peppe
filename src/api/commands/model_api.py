import glob, os, fastText

from whoosh.analysis import CharsetFilter, StemmingAnalyzer
from whoosh import fields
from whoosh.support.charset import accent_map

from datetime import datetime

from flask import abort

_g_models = {}

def _load_model(modelName, force=False):
    modelFilePath = "./models/" + modelName + ".bin"

    if modelName not in _g_models or force:
        if os.path.isfile(modelFilePath):
            _g_models[modelName] = fastText.load_model(modelFilePath)
        else:
            raise abort(404, "Model not found!")

    return _g_models[modelName]

def call(modelName):
    model = _load_model(modelName)

    return {
        """
        'name' : model.name,
        'dim' : model.dim,
        'min_count' : model.min_count,
        'bucket' : model.bucket,
        'encoding' : model.encoding,
        'word_ngrams' : model.word_ngrams,
        'loss_name' : model.loss_name,
        'minn' : model.minn,
        'maxn' : model.maxn,
        't' : model.t,
        'neg' : model.neg,
        """
    }

def labels(modelName):
    model = _load_model(modelName)

    return list(model.get_labels())

def words(modelName):
    model = _load_model(modelName)

    return list(model.get_words())

def reload(modelName):
    _load_model(modelName, True)

    return 'ok'

def predict(modelName, text):
    model = _load_model(modelName)

    my_analyzer = StemmingAnalyzer() | CharsetFilter(accent_map)

    tokens = my_analyzer(text.strip())

    words = [token.text for token in tokens]

    sentence = ' '.join(words)

    a = datetime.now()

    l_labels,l_probs = model.predict(sentence, 10)

    b = datetime.now()

    delta = b - a

    ret = {}

    for i in range(len(l_labels)):
        if i < len(l_probs):
            ret[l_labels[i].replace("__label__","")] = l_probs[i]

    return {
        'took' : delta.microseconds,
        'sentence' : sentence,
        'labels' : ret
    }

def cat_models():
    ret = []
    for filename in glob.glob("./models/*.bin"):
        ret.append(os.path.splitext(os.path.basename(filename))[0])

    return ret
