ENDPOINT = 'api/v1/students/'


def test_post_student_should_return_422_when_payload_is_invalid(test_app, student_fake):
    response = test_app.post(ENDPOINT)
    assert response.status_code == 422


def test_post_student_should_return_201_when_payload_is_invalid(test_app, student_fake):
    response = test_app.post(ENDPOINT, json=student_fake)
    assert response.status_code == 201
    assert response.json() == {"message": "Aluno Criado com sucesso"}
