def test_example_1(client):
    print(client)
    response = client.get("/api")
    assert response.status_code == 200
