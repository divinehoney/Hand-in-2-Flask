from flask import Blueprint, render_template, request, current_app
from .models import Author

blueprint = Blueprint('authors', __name__)

@blueprint.route('/authors/')
def list_of_authors():
    page_number = request.args.get('page', 1, type=int)
    authors_pagination = Author.query.paginate(page=page_number, per_page=current_app.config['AUTHORS_PER_PAGE'])
    return render_template('authors/index.html', html_authors=authors_pagination)