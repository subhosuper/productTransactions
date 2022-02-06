from flask_restful import Resource

from utils.load_from_file import products, transactions
from utils.utility import get_product_name, find_by, data_n_days

class FindByProducts(Resource):
    """
        API class finds by product from the transaction records
    """
    def get(self, last_n_days):
        find_by_attribute = "productName"
        try:
            data = transactions
            new_data = data_n_days(data, last_n_days)
            result_data = find_by(find_by_attribute, new_data)
            return {"summary": result_data}, 200
        except Exception as e:
            print(str(e))
            return {"message": "Error with querying products", "error": True}, 500


class FindByCity(Resource):
    """
        API class finds by city from the transaction records
    """
    def get(self, last_n_days):
        find_by_attribute = "productManufacturingCity"
        try:
            data = transactions
            new_data = data_n_days(data, last_n_days)
            result_data = find_by(find_by_attribute, new_data)
            return {"summary": result_data}, 200
        except Exception as e:
            print(str(e))
            return {"message": "Error with querying products", "error": True}, 500
