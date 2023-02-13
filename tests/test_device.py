import pytest
from app import schemas

def test_get_one_device_does_not_exist(client):
    response = client.get("/position/999999")
    assert response.status_code == 404


@pytest.mark.parametrize("device_id", [
    1,2,3
])
def test_create_device(client, device_id):
    response = client.post(
        "/device/", json=[{"device_id": device_id}])

    created_device = response.json()[0]
    assert response.status_code == 201
    assert created_device['device_id'] == device_id
    