from flask import request, jsonify
from mongo_manager import MongoDBmanager

Products_DB = MongoDBmanager("Products")

class Products:


    @staticmethod
    def add_product():
        
        # Access query parameters
        name = request.args.get('name')
        print(request)
        print(name, "xxxxx")
        category = request.args.get('category')
        # Perform necessary operations using the query parameters

        # Access request body data
        data = request.json
        response = Products_DB.create(data)

        print(data)

        # Extract the necessary data from the InsertOneResult object
        response_data = {
            'id': str(response),
            'name': name,
            'category': category,
            'message': 'Product added successfully'
        }

        return jsonify(response_data)