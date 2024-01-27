from fastapi.testclient import TestClient


def test_get_data_from_api(client: TestClient):
    response = client.get("/pik/get_data")

    print(response.json())

    assert response.status_code == 200