from flask import render_template
from app import app
from .requests import get_newsSources,get_article

# Views


@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    sources_categories = get_newsSources('general')
    title="News A.tickle - fun and up-to-date news headlines"
    return render_template('index.html', title=title,general=sources_categories)

@app.route('/news.atickle/<id>')
def newatickles(id):
    '''
    View movie page function that returns the movie details page and its data
    '''
    article_items=get_article(id)
    title=f'{id}'
    return render_template('news.atickle.html', title=title, articles=article_items)

