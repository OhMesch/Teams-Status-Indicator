import requests

from TokenManager import TokenManager

class GraphQuerier():
    API_ENDPOINT = "https://graph.microsoft.com/"
    API_VER = "v1.0"

    def __init__(self):
        self.tokenManager = TokenManager()

    def getTeamsStatus(self):
        request_url = f"{self.API_ENDPOINT}/{self.API_VER}/me/presence"
        tk = self.tokenManager.getToken()
        auth = {'Authorization': 'Bearer ' + tk['access_token']}
        r = requests.get(request_url, headers=auth, timeout=5)

        print(r.status_code)
        print(r.json()["availability"])
        print(r.json()["activity"])
        return(r)