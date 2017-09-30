#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for, jsonify, Markup
import json, os, numpy, markdown
import dblp, pandas as pd
from neo4jrestclient.client import GraphDatabase

gdb = GraphDatabase("http://localhost:7474", username="neo4j", password="root")

app = Flask(__name__)


@app.route('/')
def index():
    query = "MATCH (n) WHERE n.name ='Arthur' RETURN n"
    results = gdb.query(query, data_contents=True)
    element = { "el": results.rows }
    return jsonify(element) 

#[ARTICLES CRUD]

@app.route('/articles', methods = ['GET'])
def app_root():
    return "You just got all articles loaded."

@app.route('/articles/<int:articleid>', methods = ['GET'])
def get_all_articles(articleid):
    return "You just load one article"

@app.route('/articles', methods = ['POST'])
def add_article():
    return "You just post an article"

@app.route('/articles/<int:articleid>', methods = ['PUT'])
def update_one_article(articleid):
    return "You just update one article"

@app.route('/articles/<int:articleid>', methods = ['DELETE'])
def delete_article(articleid):
    return "ATTENTION, You just delete one article"

# [END ARTICLES CRUD]

#[RUN APP]
if __name__ == "__main__":
    app.run()
