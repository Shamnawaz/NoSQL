import pymongo 
from pymongo import MongoClient
import json
import pandas as pd

def test():

    client = MongoClient('mongodb+srv://Sham:LwNIklUIvNYefZO5@cluster0.kxvrnx9.mongodb.net/test', 27017)
    db = client['Euro2020']
    for collection in db.list_collection_names():

        print(collection)
        
    return db.list_collection_names()