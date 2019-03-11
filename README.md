# Wikipedia Topic Extractor

Corpus extractor for a sepcific Wikipedia topic.

## Usage

Install dependencies:

```bash
$ pip install -r requirements.txt
```

Extract:

```bash
$ mkdir data

$ python run.py TOPIC --lang LANG
# e.g.
$ python run.py Computer_Science --lang zh
```
outputs data file to `data/wiki_TOPIC.LANG.txt`.

*Note that the topic is recommended to be in English even if you specifies another language so as to get more results.*

## Credits

This project is built on [Wronskia/Wikipedia-topic-classifier](https://github.com/Wronskia/Wikipedia-topic-classifier).