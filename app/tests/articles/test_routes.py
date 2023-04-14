from app.articles.models import Article

def test_get_published_renders(client):
    #page loads and renders publish page
    response = client.get('/publisharticle')
    assert b'Content' in response.data

def test_post_published_creates_article(client):
    #creates an article
    response = client.post('/publisharticle', data={
        'title': 'From the East to the West and Halfway Back',
        'reading_time': '5 mins',
        'text': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.',
    })
    assert Article.query.first() is not None
