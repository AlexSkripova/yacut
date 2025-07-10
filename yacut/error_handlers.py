from flask import jsonify, render_template, request

from yacut import app


def is_api_request():
    """Определяет, является ли запрос API запросом."""
    return request.path.startswith('/api/')


@app.errorhandler(404)
def not_found_error(error):
    """Обработчик ошибки 404 - страница не найдена."""
    if is_api_request():
        return jsonify({'message': 'Указанный id не найден'}), 404
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    """Обработчик ошибки 500 - внутренняя ошибка сервера."""
    if is_api_request():
        return jsonify({'message': 'Внутренняя ошибка сервера'}), 500
    return render_template('errors/500.html'), 500