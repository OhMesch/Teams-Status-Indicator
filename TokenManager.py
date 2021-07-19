import json
import msal

class TokenManager():
    MS_LOGIN = "https://login.microsoftonline.com"

    PRESENCE_SCOPE = [
        'User.Read',
        'Presence.Read']

    def __init__(self):
        with open('secret.json') as secret_file:
            secrets = json.load(secret_file)

        applicationID = secrets["appId"]
        directoryID = secrets["dirId"]

        self.publicApplication = msal.PublicClientApplication(
            applicationID,
            authority=f"{self.MS_LOGIN}/{directoryID}")

    def getToken(self):
        cache = self.publicApplication.get_accounts()
        if (len(cache) == 1):
            return self.publicApplication.acquire_token_silent(self.PRESENCE_SCOPE, account=cache[0])
        
        return self.publicApplication.acquire_token_interactive(scopes=self.PRESENCE_SCOPE)