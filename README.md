## Installation

``pipenv install``

## Usage

### Run web server

    FLASK_APP=src/api.py flask run

### Build clean corpus

    python ./src/build_corpus.py ./src/corpus > ./build/fr.txt

### Build models

    # You need fasttext bin somewhere
    # Put model under models folder
    fasttext supervised -input build/cooking.train -output models/cooking -lr 1.0 -epoch 25
