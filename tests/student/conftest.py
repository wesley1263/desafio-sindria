import pytest
from faker import Factory

faker = Factory.create()


@pytest.fixture
def student_fake():
    return {"name": faker.name(), "email": faker.email(), "rn": f"AB{faker.pyint(min_value=100, max_value=999)}"}
