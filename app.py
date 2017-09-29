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

if __name__ == "__main__":
    app.run()
