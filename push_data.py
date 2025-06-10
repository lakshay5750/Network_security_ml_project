import os
import sys
import json
import pymongo
from dotenv import load_dotenv
load_dotenv()
MONGO_DB_URL=os.getenv('MONGO_DB_URL')
print(MONGO_DB_URL)
import certifi
ca=certifi.where()
import pandas as pd
import numpy as np
from networksecurity.exception.exception import CustomException
from networksecurity.logging.logger import logging
class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise CustomException(e,sys)
    def cv_to_json_convertor(self,file_path):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records=list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise CustomException(e,sys)
    def insert_to_mongo(self,records,database,collection):
        try:
            self.database=database
            self.records=records
            self.collection=collection
            self.mongo_client=pymongo.MongoClient(MONGO_DB_URL)
            self.database=self.mongo_client[self.database]
            self.collection=self.database[self.collection]
            self.collection.insert_many(self.records)
            return len(self.records)
        except Exception as e:
            raise CustomException(e,sys)

if __name__=='__main__':
    FILE_PATH='Network_Data\phisingData.csv'
    Database='LakshayVarshney'
    Collection='NetworkData'
    networkobj=NetworkDataExtract()
    records=networkobj.cv_to_json_convertor(FILE_PATH)
    no_of_records= networkobj.insert_to_mongo(records=records,database=Database,collection=Collection)
    print(records)
    print(no_of_records)

