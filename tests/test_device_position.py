import pytest
from app import schemas

def test_get_one_device_does_not_exist(client):
    response = client.get(f"/position/999999")
    assert response.status_code == 404

@pytest.mark.parametrize("device_ref_id, latitude, longitude", [
    (1, 50.1, -40.2),
    (3, 50.1, -40.2),
    (7, 50.1, -40.2),
    (9, 50.1, -40.2),
])
def test_create_position(client, device_ref_id, latitude, longitude, test_device):
    response_position = client.post(
        "/position/", json=[{"device_id": device_ref_id, "latitude": latitude, "longitude": longitude}])

    created_position = response_position.json()[0]

    # import pdb; pdb.set_trace()

    assert response_position.status_code == 201
    assert created_position['device_id'] == device_ref_id
    assert created_position['latitude'] == latitude
    assert created_position['longitude'] == longitude
