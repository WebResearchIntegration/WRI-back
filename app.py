#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for, jsonify, Markup
import json, os, numpy, markdown
import dblp, pandas as pd
from neo4j.v1 import GraphDatabase, basic_auth

app = Flask(__name__)


@app.route('/')
def index():
    return "Welcome! You are now Connected to the WRI system."

#[ARTICLES CRUD]

@app.route('/articles', method = ['GET'])
def app_root():
    return "Welcome! You are now Connected to the WRI system."

@app.route('/articles/<int:articleid>', method = ['GET'])
def get_all_articles():
    return "You just load all articles"

@app.route('/articles', method = ['POST'])
def add_article():
    return "You just post an article"

@app.route('/articles/<int:articleid>', method = ['PUT'])
def update_one_article():
    return "You just update one article"

@app.route('/articles/<int:articleid>', method = ['DELETE'])
def delete_article():
    return "ATTENTION, You just delete one article"

# [END ARTICLES CRUD]

#[RUN APP]
if __name__ == "__main__":
    app.run()
