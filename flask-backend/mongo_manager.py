
import pymongo
import json
from pymongo import MongoClient
from pymongo.errors import AutoReconnect, ConnectionFailure
import bson
from bson.objectid import ObjectId
import configparser
import os
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.


DB_USER = os.environ.get('DB_USER') 
DB_PASS = os.environ.get('DB_PASS') 
DB_NAME = os.environ.get('DATABASE')
IP = os.environ.get('DB_HOST')
PORT = os.environ.get('DB_PORT')

class MongoDBmanager:
    def __init__(self, collection):
        # t_mongo_init = time.time()
        # self.usr = user
        # self.password = password
        self.db = DB_NAME
        self.collection = collection
        # Connect to the DB
        try:
            self.client = MongoClient(f'mongodb://{DB_USER}:{DB_PASS}@{IP}:{PORT}/{DB_NAME}')
            # self.client = MongoClient("mongodb://localhost:27017/")
            print(f'Connected to Mongodb @ mongodb://{DB_USER}:{DB_PASS}@{IP}:{PORT}/{DB_NAME}')
        except (AutoReconnect, ConnectionFailure) as e:
            print(e)
            print(f'CONNECTION_ERROR to mongodb://{DB_USER}:{DB_PASS}@{IP}:{PORT}/{DB_NAME}')
            raise Exception("CONNECTION_ERROR")


    def get_one_document(self, query):
        _DB = self.client[self.db]
        collection = _DB[self.collection]
        res = collection.find_one(query)
        if res is not None:           
            return res
        else:
            # mongodb_logger.debug('get_one_document(): READ_ERROR')
            print(('get_one_document(): READ_ERROR'))
            raise Exception("READ_ERROR")

    def get_documents(self, query):
        _DB = self.client[self.db]
        collection = _DB[self.collection]
        ret = collection.find(query)
        return ret

    def aggregate(self, query):
        _DB = self.client[self.db]
        collection = _DB[self.collection]
        ret = collection.aggregate(query)
        return ret
    
    def create(self, query):
        _DB = self.client[self.db]
        collection = _DB[self.collection]
        ret = collection.insert_one(query)
        return ret.inserted_id

    def bulkWrite(self, query):
        if query!=None and len(query)>0:
            _DB = self.client[self.db]

            collection = _DB[self.collection]
            ret = collection.bulk_write(query)
            return ret
        else:
            print("No query to bulkwrite")

    def find_one_update(self, find_query, update_query, array_filters):
        _DB = self.client[self.db]
        collection = _DB[self.collection]
        try:
            collection.update_one(find_query, {'$set': update_query}, array_filters = array_filters)
        except bson.errors.InvalidId:
            print('find_one_update(): UNSUPPORTED ID')
            raise Exception("UNSUPPORTED_ID")

    def find_one_update_inc(self, find_query, update_query, array_filters):
        _DB = self.client[self.db]
        collection = _DB[self.collection]
        try:
            collection.update_one(find_query, {'$inc': update_query}, array_filters = array_filters)
        except bson.errors.InvalidId:
            print('find_one_update_inc(): UNSUPPORTED ID')
            raise Exception("UNSUPPORTED_ID")
    
    