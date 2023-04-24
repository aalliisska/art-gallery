from flask import Flask, url_for, request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def page():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Картинная галерея выдающихся русских художников</title>
                          </head>
                          <body>
                          <h1 align="center">Картинная галерея выдающихся русских художников</h1>
                          <p align="center">img src="{url_for('static', filename='img/0.jpeg')}"</p>
                          <a href="{{ url_for('polenov') }}"><span><h1 align="center">Художник Василий Дмитриевич Поленов</h1></span></a>
                          <a href="{{ url_for('surikov') }}"><span><h1 align="center">Художник Василий Иванович Суриков</h1></span></a>
                          <a href="{{ url_for('brulev') }}"><span><h1 align="center">Художник Карл Павлович Брюллов</h1></span></a>
                          <a href="{{ url_for('sagal') }}"><span><h1 align="center">Художник Марк Захарович Шагал</h1></span></a>
                          <a href="{{ url_for('petrov-vodkin') }}"><span><h1 align="center">Художник Кузьма Сергеевич Петров-Водкин</h1></span></a>
                          </body>
                        </html>'''

@app.route('/polenov', methods=['POST', 'GET'])
def carousel():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Выставка картин. Художник Василий Дмитриевич Поленов</title>
                          </head>
                          <body>
                            <h1 align="center">Выставка картин. Художник Василий Дмитриевич Поленов.</h1>
                            <div align="center" id="carousel-example-generic" class="carousel slide" data-ride="carousel">
                              <ol class="carousel-indicators">
                                <li data-target="#carousel-example-generic" data-slide-to="0" class="active"></li>
                                <li data-target="#carousel-example-generic" data-slide-to="1"></li>
                                <li data-target="#carousel-example-generic" data-slide-to="2"></li>
                                <li data-target="#carousel-example-generic" data-slide-to="3"></li>
                                <li data-target="#carousel-example-generic" data-slide-to="4"></li>
                                <li data-target="#carousel-example-generic" data-slide-to="5"></li>
                                <li data-target="#carousel-example-generic" data-slide-to="6"></li>
                                <li data-target="#carousel-example-generic" data-slide-to="7"></li>
                                <li data-target="#carousel-example-generic" data-slide-to="8"></li>
                                <li data-target="#carousel-example-generic" data-slide-to="9"></li>
                                <li data-target="#carousel-example-generic" data-slide-to="10"></li>
                                <li data-target="#carousel-example-generic" data-slide-to="11"></li>
                                <li data-target="#carousel-example-generic" data-slide-to="12"></li>
                                <li data-target="#carousel-example-generic" data-slide-to="13"></li>
                                <li data-target="#carousel-example-generic" data-slide-to="14"></li>
                                <li data-target="#carousel-example-generic" data-slide-to="15"></li>
                                <li data-target="#carousel-example-generic" data-slide-to="16"></li>
                                <li data-target="#carousel-example-generic" data-slide-to="17"></li>
                                <li data-target="#carousel-example-generic" data-slide-to="18"></li>
                              </ol>
                              <div class="carousel-inner" role="listbox">
                                <div class="carousel-item active">
                                  <img src="/static/img/1.jpeg" alt="First slide">
                                </div>
                                <div class="carousel-item">
                                  <img src="/static/img/2.jpeg" alt="Second slide">
                                </div>
                                <div class="carousel-item">
                                  <img src="/static/img/3.jpeg" alt="Third slide">
                                </div>
                                <div class="carousel-item">
                                  <img src="/static/img/4.jpeg" alt="Third slide">
                                </div>
                                <div class="carousel-item">
                                  <img src="/static/img/5.jpeg" alt="Fourth slide">
                                </div>
                                <div class="carousel-item">
                                  <img src="/static/img/6.jpeg" alt="Fifth slide">
                                </div>
                                <div class="carousel-item">
                                  <img src="/static/img/7.jpeg" alt="Sixth slide">
                                </div>
                                <div class="carousel-item">
                                  <img src="/static/img/8.jpeg" alt="Slide slide">
                                </div>
                                <div class="carousel-item">
                                  <img src="/static/img/9.jpeg" alt="The ninth slide">
                                </div>
                                <div class="carousel-item">
                                  <img src="/static/img/10.jpeg" alt="The tenth slide">
                                </div>
                                <div class="carousel-item">
                                  <img src="/static/img/11.jpeg" alt="The eleventh slide">
                                </div>
                                <div class="carousel-item">
                                  <img src="/static/img/12.jpeg" alt="The twelfth slide">
                                </div>
                                <div class="carousel-item">
                                  <img src="/static/img/13.jpeg" alt="The thirteenth slide">
                                </div>
                                <div class="carousel-item">
                                  <img src="/static/img/14.jpeg" alt="The fourteenth slide">
                                </div>
                                <div class="carousel-item">
                                  <img src="/static/img/15.jpeg" alt="The fifteenth slide">
                                </div>
                                <div class="carousel-item">
                                  <img src="/static/img/16.jpeg" alt="The sixteenth slide">
                                </div>
                                <div class="carousel-item">
                                  <img src="/static/img/17.jpeg" alt="The sixteenth slide">
                                </div>
                                <div class="carousel-item">
                                  <img src="/static/img/18.jpeg" alt="The sixteenth slide">
                                </div>
                              </div>
                              <a class="left carousel-control" href="#carousel" role="button" data-slide="prev">
                                <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
                                <span class="sr-only">Previous</span>
                              </a>
                              <a class="right carousel-control" href="#carousel" role="button" data-slide="next">
                                <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
                                <span class="sr-only">Next</span>
                              </a>
                            </div>
                        </div>
                          </body>
                        </html>'''


@app.route('/surikov', methods=['POST', 'GET'])
def carousel2():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Выставка картин. Художник Василий Иванович Суриков</title>
                          </head>
                          <body>
                            <h1 align="center">Выставка картин. Художник Василий Иванович Суриков.</h1>
                            <div align="center" id="carousel2-example-generic" class="carousel2 slide" data-ride="carousel2">
                              <ol class="carousel2-indicators">
                                <li data-target="#carousel2-example-generic" data-slide-to="19.1" class="active"></li>
                                <li data-target="#carousel2-example-generic" data-slide-to="19"></li>
                                <li data-target="#carousel2-example-generic" data-slide-to="20"></li>
                                <li data-target="#carousel2-example-generic" data-slide-to="21"></li>
                                <li data-target="#carousel2-example-generic" data-slide-to="22"></li>
                                <li data-target="#carousel2-example-generic" data-slide-to="23"></li>
                                <li data-target="#carousel2-example-generic" data-slide-to="24"></li>
                                <li data-target="#carousel2-example-generic" data-slide-to="25"></li>
                                <li data-target="#carousel2-example-generic" data-slide-to="26"></li>
                                <li data-target="#carousel2-example-generic" data-slide-to="27"></li>
                                <li data-target="#carousel2-example-generic" data-slide-to="28"></li>
                                <li data-target="#carousel2-example-generic" data-slide-to="29"></li>
                                <li data-target="#carousel2-example-generic" data-slide-to="30"></li>
                              </ol>
                              <div class="carousel2-inner" role="listbox">
                                <div class="carousel2-item active">
                                  <img src="/static/img/19.1.jpeg" alt="First slide">
                                </div>
                                <div class="carousel2-item">
                                  <img src="/static/img/19.jpeg" alt="Second slide">
                                </div>
                                <div class="carousel2-item">
                                  <img src="/static/img/20.jpeg" alt="Third slide">
                                </div>
                                <div class="carousel2-item">
                                  <img src="/static/img/21.jpeg" alt="Third slide">
                                </div>
                                <div class="carousel2-item">
                                  <img src="/static/img/22.jpeg" alt="Fourth slide">
                                </div>
                                <div class="carousel2-item">
                                  <img src="/static/img/23.jpeg" alt="Fifth slide">
                                </div>
                                <div class="carousel2-item">
                                  <img src="/static/img/24.jpeg" alt="Sixth slide">
                                </div>
                                <div class="carousel2-item">
                                  <img src="/static/img/25.jpeg" alt="Slide slide">
                                </div>
                                <div class="carousel2-item">
                                  <img src="/static/img/26.jpeg" alt="The ninth slide">
                                </div>
                                <div class="carousel2-item">
                                  <img src="/static/img/27.jpeg" alt="The tenth slide">
                                </div>
                                <div class="carousel2-item">
                                  <img src="/static/img/28.jpeg" alt="The eleventh slide">
                                </div>
                                <div class="carousel2-item">
                                  <img src="/static/img/29.jpeg" alt="The twelfth slide">
                                </div>
                              </div>
                              <a class="left carousel2-control" href="#carousel2" role="button" data-slide="prev">
                                <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
                                <span class="sr-only">Previous</span>
                              </a>
                              <a class="right carousel2-control" href="#carousel2" role="button" data-slide="next">
                                <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
                                <span class="sr-only">Next</span>
                              </a>
                            </div>
                        </div>
                          </body>
                        </html>'''

@app.route('/brulev', methods=['POST', 'GET'])
def carousel3():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Выставка картин. Художник Карл Павлович Брюллов</title>
                          </head>
                          <body>
                            <h1 align="center">Выставка картин. Художник Карл Павлович Брюллов</h1>
                            <div align="center" id="carousel3-example-generic" class="carousel3 slide" data-ride="carousel3">
                              <ol class="carousel3-indicators">
                                <li data-target="#carousel3-example-generic" data-slide-to="30" class="active"></li>
                                <li data-target="#carousel3-example-generic" data-slide-to="31"></li>
                                <li data-target="#carousel3-example-generic" data-slide-to="32"></li>
                                <li data-target="#carousel3-example-generic" data-slide-to="33"></li>
                                <li data-target="#carousel3-example-generic" data-slide-to="34"></li>
                                <li data-target="#carousel3-example-generic" data-slide-to="35"></li>
                                <li data-target="#carousel3-example-generic" data-slide-to="36"></li>
                                <li data-target="#carousel3-example-generic" data-slide-to="37"></li>
                                <li data-target="#carousel3-example-generic" data-slide-to="38"></li>
                              </ol>
                              <div class="carousel3-inner" role="listbox">
                                <div class="carousel3-item active">
                                  <img src="/static/img/30.jpeg" alt="First slide">
                                </div>
                                <div class="carousel3-item">
                                  <img src="/static/img/31.jpeg" alt="Second slide">
                                </div>
                                <div class="carousel3-item">
                                  <img src="/static/img/32.jpeg" alt="Third slide">
                                </div>
                                <div class="carousel3-item">
                                  <img src="/static/img/33.jpeg" alt="Third slide">
                                </div>
                                <div class="carousel3-item">
                                  <img src="/static/img/34.jpeg" alt="Fourth slide">
                                </div>
                                <div class="carousel3-item">
                                  <img src="/static/img/35.jpeg" alt="Fifth slide">
                                </div>
                                <div class="carousel3-item">
                                  <img src="/static/img/36.jpeg" alt="Sixth slide">
                                </div>
                                <div class="carousel3-item">
                                  <img src="/static/img/37.jpeg" alt="Slide slide">
                                </div>
                                <div class="carousel3-item">
                                  <img src="/static/img/38.jpeg" alt="The ninth slide">
                                </div>
                                <div class="carousel3-item">
                                  <img src="/static/img/39.jpeg" alt="The tenth slide">
                                </div>
                              </div>
                              <a class="left carousel3-control" href="#carousel3" role="button" data-slide="prev">
                                <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
                                <span class="sr-only">Previous</span>
                              </a>
                              <a class="right carousel3-control" href="#carousel3" role="button" data-slide="next">
                                <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
                                <span class="sr-only">Next</span>
                              </a>
                            </div>
                        </div>
                          </body>
                        </html>'''

@app.route('/sagal', methods=['POST', 'GET'])
def carousel4():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Выставка картин. Художник Марк Захарович Шагал</title>
                          </head>
                          <body>
                            <h1 align="center">Выставка картин. Художник Марк Захарович Шагал</h1>
                            <div align="center" id="carousel4-example-generic" class="carousel4 slide" data-ride="carousel4">
                              <ol class="carousel4-indicators">
                                <li data-target="#carousel4-example-generic" data-slide-to="40" class="active"></li>
                                <li data-target="#carousel4-example-generic" data-slide-to="41"></li>
                                <li data-target="#carousel4-example-generic" data-slide-to="42"></li>
                                <li data-target="#carousel4-example-generic" data-slide-to="43"></li>
                                <li data-target="#carousel4-example-generic" data-slide-to="44"></li>
                                <li data-target="#carousel4-example-generic" data-slide-to="45"></li>
                                <li data-target="#carousel4-example-generic" data-slide-to="46"></li>
                                <li data-target="#carousel4-example-generic" data-slide-to="47"></li>
                                <li data-target="#carousel4-example-generic" data-slide-to="48"></li>
                                <li data-target="#carousel4-example-generic" data-slide-to="49"></li>
                              </ol>
                              <div class="carousel4-inner" role="listbox">
                                <div class="carousel4-item active">
                                  <img src="/static/img/40.jpeg" alt="First slide">
                                </div>
                                <div class="carousel4-item">
                                  <img src="/static/img/41.jpeg" alt="Second slide">
                                </div>
                                <div class="carousel4-item">
                                  <img src="/static/img/42.jpeg" alt="Third slide">
                                </div>
                                <div class="carousel4-item">
                                  <img src="/static/img/43.jpeg" alt="Third slide">
                                </div>
                                <div class="carousel4-item">
                                  <img src="/static/img/44.jpeg" alt="Fourth slide">
                                </div>
                                <div class="carousel4-item">
                                  <img src="/static/img/45.jpeg" alt="Fifth slide">
                                </div>
                                <div class="carousel4-item">
                                  <img src="/static/img/46.jpeg" alt="Sixth slide">
                                </div>
                                <div class="carousel4-item">
                                  <img src="/static/img/47.jpeg" alt="Slide slide">
                                </div>
                                <div class="carousel4-item">
                                  <img src="/static/img/48.jpeg" alt="The ninth slide">
                                </div>
                                <div class="carousel4-item">
                                  <img src="/static/img/49.jpeg" alt="The tenth slide">
                                </div>
                              </div>
                              <a class="left carousel4-control" href="#carousel4" role="button" data-slide="prev">
                                <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
                                <span class="sr-only">Previous</span>
                              </a>
                              <a class="right carousel4-control" href="#carousel4" role="button" data-slide="next">
                                <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
                                <span class="sr-only">Next</span>
                              </a>
                            </div>
                        </div>
                          </body>
                        </html>'''


@app.route('/petrov-vodkin', methods=['POST', 'GET'])
def carousel5():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Выставка картин. Художник Кузьма Сергеевич Петров-Водкин</title>
                          </head>
                          <body>
                            <h1 align="center">Выставка картин. Художник Кузьма Сергеевич Петров-Водкин</h1>
                            <div align="center" id="carousel5-example-generic" class="carousel5 slide" data-ride="carousel5">
                              <ol class="carousel5-indicators">
                                <li data-target="#carousel5-example-generic" data-slide-to="50" class="active"></li>
                                <li data-target="#carousel5-example-generic" data-slide-to="51"></li>
                                <li data-target="#carousel5-example-generic" data-slide-to="52"></li>
                                <li data-target="#carousel5-example-generic" data-slide-to="53"></li>
                                <li data-target="#carousel5-example-generic" data-slide-to="54"></li>
                                <li data-target="#carousel5-example-generic" data-slide-to="55"></li>
                                <li data-target="#carousel5-example-generic" data-slide-to="56"></li>
                                <li data-target="#carousel5-example-generic" data-slide-to="57"></li>
                                <li data-target="#carousel5-example-generic" data-slide-to="58"></li>
                                <li data-target="#carousel5-example-generic" data-slide-to="59"></li>
                                <li data-target="#carousel5-example-generic" data-slide-to="60"></li>
                              </ol>
                              <div class="carousel5-inner" role="listbox">
                                <div class="carousel5-item active">
                                  <img src="/static/img/50.jpeg" alt="First slide">
                                </div>
                                <div class="carousel5-item">
                                  <img src="/static/img/51.jpeg" alt="Second slide">
                                </div>
                                <div class="carousel5-item">
                                  <img src="/static/img/52.jpeg" alt="Third slide">
                                </div>
                                <div class="carousel5-item">
                                  <img src="/static/img/53.jpeg" alt="Third slide">
                                </div>
                                <div class="carousel5-item">
                                  <img src="/static/img/54.jpeg" alt="Fourth slide">
                                </div>
                                <div class="carousel5-item">
                                  <img src="/static/img/55.jpeg" alt="Fifth slide">
                                </div>
                                <div class="carousel5-item">
                                  <img src="/static/img/56.jpeg" alt="Sixth slide">
                                </div>
                                <div class="carousel5-item">
                                  <img src="/static/img/57.jpeg" alt="Slide slide">
                                </div>
                                <div class="carousel5-item">
                                  <img src="/static/img/58.jpeg" alt="The ninth slide">
                                </div>
                                <div class="carousel5-item">
                                  <img src="/static/img/59.jpeg" alt="The tenth slide">
                                </div>
                                <div class="carousel5-item">
                                  <img src="/static/img/60.jpeg" alt="The eleventh slide">
                                </div>
                              </div>
                              <a class="left carousel5-control" href="#carousel5" role="button" data-slide="prev">
                                <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
                                <span class="sr-only">Previous</span>
                              </a>
                              <a class="right carousel5-control" href="#carousel5" role="button" data-slide="next">
                                <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
                                <span class="sr-only">Next</span>
                              </a>
                            </div>
                        </div>
                          </body>
                        </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
