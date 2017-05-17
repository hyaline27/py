#-*- encoding=UTF-8 -*-

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/index/')
@app.route('/')
def index():
    return 'hello'

@app.route('/profile/<int:uid>/', methods=['GET', 'post'])
#指定了类型
def profile(uid):
    return render_template('profile.html', uid=uid)


@app.route('/request/')
def request_demo():
    res = request.args.get('key', 'defaultkey') + '</br>'
    for property in dir(request):
        res = res + str(property) + '<br>' + str(eval('request.' + property)) + '<br>'
    return res


if __name__ == '__main__':
    app.run(debug=True)