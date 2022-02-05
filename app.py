from json import load
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_restful import Api

from utils.load_from_file import load_products, load_transactions
from resources.transaction import Transaction
from resources.find_by import FindByProducts, FindByCity

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

api = Api(app)

CORS(app, origins="*", expose_headers='Content-Disposition', 
    allow_headers=["Content-Type", "Accept", "Authorization", "Access-Control-Allow-Credentials",\
    "Access-Control-Allow-Origin", "Cache-Control"],\
    supports_credentials=True
    )

load_products()
load_transactions()

api.add_resource(Transaction, "/assignment/transaction/<string:transaction_id>")
api.add_resource(FindByProducts, "/assignment/transactionSummaryByProducts/<int:last_n_days>")
api.add_resource(FindByCity, "/assignment/transactionSummaryByManufacturingCity/<int:last_n_days>")


if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')