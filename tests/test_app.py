import pytest
from app import app, STUDENTS


@pytest.fixture
def client():
    app.config["TESTING"] = True
    STUDENTS.clear()
    with app.test_client() as c:
        yield c


def test_home_page_loads(client):
    r = client.get("/")
    assert r.status_code == 200
    assert b"Student Registration App" in r.data


def test_register_student(client):
    client.post("/", data={"name": "Mayur", "roll": "DS03"})
    assert client.get("/api/students").get_json() == [{"name": "Mayur", "roll": "DS03"}]


def test_empty_form_is_ignored(client):
    client.post("/", data={"name": "", "roll": ""})
    assert client.get("/api/students").get_json() == []


def test_health_endpoint(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.get_json()["status"] == "UP"


def test_metrics_endpoint(client):
    data = client.get("/metrics").get_json()
    assert "total_requests" in data and "registered_students" in data
