import pytest
from faker import Factory

faker = Factory.create("pt_BR")


@pytest.fixture(scope="session")
def options_fake():
    return [
        {"option": "A", "description": faker.text()},
        {"option": "B", "description": faker.text()},
        {"option": "C", "description": faker.text()},
        {"option": "D", "description": faker.text()},
    ]


@pytest.fixture(scope="session")
def category_fake():
    return {
        "title": faker.name(),
    }


@pytest.fixture(scope="session")
def post_question_fake(options_fake, category_fake):
    return {
        "title": faker.name(),
        "question": faker.text(),
        "answer": "A",
        "options": options_fake,
        "area": category_fake,
    }
