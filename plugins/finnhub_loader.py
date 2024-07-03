import finnhub

def scrape_news():
    with open('./data/api_key.txt', 'r') as key_file:
        api_key = key_file.read().strip()

    finnhub_client = finnhub.Client(api_key= api_key)

    news = finnhub_client.general_news('general', min_id=0)

    return news