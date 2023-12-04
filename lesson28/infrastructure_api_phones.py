import requests
import json



url = 'https://api.restful-api.dev/objects'


class Dog:
    def __init__(self, data):
        self.id = data['id']
        self.data = data
        self.creation_date = data.pop('createdAt')


    def change_name(self, new_name):
        self.data['name'] = new_name

    def change_breed(self, new_breed):
        self.data['data']['breed'] = new_breed

    def change_size(self, new_size):
        self.data['data']['size'] = new_size




def get_an_object(object_id):
    return requests.get(f'{url}/{object_id}')


def get_an_filtred_list_of_objects(list_of_objects:list):
    ids=''
    for object_id in list_of_objects:
        if object_id != list_of_objects[-1]:
            ids += f'id={object_id}&'
        else:
            ids += f'id={object_id}'
    final_string = f'{url}?{ids}'
    print(final_string)
    return requests.get(final_string)

def create_an_object():
    headers = {"content-type":"application/json"}
    object_body = json.dumps({"name": "Apple MacBook Pro 16", "data": {
      "year": 2019,
      "price": 1849.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB"}})
    response = requests.post(url, data=object_body,headers=headers)
    return response

def create_a_dog():
    headers = {"content-type":"application/json"}
    object_body = json.dumps({"name": "dog1", "data":{"size": "large", "breed": "good boy"}})
    response = requests.post(url, data=object_body,headers=headers)
    return response




def update_an_object(object_id, changed_dict):
    headers = {"content-type":"application/json"}
    updated_object = json.dumps(changed_dict)
    return requests.put(f'{url}/{object_id}', data=updated_object,headers=headers)


def patch_an_object(object_id, changed_dict):
    headers = {"content-type": "application/json"}
    updated_object = json.dumps(changed_dict)
    return requests.patch(f'{url}/{object_id}', data=updated_object, headers=headers)

def create_parametrised_dog_classified(data):
    return Dog(data=data)

def delete_an_object(object_id):
    return requests.delete(f'{url}/{object_id}')