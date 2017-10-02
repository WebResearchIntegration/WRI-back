#!/usr/bin/env python
# -*- coding: utf-8 -*-
from neo4jrestclient.client import GraphDatabase
from config.graphDB import ConnectDatabase

gdb = ConnectDatabase().gdb

# This is the class file of articles models

class Article():
    def __init__(self, title, year, user_score, authors,  conference = "", journal = "", keywords = [], references = [], notes = [], saved = False, printed = False, read = False):
        self.title = title
        self.conference = conference
        self.journal = journal
        self.year = year
        self.user_score = user_score
        self.authors = authors
        self.keywords = keywords
        self.references = references
        self.notes = notes
        self.saved = saved
        self.printed = printed
        self.read = read

        # Node Element properties
        self.node = None

    def save(self):
        if self.node is None:
            self.node = gdb.nodes.create(title=self.title)
        else:
            self.node = gdb.nodes.create(title=self.title)
            self.node.labels.add('Article')    
        
        
    

