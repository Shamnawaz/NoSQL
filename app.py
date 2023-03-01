from flask import Flask, render_template
import pymongo
from pymongo import MongoClient
import json
import pandas as pd 
import db
from db import test

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>FERFERFERFER</p>"



@app.route('/index')
def index():
    test()