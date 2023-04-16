from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def greet_mission():
    return "<p><b>Миссия Колонизация Марса</b></p>"


@app.route('/index')
def index():
    return "<p><b>И на Марсе будут яблони цвести!</b></p>"

promotion_list = '''Человечество вырастает из детства.
Человечеству мала одна планета.
Мы сделаем обитаемыми безжизненные пока планеты.
И начнем с Марса!
Присоединяйся!'''.split('\n')


@app.route('/promotion')
def promotion():
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


@app.route('/bootstrap_sample')
def bootstrap():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/MARS.png')}" 
       alt="здесь должна была быть картинка, но не нашлась">
                    <div class="alert alert-primary" role="alert">
                      <b>Человечество вырастает из детства.</b>
                    </div>
                    <div class="alert alert-danger" role="alert">
                      <b>Человечеству мала одна планета.</b>
                    </div>
                    <div class="alert alert-info" role="alert">
                      <b>Мы сделаем обитаемыми безжизненные пока планеты.</b>
                    </div>
                    <div class="alert alert-success" role="alert">
                      <b>И начнем с Марса!</b>
                    </div>
                    <div class="alert alert-dark" role="alert">
                      <b>Присоединяйся!</b>
                    </div>
    
    
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
