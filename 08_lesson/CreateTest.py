import pytest
from CreateProject import CreateProject

@pytest.fixture
def create_project():
    return CreateProject("https://yougile.com/api-v2/", "")


def test_create_project_success(create_project):
    response = create_project.create_project("My New Project", "d2ce74b6-ee30-4132-ac6f-50078eea5efe" , "admin")
    assert response.status_code == 201


def test_create_negative(create_project):
    response = create_project.create_project("")
    assert response.status_code == 400
