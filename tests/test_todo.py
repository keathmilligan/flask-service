"""
Test Service
"""

import json
import pytest


@pytest.fixture
def client(monkeypatch):
    """
    API test fixture - bypass regular JWT check
    """
    import sample

    app = sample.create_app()
    from flask_jwt_extended import view_decorators

    monkeypatch.setattr(
        view_decorators, "verify_jwt_in_request", lambda w, x, y, z: None
    )
    return app.test_client()


def test_get_all(client):
    rv = client.get("/api/todos")
    assert rv.status_code == 200
    data = json.loads(rv.data.decode("utf-8"))
    assert len(data) == 4


def test_get(client):
    rv = client.get("/api/todos/0")
    assert rv.status_code == 200
    data = json.loads(rv.data.decode("utf-8"))
    assert data["summary"] == "Pick up groceries"
    assert data["status"] == "TO-DO"
