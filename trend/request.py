import urllib.request,json
from .models import News


NEWS_API_BASE_URL='https://newsapi.org/v2/everything?q={}&apiKey={}'
NEWS_API_KEY='42621ea7be204cc899887a2fc2856ab7'


N_base_url=NEWS_API_BASE_URL
api_key=NEWS_API_KEY



def get_news(source):
    '''
    Function to get the json response to our url request
    '''
    get_news_url = N_base_url.format(source,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)
    
    return news_results

def process_results(news_list):
    '''
    Function to process movie results obtained by the api to 
    convert it to a list of objects
    
    Args:
        news_list: list of dictionaries with news details
    Returns:
        news_results: list of news objects
    '''

    news_results = []
    for news_item in news_list:
    
        author = news_item.get('author')
        title = news_item.get('title')
        description = news_item.get('description')
        urlToImage = news_item.get('urlToImage')
        publishedAt= news_item.get('publishedAt')
        content = news_item.get('content')
        
        

        if urlToImage:
            news_object = News(author,title,description,urlToImage,publishedAt,content)
            news_results.append(news_object)
            

    return news_results