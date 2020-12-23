from flask import Flask,request,json,Response
from pymongo import MongoClient
import dns.resolver
import ssl
'''
Instantiate an instance of this class whenever you need to make queries progromatically. Its methods
will handle CRUD requests
'''
class DBAPI:
    def __init__(self,data):
        
        #the local host address is the port exposed within our container that contains the MongoDB
        self.client = MongoClient("mongodb+srv://testinAdmin:test@cluster0.hq4ti.mongodb.net/test",ssl_cert_reqs=ssl.CERT_NONE)
        #self.client = MongoClient("mongodb+srv://testinAdmin:bestfantasyplayer123@cluster0.hq4ti.mongodb.net/FantasyFootball?retryWrites=true&w=majority")
        #self.client = MongoClient("mongodb://localhost:27017/")  
        #self.client = MongoClient("mongodb://localhost:5000/")  
        database = data['database']
        collection = data['collection']
        cursor = self.client[database]
        self.collection = cursor[collection]
        self.data = data

    def read(self):
        documents = self.collection.find()
        output = [{item: data[item] for item in data if item != '_id'} for data in documents]
        return output

    def write(self, data):
        new_document = data['Document']
        response = self.collection.insert_one(new_document)
        output = {'Status': 'Successfully Inserted',
                    'Document_ID': str(response.inserted_id)}
        return output

    def update(self):
        filt = self.data['Filter']
        updated_data = {"$set": self.data['DataToBeUpdated']}
        response = self.collection.update_one(filt, updated_data)
        output = {'Status': 'Successfully Updated' if response.modified_count > 0 else "Nothing was updated."}
        return output

    def delete(self, data):
        filt = data['Document']
        response = self.collection.delete_one(filt)
        output = {'Status': 'Successfully Deleted' if response.deleted_count > 0 else "Document not found."}
        return output
    
    
