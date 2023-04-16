from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def greet_mission():
    return "<p><b>Миссия Колонизация Марса</b></p>"


@app.route('/index')
def index():
    return "<p><b>И на Марсе будут яблони цвести!</b></p>"


@app.route('/promotion')
def promotion():
    promotion_list = '''Человечество вырастает из детства.

Человечеству мала одна планета.

Мы сделаем обитаемыми безжизненные пока планеты.

И начнем с Марса!

Присоединяйся!'''.split('\n\n')
    return '<p><b></br>'.join(promotion_list)


@app.route('/mars_image')
def mars_page():
    return f'''<head>
                <h1>Жди нас, марс!</h1>
                <title>Привет, Марс!</title>
                </head>
                <body>
    
    <img src="{url_for('static', filename='img/MARS.png')}" 
       alt="здесь должна была быть картинка, но не нашлась">
                </body>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
