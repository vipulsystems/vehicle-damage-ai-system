from app.services.auth_service import login_user


def test_login_invalid_user():
    result = login_user("invalid@email.com", "wrongpass")

    assert result is None