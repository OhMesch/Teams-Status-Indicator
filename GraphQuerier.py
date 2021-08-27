import requests

from DeviceCodePrinter import DeviceCodePrinter
from TokenManager import TokenManager

class GraphQuerier():
    API_ENDPOINT = "https://graph.microsoft.com/"
    API_VER = "v1.0"

    def __init__(self):
        self.tokenManager = TokenManager()

    def getTeamsStatus(self):
        if (tk := self.tokenManager.getTokenSilent()):
            pass
        else:
            device_flow =self.tokenManager.initDeviceFlow()
            code_printer = DeviceCodePrinter(device_flow["user_code"])
            code_printer.printUntilComplete()
            tk = self.tokenManager.getTokenDeviceFlow(device_flow)
            code_printer.complete()

        request_url = f"{self.API_ENDPOINT}/{self.API_VER}/me/presence"
        auth = {'Authorization': 'Bearer ' + tk['access_token']}
        r = requests.get(request_url, headers=auth, timeout=5)

        print(r.status_code)
        print(r.json())
        return(r)