#დავალება1
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>/<int:age>')
def user(name, age):
    subjects = ['Math', 'Science', 'IT', 'English']
    return render_template('user.html', name=name, age=age, subjects=subjects)

if __name__ == '__main__':
    app.run(debug=True)
