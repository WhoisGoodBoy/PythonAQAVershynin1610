from lesson29.requests_last_points import CRUDWithSession


def test_get_an_object():
    session = CRUDWithSession()
    object = session.get_an_object(5)
    assert object.status_code == 200

def test_get_nonexisting_object():
    session = CRUDWithSession()
    object = session.get_nonexisting_object()

def test_try_to_auth():
    session = CRUDWithSession()
    object = session.get_issues()
    print(object.content)

def test_simple_auth():
    session = CRUDWithSession()
    responce = session.mocked_login()
    assert responce.status_code == 200


def test_simple_auth2():
    session = CRUDWithSession()
    responce = session.mocked_login2()
    assert responce.status_code == 200
