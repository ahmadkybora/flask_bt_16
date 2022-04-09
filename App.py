from dataclasses import field
from email.policy import default
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import datetime
from flask_cors import CORS

from requests import request

app=Flask(__name__)
CORS(app)
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(100))
    date = db.Column(db.DateTime, default = datetime.datetime.now)

    def __init__(self, title, description):
        self.title = title
        self.description = description

class ArticleSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description', 'date')


article_schema = ArticleSchema() 
articles_schema = ArticleSchema(many=True)

@app.route("/get", methods=['GET'])
def get_articles():
    articles = Articles.query.all()
    results = articles_schema.dump(articles)
    return jsonify(results)

@app.route("/get<id>/", methods=["GET"])
def show_article(id):
    article = Articles.query.get(id)
    return article_schema.jsonify(article)

@app.route("/add", methods=['POST'])
def add_article():
    title = request.json['title']
    description = request.json['description']

    articles = Articles(title, description)
    db.session.add(articles)
    db.session.commit()
    return article_schema.jsonify(articles)

@app.route("/update/<id>/", methods=["PUT"])
def update_article(id):
    article = Articles.query.get(id)

    title = request.json['title']
    description = request.json['description']

    article.title = title
    article.description = description

    db.session.commit()
    return article_schema.jsonify(article)

@app.route("/delete/<id>/", methods=['DELETE'])
def delete_article(id):
    article = Articles.query.get(id)
    db.session.delete(article)
    db.session.commit()
    return article_schema.jsonify(article) 
if __name__ == '__main__':
    app.run(debug=True)