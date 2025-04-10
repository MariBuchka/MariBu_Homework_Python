from Authorization import BaseUrl

class UpdateProject(BaseUrl):

    def __init__(self, base_url, token):
        super().__init__(base_url, token)


    def update_project(self, project_id, title=None, users=None, deleted=False):
        endpoint = f"projects/{project_id}"
        new_project = {}
        if title: new_project["title"] = title
        if users: new_project["users"] = users
        if deleted: new_project["deleted"] = deleted

        return self._send_request("PUT", endpoint, json=new_project)
