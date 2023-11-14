"""
 * @class MilvusManager
 * @description MilvusManager use for connect and curd operation with milvus vector database 
 * @author chathushka

"""

import os
import pathlib
from pymilvus import (
    connections,
    utility,
    FieldSchema, CollectionSchema, DataType,
    Collection,
    db
)
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.



VECTOR_DB_HOST = os.environ.get('VECTOR_DB_HOST')
VECTOR_DB_PORT = os.environ.get('VECTOR_DB_PORT')
VECTOR_DB_USER = os.environ.get('VECTOR_DB_USER')
VECTOR_DB_PASS = os.environ.get('VECTOR_DB_PASS')
VECTOR_DB_SSL = False
VECTOR_DB_NAME = os.environ.get('VECTOR_DB_NAME')

from logger import get_debug_logger

if not os.path.exists(pathlib.Path.joinpath(pathlib.Path(__file__).parent.resolve(), '../logs')):
    os.makedirs(pathlib.Path.joinpath(
        pathlib.Path(__file__).parent.resolve(), '../logs'))

logger = get_debug_logger('milvus_manager', pathlib.Path.joinpath(
    pathlib.Path(__file__).parent.resolve(), '../logs/server.log'))

class MilvusManager:
  def __init__(self, collection):
      self.connect_to_milvus(VECTOR_DB_NAME)
      self.collection = Collection(collection)

  """
  Use to connect with milvus database
  """
  def connect_to_milvus(self, db_name="default"):
      logger.debug(f"connect to milvus\n")
      connections.connect(
        host=VECTOR_DB_HOST, 
        port=VECTOR_DB_PORT, 
        user=VECTOR_DB_USER, 
        password=VECTOR_DB_PASS, 
        db_name=db_name
      )

  """
  Use to search similar vectors from milvus database
  """
  def search(
        self, 
        vectors_to_search, 
        field="embeddings", 
        search_params={
        "metric_type": "IP",
        "params": {"nprobe": 10, "radius": 0.5, "range_filter" : 10}
        },
        output_fields=["uniqueName"],
        expr="",
        limit=100,
        offset=0,
    ):
    result = self.collection.search(
      vectors_to_search, 
      field, 
      search_params, 
      limit=limit, 
      offset=offset,
      output_fields=output_fields,
      expr = expr
    )

    return_result = []
    for raw_result in result:
      for result in raw_result:
        id = result.id
        distance = result.distance
        entity = result.entity._row_data
        obj = {
           "id": id,
           "distance": distance,
           "entity": entity
        }
        return_result.append(obj)
    return return_result
  

  """
  Use to query vector data from milvus database
  """
  def query(
        self, 
        expr, 
        output_fields=["uniqueName"],
        limit=100,
        offset=0,
    ):
    result = self.collection.query(
      expr=expr, 
      output_fields=output_fields,
      limit=limit,
      offset=offset,
      consistency_level="Strong"
      )
    return result