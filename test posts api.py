"""
test_posts_api.py
Python-side validation using `requests` + `pytest`.
This complements the Postman collection: Postman covers single-request
validation, while these tests chain multiple calls together (create ->
verify -> update -> delete) which is harder to express cleanly in
Postman's per-request test scripts.
"""

import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_single_post_status_and_fields():
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200

    body = response.json()
    for field in ("id", "title", "body", "userId"):
        assert field in body, f"Missing field: {field}"


def test_get_nonexistent_post_returns_404():
    response = requests.get(f"{BASE_URL}/posts/99999")
    assert response.status_code == 404


def test_create_then_verify_post_chain():
    """
    Chained validation: create a post, then confirm the response
    reflects what we sent. (JSONPlaceholder is a mock API and won't
    actually persist the record, so we only validate the create
    response itself here - a real API would let us GET it back too.)
    """
    payload = {
        "title": "Chained test post",
        "body": "Created via requests, then validated",
        "userId": 5,
    }
    create_response = requests.post(f"{BASE_URL}/posts", json=payload)
    assert create_response.status_code == 201

    created = create_response.json()
    assert created["title"] == payload["title"]
    assert created["userId"] == payload["userId"]
    assert "id" in created


def test_update_post():
    payload = {"id": 1, "title": "Updated via requests", "body": "...", "userId": 1}
    response = requests.put(f"{BASE_URL}/posts/1", json=payload)
    assert response.status_code == 200
    assert response.json()["title"] == "Updated via requests"


def test_delete_post():
    response = requests.delete(f"{BASE_URL}/posts/1")
    assert response.status_code == 200


def test_response_time_under_threshold():
    response = requests.get(f"{BASE_URL}/posts")
    assert response.elapsed.total_seconds() < 2.0
    assert response.status_code == 200
    assert isinstance(response.json(), list)
