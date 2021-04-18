from app import app
import urllib.request,json
from .models import newsources,articles
Sources = newsources.Sources
Articles = articles.Articles




# Getting api key
api_key = app.config['NEWS_API_KEY']

#Getting Sources base url
base_url=app.config["NEWS_API_BASE_URL"]

#Getting Articles base url
articles_base_url = app.config["ATICKLES_API_BASE_URL"]

def get_newsSources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data= url.read()
        get_sources_response= json.loads(get_sources_data)

        sources_results= None

        if get_sources_response['sources']:
            sources_results_list=  get_sources_response['sources']
            sources_results= process_sources_results(sources_results_list)


    return sources_results

def process_sources_results(sources_list):
    """
    Function  that processes the sources result and transform them to a list of Objects

    Args:
        sources_list: A list of dictionaries that contain sources details

    Returns :
        sources_results: A list of source objects
    """

    sources_results= []
    for source_item in sources_list:
        id= source_item.get('id')
        name= source_item.get('name')
        description= source_item.get('description')
        url= source_item.get('url')
        category= source_item.get('category')
        language= source_item.get('language')
        country= source_item.get('country')

        # if poster:
        source_object= Sources(id, name, description, url, category, language, country)
        sources_results.append(source_object)

    return sources_results


def get_article(id):
    get_article_url = articles_base_url.format(id, api_key)

    with urllib.request.urlopen(get_article_url) as url:
       get_article_data = url.read()
       get_article_response = json.loads(get_article_data)

       article_results = None

       if get_article_response['articles']:
           article_results_list = get_article_response['articles']
           article_results=process_article_results(article_results_list)
    
    return article_results


def process_article_results(article_list):
    """
    Function  that processes the articles result and transform them to a list of Objects

    Args:
        article_list: A list of dictionaries that contain articles details

    Returns :
        article_results: A list of source objects
    """

    article_results = []
    for article_item in article_list:
        id = article_item.get('id')
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')
        content = article_item.get('content')

        if urlToImage:
            article_object = Articles(id, author, title, description, url, urlToImage, publishedAt, content)
            article_results.append(article_object)

    return article_results

            
