def test_example_1(client):
    print(client)
    response = client.get("/api")
    assert response.status_code == 200


def test_example_2():
    assert True == True


def test_example_3():
    assert False == True
