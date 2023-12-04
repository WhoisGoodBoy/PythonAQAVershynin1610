import requests
import lesson28.infrastructure_api_phones as infra


def test_get_single_object():
    object = infra.get_an_object(5)
    assert object.status_code == 200

def test_create_single_object():
    response = infra.create_an_object()
    print(response.json())
    assert response.json()['name'] == "Apple MacBook Pro 16"

def test_creation_of_dog1():
    response = infra.create_a_dog()
    print(response.json())
    assert response.json()['data']['breed'] == 'good boy'


def test_update_mac():
    created_mac = infra.create_an_object()
    updated_mac_dict = created_mac.json()
    updated_mac_dict['data']['colour'] = 'pink'
    updated_mac_dict['data']['price'] = 900
    updated_mac_dict.pop('createdAt')
    updated_mac_response_object = infra.update_an_object(updated_mac_dict['id'], updated_mac_dict)
    print(created_mac.json())
    print(updated_mac_response_object.json())
    assert updated_mac_response_object.json()['data']['colour'] == 'pink'
    assert updated_mac_response_object.json()['data']['price'] == 900

def test_patch_dog1():
    created_dog = infra.create_a_dog()
    updated_dog_dict = {'name':'dog2'}
    updated_dog_response_object = infra.patch_an_object(created_dog.json()['id'], updated_dog_dict)
    print(created_dog.json())
    print(updated_dog_response_object.json())
    assert updated_dog_response_object.json()['name'] == 'dog2'


def test_patch_dog2():
    created_dog = infra.create_a_dog()
    updated_dog_dict = {"data":{"size": "very large", "breed": "good boy"}}
    updated_dog_response_object = infra.patch_an_object(created_dog.json()['id'], updated_dog_dict)
    print(created_dog.json())
    print(updated_dog_response_object.json())
    assert updated_dog_response_object.json()['data']['size'] == "very large"

def test_update_dog_with_class_and_parameters():
    created_dog = infra.create_a_dog()
    dog_dict = infra.create_parametrised_dog_classified(created_dog.json())
    dog_dict.change_size('very very large')
    updated_dog = infra.update_an_object(dog_dict.id, dog_dict.data)
    assert updated_dog.json()['data']['size'] == 'very very large'

def test_delete_mac():
    created_mac = infra.create_an_object()
    response_deleted_object = infra.delete_an_object(created_mac.json()['id'])
    assert response_deleted_object.json()['message'] == f"Object with id = {created_mac.json()['id']} has been deleted."


def test_get_check_filtered_list():
    filtered_list = infra.get_an_filtred_list_of_objects(['2', '4', '6'])
    print(filtered_list.json())

