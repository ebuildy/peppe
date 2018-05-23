![](https://beemapp2.s3.amazonaws.com/cf33380b-f2e3-482a-ace3-9c38fc4c0b32.jpg)

![](https://beemapp2.s3.amazonaws.com/e0e2c84e-24b1-4101-980a-19f8197ebf51.jpg)

peppe is a HTTP API to "obtain the k most likely labels for a piece of text" with fasttext.

You still must build your model manually.

## Installation

    pipenv install
    pipenv shell


## Usage

### Run web server

    FLASK_APP=src/api.py flask run

Open ``http://127.0.0.1:5000/`` in a browser to see available endpoints.

### Build clean corpus

    python ./src/build_corpus.py ./src/corpus > ./build/fr.txt

### Build models

    # You need fasttext bin somewhere
    # Put model under models folder
    fasttext supervised -input build/cooking.train -output models/cooking -lr 1.0 -epoch 25
