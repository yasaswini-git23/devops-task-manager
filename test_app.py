import pytest
from app import app, tasks


@pytest.fixture
def client():
    tasks.clear()
    with app.test_client() as client:
        yield client


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"DevOps Task Manager" in response.data


def test_add_task(client):
    response = client.post("/tasks", json={"title": "Learn Docker"})
    assert response.status_code == 201
    assert response.json["title"] == "Learn Docker"


def test_complete_task(client):
    response = client.post("/tasks", json={"title": "Learn Terraform"})
    task_id = response.json["id"]
    response = client.post(f"/tasks/{task_id}/complete")
    assert response.status_code == 302
    assert tasks[0]["completed"] is True


def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"
