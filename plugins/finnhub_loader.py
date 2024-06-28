import finnhub

def scrape_news():
    finnhub_client = finnhub.Client(api_key="cptutg9r01qnga5io0g0cptutg9r01qnga5io0gg")

    news = finnhub_client.general_news('general', min_id=0)

    return news