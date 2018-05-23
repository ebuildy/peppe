import argparse, glob, os

from whoosh.analysis import CharsetFilter, StemmingAnalyzer
from whoosh import fields
from whoosh.support.charset import accent_map

def main(args):
    my_analyzer = StemmingAnalyzer() | CharsetFilter(accent_map)

    for filename in glob.glob(args.dir + "/*.txt"):
        with open(filename, 'r') as readfile:
            infile = readfile.readlines()
            label = "__label__" + os.path.splitext(os.path.basename(readfile.name))[0] + " "
            for line in infile:
                tokens = my_analyzer(line.strip())
                words = [token.text for token in tokens]

                #print(line.strip())
                print(label + ' '.join(words))
                #print()

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Build corpus.')

    parser.add_argument('dir', type=str, help='directory')

    args = parser.parse_args()

    main(args)
