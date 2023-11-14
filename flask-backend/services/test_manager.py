"""
 * @class TestManager
 * @description TestManager use for calculate, insert, and retrieval
 * @author chathushka

"""
from datetime import datetime
import os
import pathlib
import numpy as np
from databases import mongo_manager
from databases import milvus_manager
from logger import get_debug_logger
from bson.objectid import ObjectId
from pymongo import MongoClient, InsertOne, UpdateOne
BATCH_SIZE = 16000
N_COMPONENTS = 2
DATE_FORMAT = "%Y-%m-%dT%H:%M:%SZ"

if not os.path.exists(pathlib.Path.joinpath(pathlib.Path(__file__).parent.resolve(), '../logs')):
    os.makedirs(pathlib.Path.joinpath(
        pathlib.Path(__file__).parent.resolve(), '../logs'))

logger = get_debug_logger('test_manager', pathlib.Path.joinpath(
    pathlib.Path(__file__).parent.resolve(), '../logs/server.log'))

class TestManager():
  def __init__(self):
    logger.debug('Initiate Test Manager')
    self.meta_data_collection = mongo_manager.MongoDBmanager("TestData")
 
  """
  use to convert ejson to json
  data - ejson_data
  return json data
  """
  def convert_ejson_to_json(self, ejson_data):
      if isinstance(ejson_data, dict):
          if "$oid" in ejson_data:
              return ObjectId(ejson_data["$oid"])
          elif "$date" in ejson_data:
              return datetime.strptime(ejson_data["$date"],DATE_FORMAT)
          elif "$regex" in ejson_data:
                regex_data = ejson_data["$regex"].get('$regularExpression', {})
                pattern = regex_data.get('pattern', '')
                options = regex_data.get('options', '')
                return {"$regex": pattern, "$options": options}
          else:
              return {key: self.convert_ejson_to_json(value) for key, value in ejson_data.items()}
      elif isinstance(ejson_data, list):
          return [self.convert_ejson_to_json(item) for item in ejson_data]
      else:
          return ejson_data
      
  def get_test_sample_coordinates(group_id, coordinates):
    print(group_id, coordinates)
    return {}
  def insert_test_coordinates(data):
    return data