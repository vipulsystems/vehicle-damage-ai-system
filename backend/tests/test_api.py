from app import create_app


def test_app_creation():
    app = create_app()
    assert app is not None


def test_invalid_route():
    app = create_app()
    client = app.test_client()

    response = client.get("/invalid-route")

    assert response.status_code == 404