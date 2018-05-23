import glob, os

def call():
    ret = []
    for filename in glob.glob("./models/*.bin"):
        ret.append(os.path.splitext(os.path.basename(filename))[0])

    return ret
