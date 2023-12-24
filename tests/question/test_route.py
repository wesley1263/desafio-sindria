ENDPOINT = 'api/v1/questions/'


def test_endpoint_get_question_should_return_200_when_called(test_app):
    response = test_app.get(ENDPOINT)
    _payload = response.json()

    assert response.status_code == 200
    assert "page" in _payload
    assert "limit" in _payload
    assert "total" in _payload
    assert "total_pages" in _payload
    assert isinstance(_payload["data"], list)
    assert _payload["limit"] == 10
    assert _payload["page"] == 1


def test_endpoint_create_question_should_return_422_when_payload_is_invalid(test_app):
    response = test_app.post(ENDPOINT + "create")
    assert response.status_code == 422


def test_endpoint_create_question_should_return_201_when_payload_is_valid(test_app, post_question_fake):
    response = test_app.post(ENDPOINT + "create", json=post_question_fake)
    assert response.status_code == 201
