#!/usr/bin/env python
# -*- coding: utf-8 -*-
from neo4jrestclient.client import GraphDatabase
import json
from config.graphDB import ConnectDatabase
from models.article import Article

# Connect current database with controller
gdb = ConnectDatabase().gdb

# This is the Controller class file of articles

class ArticlesController():

    def get_one_article(self, articleId):
        node = gdb.nodes.get(articleId)
        article = node.properties
        article['id'] = node.id
        return article
    
    def get_all(self):
        articles = (gdb.labels.get('Article')).all()
        articles_to_return = []

        for article in articles:
            print json.dumps(dict(article.items()))
            tmp_article = article.properties
            tmp_article['id'] = article.id
            articles_to_return.append(tmp_article)
        return articles_to_return
    
    def create_article(self, data):
        print data
        return ""

    def update_article(self, articleId, data):
        return ""

    def delete_article(self, articleId):
        node = gdb.nodes.get(articleId)
        article_deleted = node.properties
        node.delete()
        return article_deleted
    

        
    

