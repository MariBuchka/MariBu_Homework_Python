import pytest
from GetProject import GetProject
from CreateProject import CreateProject

@pytest.fixture
def get_project():
    return GetProject("https://yougile.com/api-v2/", "")


@pytest.fixture
def test_create_project():
    create_project = CreateProject("https://yougile.com/api-v2/", "")
    response = create_project.create_project("Test get", "d2ce74b6-ee30-4132-ac6f-50078eea5efe" , "admin")
    return response.json()["id"]


def test_get_project_success(get_project, test_create_project):
    response = get_project.get_project(test_create_project)
    assert response.status_code == 200
    assert response.json()["id"] == test_create_project


def test_get_nonexistent_project(get_project):
    response = get_project.get_project("00000000-0000-0000-0000-000000000000")
    assert response.status_code == 404
