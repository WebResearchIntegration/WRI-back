#!/usr/bin/env python
# -*- coding: utf-8 -*-
from neo4jrestclient.client import GraphDatabase
from config.graphDB import ConnectDatabase
from models.article import Article

gdb = ConnectDatabase().gdb

# This is the Controller class file of articles

class ArticlesController():

    def get_one_article(self, articleId):
        article = gdb.nodes.get(articleId)
        print article
        return article
    
    def get_all(self):
        return ""
    
    def create_article(self, data):
        return ""

    def update_article(self, articleId, data):
        return ""

    def delete_article(self, articleId):
        return ""
    

        
    

