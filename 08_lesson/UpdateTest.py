import pytest
from UpdateProject import UpdateProject
from CreateProject import CreateProject

@pytest.fixture
def update_project():
    return UpdateProject("https://yougile.com/api-v2/", "wP-wVV2Hl9ngTUueTwKlYen03kczRfsjaWX3+pC+dkO9bpboZOB9nKFR0jmf4EC5")


@pytest.fixture
def test_create_project():
    create_project = CreateProject("https://yougile.com/api-v2/", "wP-wVV2Hl9ngTUueTwKlYen03kczRfsjaWX3+pC+dkO9bpboZOB9nKFR0jmf4EC5")
    response = create_project.create_project("Test update", "d2ce74b6-ee30-4132-ac6f-50078eea5efe" , "admin")
    return response.json()["id"]


def test_update_project_success(update_project, test_create_project):
    response = update_project.update_project(test_create_project, title="New Title")
    assert response.status_code == 200


def test_update_nonexistent_project(update_project):
    response = update_project.update_project("00000000-0000-0000-0000-000000000000", title="Base")
    assert response.status_code == 404
