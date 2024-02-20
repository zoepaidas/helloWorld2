from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Zoe Paidas! This is my first code change!'

@app.route('/hello')
def hello():  # put application's code here
    return render_template('hello.html')

if __name__ == '__main__':
    app.run()
@app.route('/about')
def about():  # put application's code here
    return render_template('about.html')
