#------------------------------------------------- #
# Title: Lab7-1
# Description: A simple example of storing data in a binary file
# ChangeLog: (Who, When, What)
# NeetuUpadhyay,05.31.2023,Created Script
# ------------------------------------------------- #
import pickle

# Data -------------------------------------------- #
strFileName = 'AppData.dat'
lstCustomer = []

# Processing -------------------------------------- #
def save_data_to_file(file_name, list_of_data):
    with open(file_name, 'wb') as file:
        pickle.dump(list_of_data, file)

def read_data_from_file(file_name):
    with open(file_name, 'rb') as file:
        data = pickle.load(file)
    return data

# Presentation ------------------------------------ #
customer_id = input("Enter customer ID: ")
customer_name = input("Enter customer name: ")
customer = {'ID': customer_id, 'Name': customer_name}
lstCustomer.append(customer)

save_data_to_file(strFileName, lstCustomer)
print("Data saved to file:", strFileName)

new_list = read_data_from_file(strFileName)
print("Data read from file:", strFileName)
for customer in new_list:
    print("ID:", customer['ID'])
    print("Name:", customer['Name'])

