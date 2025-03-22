import pymongo

from pymongo import MongoClient

# establish a connection to localhost


# Connect to the MongoDB client

client = pymongo.MongoClient("mongodb://localhost:27017/")

# select a database
db = client['Shoppingsystem']

# select a collection
collection = db['Productlist']

# perform operations on the collection
result = collection.find_one({'Category': 'Juices'})
print(result)

# close the connection when you're done
#client.close()

# check whether the connection is established
if client:
    try:
        # ping the server
        client.admin.command('ping')
        print('Connection established.')
    except:
        print('Connection failed.')
else:
    print('Unable to connect to MongoDB.')

    # select the database
db = client['shoppingsystem']

# select the collection
collection = db['productlist']

# read all documents from the collection
documents = collection.find()

# print the values of the documents
for document in documents:
    print(document)