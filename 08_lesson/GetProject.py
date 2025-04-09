from Authorization import BaseUrl

class GetProject(BaseUrl):

    def __init__(self, base_url, token):
        super().__init__(base_url, token)


    def get_project(self, project_id):
        endpoint = f"projects/{project_id}"
        return self._send_request("GET", endpoint)
