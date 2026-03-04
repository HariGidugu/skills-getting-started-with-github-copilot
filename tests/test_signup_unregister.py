from urllib.parse import quote


def test_signup_success_and_state_mutation(client):
    # Arrange
    activity = 'Chess Club'
    email = 'tester+1@example.com'
    # Act
    resp = client.post(f"/activities/{quote(activity)}/signup", params={'email': email})
    # Assert
    assert resp.status_code == 200
    assert email in client.get('/activities').json()[activity]['participants']


def test_signup_existing_email_returns_400(client):
    # Arrange
    activity = 'Chess Club'
    email = 'michael@mergington.edu'
    # Act
    resp = client.post(f"/activities/{quote(activity)}/signup", params={'email': email})
    # Assert
    assert resp.status_code == 400


def test_signup_nonexistent_activity_returns_404(client):
    # Arrange
    activity = 'Nope Club'
    email = 'a@example.com'
    # Act
    resp = client.post(f"/activities/{quote(activity)}/signup", params={'email': email})
    # Assert
    assert resp.status_code == 404


def test_unregister_success_and_state_mutation(client):
    # Arrange
    activity = 'Chess Club'
    email = 'tester+2@example.com'
    # ensure the user is signed up first
    r1 = client.post(f"/activities/{quote(activity)}/signup", params={'email': email})
    assert r1.status_code == 200
    # Act: unregister
    r2 = client.post(f"/activities/{quote(activity)}/unregister", params={'email': email})
    # Assert
    assert r2.status_code == 200
    assert email not in client.get('/activities').json()[activity]['participants']


def test_unregister_not_signed_up_returns_404(client):
    # Arrange
    activity = 'Chess Club'
    email = 'not-present@example.com'
    # Act
    resp = client.post(f"/activities/{quote(activity)}/unregister", params={'email': email})
    # Assert
    assert resp.status_code == 404
