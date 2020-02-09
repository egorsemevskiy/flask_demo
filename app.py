from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from _datetime import datetime

app = Flask(__name__, static_folder='./static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(20), nullable=False, default="N/A")
    data_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'Blog Post {str(self.id)}'


all_posts = [
    {
        'title': 'Post 1',
        'content': 'This is content of post 1',
        'author': 'Egor',
    },
    {
        'title': 'Post 2',
        'content': 'This is content of post 2',
        'author': 'Egor',
    },
    {
        'title': 'Post 3',
        'content': 'This is content of post 3',
    }
]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/posts')
def posts():
    return render_template('posts.html', posts=all_posts)


@app.route('/home/<string:name>/posts/<int:id>')
def hello(name, id):
    return f"Hello, {name}, your id is {str(id)}"


@app.route('/onlyget', methods=['GET'])
def get_req():
    return 'you can only get this webpage'


if __name__ == '__main__':
    app.run(debug=True)

