from whoosh.analysis import CharsetFilter, StemmingAnalyzer
from whoosh import fields
from whoosh.support.charset import accent_map

def analyze(text):
    my_analyzer = StemmingAnalyzer() | CharsetFilter(accent_map)

    tokens = my_analyzer(text.strip())

    words = [token.text for token in tokens]

    return words
