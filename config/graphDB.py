#!/usr/bin/env python
# -*- coding: utf-8 -*-

from neo4jrestclient.client import GraphDatabase

class ConnectDatabase:
    def __init__(self):
        self.gdb = GraphDatabase("http://localhost:7474", username="neo4j", password="root")
