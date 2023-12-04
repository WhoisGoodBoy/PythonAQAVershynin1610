from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import bson



connection_str = 'mongodb+srv://Primat:d2z76ctb@cluster0.v1o4bs7.mongodb.net/'

client = MongoClient(connection_str, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print('we`re connected')
except Exception as e:
    print(e)


weather_db = client.get_database('sample_weatherdata')
data_collection = weather_db.get_collection('data')
print(data_collection)

collection_of_datasamples = data_collection.find_raw_batches()
#for datasample in collection_of_datasamples:
#    print(bson.decode_all(datasample))
result = data_collection.find_one(filter={'sections': ['AG1', 'GF1', 'MD1', 'SA1', 'UA1']})
print(result)
value_to_insert = data_collection.insert_one({'Detroytshina':'Kyivan region'})
print(value_to_insert)
check_if_value_inserted = data_collection.find_one(value_to_insert.inserted_id)
print(check_if_value_inserted)