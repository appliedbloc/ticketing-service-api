def test_example_1(client):
    response = client.get("/clients/")
    assert response.status_code == 200


def test_example_2():
    assert True == True


def test_example_3():
    assert False == True
