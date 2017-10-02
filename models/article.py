#!/usr/bin/env python
# -*- coding: utf-8 -*-
from neo4jrestclient.client import GraphDatabase
from config.graphDB import ConnectDatabase

gdb = ConnectDatabase().gdb

# This is the class file of articles models

class Article():
    def __init__(self, title, year, user_score, authors, node = None,  conference = "", journal = "", keywords = [], references = [], notes = [], saved = False, printed = False, read = False):
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
        self.node = node


    # TODO:: Finish to put values inside 
    def save(self):
        if self.node is None:
            self.node = gdb.nodes.create(title=self.title, conference=self.conference, journal=self.journal, year=self.year, user_score=self.user_score, authors=self.authors, keywords=self.keywords)
            self.node.labels.add('Article')
        else:
            self.node.set('title', self.title)
            self.node.set('conference', self.conference)
            self.node.set('journal', self.journal)
            self.node.set('year', self.year)
            self.node.set('user_score', self.user_score)
            self.node.set('authors', self.authors)
            self.node.set('keywords', self.keywords)
            self.node.set('references', self.references)
            self.node.set('notes', self.notes)
            self.node.set('saved', self.saved)
            self.node.set('printed', self.printed)
            self.node.set('read', self.read)
        
        
    

