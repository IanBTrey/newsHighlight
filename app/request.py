
# Getting the API key, base url and article base url
api_key = None
base_url = None
article_base_url = None

def configure_request(app):
    global api_key,base_url, article_base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    article_base_url = app.config['ARTICLES_API_BASE_URL']


def get_sources():
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(api_key)
    # print(get_sources_url)
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_results(sources_results_list)


    return sources_results
