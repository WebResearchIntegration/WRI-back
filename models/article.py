#!/usr/bin/env python
# -*- coding: utf-8 -*-
from neo4jrestclient.client import GraphDatabase
from config.graphDB import ConnectDatabase

gdb = ConnectDatabase().gdb

# This is the class file of articles models

class Article():
    def __init__(self, article):
        self.title = article.title
        self.conference = article.conference
        self.journal = article.journal
        self.year = article.year
        self.user_score = article.user_score
        self.authors = article.authors
        self.keywords = article.keywords
        self.references = article.references
        self.notes = article.title
        self.saved = article.saved
        self.printed = article.printed
        self.read = article.read

        # Node Element properties
        self.node = gdb.nodes.create(title=self.title)
        self.node.labels.add('Article')
        

