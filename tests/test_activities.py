def test_root_redirect(client):
    # Arrange: client fixture provided
    # Act
    resp = client.get('/', follow_redirects=False)
    # Assert
    assert resp.status_code in (301, 302, 307, 308)
    assert '/static/index.html' in resp.headers.get('location', '')


def test_get_activities_contains_expected_keys(client):
    # Arrange
    # Act
    resp = client.get('/activities')
    # Assert
    assert resp.status_code == 200
    data = resp.json()
    assert 'Chess Club' in data
    assert isinstance(data['Chess Club']['participants'], list)
