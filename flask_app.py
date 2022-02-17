
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, url_for, request, flash, Markup
import twitterfriend

# from datetime import datetime




app = Flask(__name__)
app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# class Article(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     intro = db.Column(db.String(300), nullable=False)
#     text = db.Column(db.Text, nullable=False)
#     date = db.Column(db.DateTime, default=datetime.utcnow)
#
#     def __repr__(self):
#         return '<Article %r>' %self.id

@app.route('/home')
def main_part():
    return render_template('index.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/map', methods=['POST', 'GET'])
def about():
    if request.method == "POST" and len(request.form['title'])>=1:
        account = request.form['title']
        try:
            current_user = twitterfriend.crearte_map(account)
            map_html = Markup(current_user._repr_html_())
            flash(map_html)
            return render_template('map.html')
        except Exception as err:
            return 'Такого користувача не існує!'
    else:
        return 'Ти ввів неправильні дані!'

@app.route('/search')
def create_article():
    return render_template('search.html')

