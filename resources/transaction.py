from flask_restful import Resource

from utils.load_from_file import products, transactions
from utils.utility import get_product_name

class Transaction(Resource):
    """
        API class returns a particular transaction from its transaction id
    """
    def get(self, transaction_id):
        try:
            for transaction in transactions:
                if transaction["transactionId"] == transaction_id:
                    query_transaction = transaction
                    product_name = get_product_name(query_transaction["productId"], products)
                    query_transaction.update({"productName": product_name})
                    query_transaction.pop("productId")
                    return {"transaction": query_transaction}, 200
            return {"message": f"Transaction with id {transaction_id} not found", "error": False}, 404        
        except Exception as e:
            print(str(e))
            return {"message": "Error while querying transaction", "error": True}, 500
        

