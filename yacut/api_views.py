from flask import jsonify, request, url_for

from yacut import app
from yacut.services import URLMapService


@app.route('/api/id/', methods=['POST'])
def create_short_link():
    """Создание короткой ссылки через API."""
    data = request.get_json(silent=True)
    
    if data is None:
        return jsonify({'message': 'Отсутствует тело запроса'}), 400
    
    if 'url' not in data:
        return jsonify({'message': '"url" является обязательным полем!'}), 400
    
    original_url = data['url']
    custom_id = data.get('custom_id')
    
    try:
        url_map = URLMapService.create_url_map(original_url, custom_id)
        short_link = url_for('redirect_to_original', short_id=url_map.short, _external=True)
        
        return jsonify({
            'url': original_url,
            'short_link': short_link
        }), 201
    except ValueError as e:
        return jsonify({'message': str(e)}), 400


@app.route('/api/id/<short_id>/', methods=['GET'])
def get_original_url(short_id):
    """Получение оригинальной ссылки по короткому идентификатору."""
    url_map = URLMapService.get_by_short_id(short_id)
    
    if not url_map:
        return jsonify({'message': 'Указанный id не найден'}), 404
    
    return jsonify({'url': url_map.original}), 200