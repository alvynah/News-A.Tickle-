from flask import render_template
from app import app
from .requests import get_newsSources

# Views


@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    sources_categories = get_newsSources('general')
    title="News A.tickle - fun and up-to-date news headlines"
    return render_template('index.html', title=title,general=sources_categories)

@app.route('/news.atickle/<int:id>')
def newatickles(id):
    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('newsources.html', id=news_id)
