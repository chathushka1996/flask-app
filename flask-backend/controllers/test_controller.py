"""
 * @class TestController
 * @description This controller use for Handle the request related to the test insert and test coordinate retrieval
 * @author chathushka

"""
import os
import pathlib
import time
from flask import request
from logger import get_debug_logger
from services.test_manager import TestManager

if not os.path.exists(pathlib.Path.joinpath(pathlib.Path(__file__).parent.resolve(), '../logs')):
    os.makedirs(pathlib.Path.joinpath(
        pathlib.Path(__file__).parent.resolve(), '../logs'))

logger = get_debug_logger('test_controller', pathlib.Path.joinpath(
    pathlib.Path(__file__).parent.resolve(), '../logs/server.log'))


class TestController:
  def __init__(self, app):
        logger.debug('Initiate Test Controller')
        app.add_url_rule('/api/test/insert/ipca', 'insert test coordinates', self.insert_test_coordinates, methods=['POST'])
        app.add_url_rule('/api/test/sample/coordinates', 'get test sample coordinates', self.get_test_sample_coordinates, methods=['POST'])
        self.test_manager = TestManager()


  """
  * Use for insert the test coordinates for query
  * aggregateQuery = json.loads(data.get("aggregateQuery")) - match query
  * objectType = data.get("objectType") - object type for filter
  * testId = data.get("testId") - testId for save ipca data
  * isCronJobDeletable = data.get("isCronJobDeletable") - deletable or not
  * return {"testId": test_id}
  """
  def insert_test_coordinates(self):
    data = request.json
    logger.debug(f'Insert test coordinates, request data: {data}')
    return self.test_manager.insert_test_coordinates(data)
  
  """
  * Use for retrieve the test coordinates for polygon selection
  * group_id = data.get('testId') - testId for retrieve ipca data
  * coordinates = data.get('coordinates') - polygon for filter
  * return sample_response_list
  """
  def get_test_sample_coordinates(self):
    data = request.json
    group_id = data.get('testId')
    coordinates = data.get('coordinates')
    # team_id = data.get('teamId')
    logger.debug(f'Get test sample coordinates, request data: {data}')
    return self.test_manager.get_test_sample_coordinates(group_id, coordinates)
    


    

    