import wikipedia


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
