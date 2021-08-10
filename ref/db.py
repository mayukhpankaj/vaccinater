import pymongo
from pymongo import mongo_client

cluster = mongo_client.MongoClient("mongodb+srv://<username>:<pwd>@cluster0.ncyur.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = cluster["db"]

collection = db["users"]

data = {"name":"arti","email":"artikumari2075@gmail.com","district":10}

# collection.insert_one(data)

'''adding to db '''



# result = collection.find({"district":15})

result = collection.find({})

# result = collection.find_one({})

# print(result)

for r in result:
 print(r)



docs_count = collection.count_documents({})

print(docs_count)


i=1


# Query with sort()

sorted_list = collection.find().sort('district',pymongo.ASCENDING)



print(240==int(sorted_list[i-1]['d']))

for doc in sorted_list:
    print(doc['name'])



