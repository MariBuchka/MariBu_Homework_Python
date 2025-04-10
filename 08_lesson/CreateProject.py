from Authorization import BaseUrl

class CreateProject(BaseUrl):

    def __init__(self, base_url, token):
        super().__init__(base_url, token)
        self.endpoint = "projects"


    def create_project(self, title, user=None, role="admin"):
        project = {
            "title": title,
            "users": {
                user: role
            }
        }
        return self._send_request("POST", self.endpoint, json=project)
