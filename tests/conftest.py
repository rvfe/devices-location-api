from app.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base, get_db
from fastapi.testclient import TestClient
import pytest
from app.main import app
from app import models



SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)


@pytest.fixture()
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture()
def client(session):
    def override_get_db():

        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)

@pytest.fixture
def test_device(session):
    device_data = [{
        "device_id": 1
    },{
        "device_id": 3
    },{
        "device_id": 7
    },{
        "device_id": 9
    }]

    def create_device_model(device):
        return models.Device(**device)

    device_map = map(create_device_model, device_data)
    devices = list(device_map)

    session.add_all(devices)
    session.commit()

    devices = session.query(models.Device).all()

    devices_id_list = [result.id for result in devices]

    return devices_id_list
    
@pytest.fixture
def test_position(session):
    position_data = [{
        "device_ref_id": 1,
        "latitude": -50.12,
        "longitude": -50.12
    }, {
        "device_ref_id": 1,
        "latitude": -54.12,
        "longitude": -50.12
    },
        {
        "device_ref_id": 2,
        "latitude": -54.12,
        "longitude": -50.12
    }, {
        "device_ref_id": 2,
        "latitude": -54.12,
        "longitude": -50.12
    }]

    def create_position_model(position):
        return models.Position(**position)

    position_map = map(create_position_model, position_data)
    position = list(position_map)

    session.add_all(position)
    # session.add_all([models.Post(title="first title", content="first content", owner_id=test_user['id']),
    #                 models.Post(title="2nd title", content="2nd content", owner_id=test_user['id']), models.Post(title="3rd title", content="3rd content", owner_id=test_user['id'])])
    session.commit()

    position = session.query(models.Position).all()
    return position

