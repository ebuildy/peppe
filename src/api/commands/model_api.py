import glob, os, fastText

def _load_model(modelName):
    modelFilePath = "./models/" + modelName + ".bin"

    if os.path.isfile(modelFilePath):
        return fastText.load_model(modelFilePath)
    else:
        raise NameError("Model not found!")

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

def predict(modelName, text):
    model = _load_model(modelName)

    l_labels,l_probs = model.predict(text)

    ret = []

    for i in range(len(l_labels[0])):
        ret.append([l_labels[0][i].replace("__label__",""),l_probs[0][i]])

    return ret

def cat_models():
    ret = []
    for filename in glob.glob("./models/*.bin"):
        ret.append(os.path.splitext(os.path.basename(filename))[0])

    return ret
