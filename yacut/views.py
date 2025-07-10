from flask import abort, flash, redirect, render_template, url_for

from yacut import app
from yacut.forms import URLForm
from yacut.services import URLMapService


@app.route('/', methods=['GET', 'POST'])
def index():
    """View-функция для главной страницы."""

    form = URLForm()
    short_link = None

    if form.validate_on_submit():
        original_url = form.original_link.data
        custom_id = form.custom_id.data

        try:
            url_map = URLMapService.create_url_map(original_url, custom_id)
            short_link = url_for('redirect_to_original',
                                 short_id=url_map.short, _external=True)
        except ValueError as e:
            flash(str(e), 'error')

    return render_template('index.html', form=form, short_link=short_link)


@app.route('/<short_id>')
def redirect_to_original(short_id):
    """View-функция для переадресации."""
    url_map = URLMapService.get_by_short_id(short_id)
    if not url_map:
        abort(404)
    return redirect(url_map.original)