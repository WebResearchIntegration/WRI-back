#!/usr/bin/env python
# -*- coding: utf-8 -*-

from controllers.articles_controller import ArticlesController
from flask import Flask, render_template, request, redirect, url_for, jsonify, Markup
import json, os, numpy, markdown
import dblp, pandas as pd
from config.graphDB import ConnectDatabase
from neo4jrestclient.client import GraphDatabase

gdb = ConnectDatabase().gdb

app = Flask(__name__)

@app.route('/')
def index():
    return "OK"

#[ARTICLES CRUD]

@app.route('/articles', methods = ['GET'])
def get_all_articles():
    articles = { "articles": ArticlesController().get_all() }
    print articles
    return jsonify(articles)

@app.route('/articles/<int:articleid>', methods = ['GET'])
def get_one_article(articleid):
    article = ArticlesController().get_one_article(articleid)
    print article
    return "You just load one article"

@app.route('/articles', methods = ['POST'])
def add_article():
    article = ArticlesController().create_article(request.data)
    print article
    return "You just post an article"

@app.route('/articles/<int:articleid>', methods = ['PUT'])
def update_one_article(articleid):
    article = ArticlesController().update_article(articleid, request.data)
    print article
    return "You just update one article"

@app.route('/articles/<int:articleid>', methods = ['DELETE'])
def delete_article(articleid):
    article = ArticlesController().delete_article(articleid)
    return "ATTENTION, You just delete one article"

# [END ARTICLES CRUD]

#[RUN APP]
if __name__ == "__main__":
    app.run()
