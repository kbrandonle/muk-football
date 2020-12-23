from pymongo import MongoClient
from flask import Flask,request,json,Response
from DBAPI import DBAPI
import dns.resolver
import ssl
def main():
    data = {
        "database": "FantasyFootball",
        "collection": "Users",
    }
    mongo_obj = DBAPI(data)
    print(json.dumps(mongo_obj.read(), indent=4))
if __name__=='__main__':
    main()