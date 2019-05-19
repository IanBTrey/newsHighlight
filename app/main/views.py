



#Views
@main.route('/')
def index():
    '''
    View root page that returns the index page and its data
    '''
    sources = get_sources()
    articles = get_articles('kenya')
    title = "news,gossips and everything nice!"
