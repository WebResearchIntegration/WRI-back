#!/usr/bin/env python
# -*- coding: utf-8 -*-
from neo4jrestclient.client import GraphDatabase
import json
from config.graphDB import ConnectDatabase
from models.article import Article

gdb = ConnectDatabase().gdb

# This is the Controller class file of articles

class ArticlesController():

    def get_one_article(self, articleId):
        article = gdb.nodes.get(articleId)
        print article.id
        print type(article)
        return article
    
    def get_all(self):
        articles = (gdb.labels.get('Article')).all()
        articles_to_return = []

        for article in articles:
            print json.dumps(dict(article.items()))
            articles_to_return.append((article.properties))
        return articles_to_return
    
    def create_article(self, data):
        return ""

    def update_article(self, articleId, data):
        return ""

    def delete_article(self, articleId):
        return ""
    

        
    

