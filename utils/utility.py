from utils.load_from_file import products

def get_product_name(product_id, products):
    #Returns product name from product_id
    for product in products:
        if product["productId"] == product_id:
            return product["productName"]

def get_product(product_id, products):
    #Returns product details(object) from product_id
    for product in products:
        if product["productId"] == product_id:
            return product

def data_n_days(data, num_days):
    #Returns transaction records from the last
    last_n_days_data = data[-num_days:]
    return last_n_days_data

def find_by(find_by_attribute, dataset):

    unique_data = set() #unique set of products
    result_list = []    #final transaction list with unique find by item

    for each_data in dataset:
        #Updates transaction record with product details(object)
        if "productId" in each_data:
            each_data.update(get_product(each_data["productId"], products))
        else:
            #returns error response if productId doesn't exist for a transaction
            return {"message": f"productId doesn't exist for transaction id {dataset['transactionId']}"}, 500

        #if product is present in the set of unique product then update its totalAmount
        if each_data[find_by_attribute] in unique_data:
            for each_row in result_list:
                if each_row[find_by_attribute] == each_data[find_by_attribute]:
                    each_row["totalAmount"] += int(each_data["transactionAmount"])
        else:
            #else create new entry of dictionary for that product
            new_entry = {find_by_attribute: each_data[find_by_attribute], \
                         "totalAmount": int(each_data["transactionAmount"])}
            unique_data.add(each_data[find_by_attribute]) #adds a new product to set
            result_list.append(new_entry)
    return result_list
