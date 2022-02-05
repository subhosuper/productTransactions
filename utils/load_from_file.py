import csv, os
from operator import itemgetter
from path import product_dir_path, transaction_dir_path

list_transaction_files = os.listdir(transaction_dir_path)
products = []
transactions = []

def read_row(file_path, file_name, store_list):
    """
        Reads each row from file provided through argument and
        stores in a list reference provided through argument
        Output: returns list of dictionaries, each dictionary belongs to each row in file
    """
    try:
        with open(file_path + f"/{file_name}", 'r') as file:
            file_reader = csv.reader(file)
            headers = next(file_reader)
            for row in file_reader:
                store_list.append(dict(zip(headers, row)))
    except Exception as e:
        print("Error in reading file", str(e))

def load_products():
    """
        Loads products and stores in a list for further use
    """
    try:
        read_row(product_dir_path, "ProductReference.csv", products)
    except Exception as e:
        print("Error loading products: ", str(e))
        return {"message": "Error while loading products", "error": True}, 500

def load_transactions():
    """
        Loads transaction and stores in a list for further use
    """
    try:
        for transaction_file in list_transaction_files:
            read_row(transaction_dir_path, transaction_file, transactions)
        # transactions.sort(key=itemgetter("transactionID"))
    except Exception as e:
        print("Error loading transactions: ", str(e))
        return {"message": "Error while loading transactions", "error": True}, 500


