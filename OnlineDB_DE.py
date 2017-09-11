import sys
import pymongo
import os
import json
from pathlib import Path


# Standard URI format: mongodb://[dbuser:dbpassword@]host:port/dbname

uri = 'mongodb://vipul:vipul@ds135812.mlab.com:35812/news'

def main(args):

    client = pymongo.MongoClient(uri)
    db = client.get_default_database()
    newsinfo= db['newsdata']
    output=[]
    for doc in newsinfo.find():
        output.append({'url':doc['url'],'All_text' :doc['All_text']})
    client.close() 


if __name__ == '__main__':
    main(sys.argv[1:])