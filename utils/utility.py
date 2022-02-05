from utils.load_from_file import products

def get_product_name(product_id, products):
    for product in products:
        if product["productId"] == product_id:
            return product["productName"]

def get_product(product_id, products):
    for product in products:
        if product["productId"] == product_id:
            return product

def data_n_days(data, num_days):
    last_n_days_data = data[-num_days:]
    return last_n_days_data

def find_by(find_by_attribute, dataset):
    unique_data = set()
    result_list = []

    for each_data in dataset:
        if "productId" in each_data:
            # print(get_product(each_data["productId"], products))
            each_data.update(get_product(each_data["productId"], products))
            # print(each_data)
            
        if each_data[find_by_attribute] in unique_data:
            for each in result_list:
                # print(each)
                if each[find_by_attribute] == each_data[find_by_attribute]:
                    each["totalAmount"] += int(each_data["transactionAmount"])
        else:
            new_entry = {find_by_attribute: each_data[find_by_attribute], \
                         "totalAmount": int(each_data["transactionAmount"])}
            unique_data.add(each_data[find_by_attribute])
            result_list.append(new_entry)
    return result_list
