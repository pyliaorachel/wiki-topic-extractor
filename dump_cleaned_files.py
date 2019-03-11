import wikipedia
import re
import requests


def _wiki_request(lang, params):
    api_url = 'http://{}.wikipedia.org/w/api.php'.format(lang)
    params['format'] = 'json'
    params['action'] = 'query'

    r = requests.get(api_url, params=params)
    return r.json()

def split_sent(text):
    text = text.strip()
    text = re.sub('\.[\.]+', '<dots>', text) # avoid dots being mixed up with periods
    splits = re.split('(。|？+|！+|\?+|!+|\.)', text)

    # Join every two elements in list, one the main sentence, one the delimeter punctuation
    splits = [''.join(x) for x in zip(splits[0::2], splits[1::2])]

    splits = [re.sub('<dots>', '...', split) for split in splits]
    return splits

def extract_links(topic):
    try:
        top = wikipedia.page(topic)
    except:
        raise Exception('Please provide a wikipedia article')

    topic_links = []

    for link in top.links:
        if 'list' in link.lower():
            topic_links.append(wikipedia.page(link).links)

    print('{} links downloaded'.format(topic))

    flat_top_links = [link for group in topic_links for link in group]
    return flat_top_links

def create_cleaned_files(topic, lang):
    print('Extracting links')
    topic_links = extract_links(topic)

    print('Writing {} articles in data/ folder'.format(topic))
    wikipedia.wikipedia._wiki_request = lambda params: _wiki_request(lang, params)

    sent_cnts = 0
    with open('data/wiki_{}.{}.txt'.format(topic, lang), 'w') as fout:
        for link in topic_links:
            try:
                output_content = wikipedia.page(link).content.strip()
                fout.write(output_content)
                sent_cnt = len(split_sent(output_content))

                print('{} sentences extracted'.format(sent_cnt))
                sent_cnts += sent_cnt
            except Exception as e:
                print(e)

    print('Total sentence count: {}'.format(sent_cnts))