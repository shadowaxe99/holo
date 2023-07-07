```python
import pymongo

class DatabaseConnection:
    def __init__(self, db_url, db_name):
        self.client = pymongo.MongoClient(db_url)
        self.db = self.client[db_name]

    def insert_data(self, collection_name, data):
        collection = self.db[collection_name]
        collection.insert_one(data)

    def get_data(self, collection_name, query):
        collection = self.db[collection_name]
        return collection.find(query)

    def update_data(self, collection_name, query, new_data):
        collection = self.db[collection_name]
        collection.update_one(query, {"$set": new_data})

    def delete_data(self, collection_name, query):
        collection = self.db[collection_name]
        collection.delete_one(query)

db_connection = DatabaseConnection("mongodb://localhost:27017/", "Ely_Database")
```