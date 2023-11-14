"""

"""

import os
from flask import Flask, request
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.
from controllers.test_controller import TestController

class TestFlaskApp:
    def __init__(self):
        self.app = Flask(__name__)
        TestController(self.app)

if __name__ == '__main__':
    meta_lake_flask_app = TestFlaskApp()
    meta_lake_flask_app.app.run(debug=True, host="0.0.0.0", port="3100")


