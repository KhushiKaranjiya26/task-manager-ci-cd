
from fastapi.testclient import TestClient
from main import app, tasks

client = TestClient(app)


def setup_function():
    tasks.clear()


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "Welcome to Task Manager API"


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_create_task():
    response = client.post(
        "/tasks",
        json={
            "title": "Learn CI/CD",
            "description": "Build a pipeline",
            "completed": False
        }
    )

    assert response.status_code == 201
    assert response.json()["task_id"] == 1


def test_get_tasks():
    client.post(
        "/tasks",
        json={
            "title": "Learn Docker",
            "description": "Understand containers",
            "completed": False
        }
    )

    response = client.get("/tasks")

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_get_missing_task():
    response = client.get("/tasks/999")

    assert response.status_code == 404


def test_delete_task():
    client.post(
        "/tasks",
        json={
            "title": "Practice GitHub",
            "description": "Push code",
            "completed": False
        }
    )

    response = client.delete("/tasks/1")

    assert response.status_code == 200
