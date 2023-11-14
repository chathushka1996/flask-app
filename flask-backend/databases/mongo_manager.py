"""
* @class MongoDBmanager
 * @description MongoDBmanager use for connect and curd operation with mongoDB database 
 * @author chathushka

"""

import pathlib
import pymongo
import json
from pymongo import MongoClient
from pymongo.errors import AutoReconnect, ConnectionFailure
import bson
import configparser
import os
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.

DB_USER = os.environ.get('DB_USER') 
DB_PASS = os.environ.get('DB_PASS') 
DB_NAME = os.environ.get('DATABASE')
IP = os.environ.get('DB_HOST')
PORT = int(os.environ.get('DB_PORT'))

from logger import get_debug_logger

if not os.path.exists(pathlib.Path.joinpath(pathlib.Path(__file__).parent.resolve(), '../logs')):
    os.makedirs(pathlib.Path.joinpath(
        pathlib.Path(__file__).parent.resolve(), '../logs'))

logger = get_debug_logger('mongo_manager', pathlib.Path.joinpath(
    pathlib.Path(__file__).parent.resolve(), '../logs/server.log'))

class MongoDBmanager:
    def __init__(self, collection):

        self.db = DB_NAME
        self.collection = collection
        # Connect to the DB
        try:
            self.client = MongoClient(f'mongodb://{DB_USER}:{DB_PASS}@{IP}:{PORT}/{DB_NAME}')
            logger.debug(f'Connected to Mongodb @ mongodb://{DB_USER}:{DB_PASS}@{IP}:{PORT}/{DB_NAME}')
        except (AutoReconnect, ConnectionFailure) as e:
            logger.debug(e)
            logger.debug(f'CONNECTION_ERROR to mongodb://{DB_USER}:{DB_PASS}@{IP}:{PORT}/{DB_NAME}')
            raise Exception("CONNECTION_ERROR")


    """
    get one document by query
    """
    def get_one_document(self, query):
        _DB = self.client[self.db]
        collection = _DB[self.collection]
        res = collection.find_one(query)
        return res

    """
    get documents by query
    """
    def get_documents(self, query):
        _DB = self.client[self.db]
        collection = _DB[self.collection]
        ret = collection.find(query)
        return ret


    """
    get documents by aggregate
    """
    def aggregate(self, query):
        _DB = self.client[self.db]
        collection = _DB[self.collection]
        ret = collection.aggregate(query)
        return ret


    """
    insert documents by bulk_write
    """
    def bulk_write(self, query):
        if query!=None and len(query)>0:
            _DB = self.client[self.db]

            collection = _DB[self.collection]
            ret = collection.bulk_write(query)
            return ret
        else:
            logger.debug("No query to bulk_write")
    

    """
    insert one document by insert_one
    """
    def insert_one(self, data):
        if data!=None:
            _DB = self.client[self.db]
            collection = _DB[self.collection]
            ret = collection.insert_one(data)
            return ret

    """
    update one document by query
    """
    def find_one_update(self, find_query, update_query, array_filters):
        _DB = self.client[self.db]
        collection = _DB[self.collection]
        try:
            collection.update_one(find_query, {'$set': update_query}, array_filters = array_filters)
        except bson.errors.InvalidId:
            logger.debug('find_one_update(): UNSUPPORTED ID')
            raise Exception("UNSUPPORTED_ID")


    """
    update one document by query
    """
    def find_one_update_inc(self, find_query, update_query, array_filters):
        _DB = self.client[self.db]
        collection = _DB[self.collection]
        try:
            collection.update_one(find_query, {'$inc': update_query}, array_filters = array_filters)
        except bson.errors.InvalidId:
            logger.debug('find_one_update_inc(): UNSUPPORTED ID')
            raise Exception("UNSUPPORTED_ID")
    
    