from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from openapi.auth import login_required
from openapi.db import get_db
from openapi.google import get_document_content
from openapi.openai import generate_text

bp = Blueprint('document', __name__)


@bp.route('/')
def index():
    db = get_db()
    documents = db.execute(
        'SELECT d.id, link, created, owner_id'
        ' FROM document d JOIN user u ON d.owner_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()

    return render_template('document/index.html', documents=documents)


@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        link = request.form['link']
        text = get_document_content(link)
        response = generate_text(text)

        print(response)
        context = {'text': text, 'response': response}
        return render_template('document/create.html', context=context)

    return render_template('document/create.html', context={})
