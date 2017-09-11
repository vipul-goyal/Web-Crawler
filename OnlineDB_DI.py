import sys
import pymongo
import json
import os
from pathlib import Path

# Standard URI format: mongodb://[dbuser:dbpassword@]host:port/dbname

uri = 'mongodb://vipul:vipul@ds135812.mlab.com:35812/news'

def main(args):

    client = pymongo.MongoClient(uri)
    db = client.get_default_database()
    db.drop_collection('newsdata')
    newsinfo= db['newsdata']
    config=json.loads(open("news.json").read())
    for q in config:
        newsinfo.insert({'url' :q['url'],'All_text' : q['All_text']})
    my_file = Path("news.json")
    if my_file.exists():
        os.remove('news.json')
    client.close()    
if __name__ == '__main__':
    main(sys.argv[1:])