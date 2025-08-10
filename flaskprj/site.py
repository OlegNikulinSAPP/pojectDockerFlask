from flask import Flask

app = Flask(__name__)  # Создаём экземпляр Flask-приложения


@app.route('/')  # Декоратор для корневого URL
def index():
    return '<h1>Hello from Docker and from flaskprj!</h1>'  # Ответ на запрос


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4000)  # Запуск сервера
