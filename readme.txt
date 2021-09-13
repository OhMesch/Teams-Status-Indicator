# One-Liner
Create a simple visualization of a user's current MS Team's Availability.


# Approach
Uses Microsoft Graph restful API to query a user's current MS Team's status.
PI Zero uses unicorn hat mini to visualize status


# Setup
MS Configuration done through https://portal.azure.com/
Must create a new "App Registration" to allow user access to graph api for MS Teams
With an app registered through the azure portal, this application relies on a secret.json file in the following format:
{
    "appId": "Your-Application-ID-From-App-Portal",
    "tenantID": "Your-Directory-ID-From-App-Portal"
}

This application uses msal and PublicClientApplication over ConfidentialClientApplication. While the PublicClientApplication avoids the need for microsoft account admin approval, the token acquistion methods are more annoying for long running headless applications such as this.
Once the initial authorization token is obtained, it is continually refreshed using the corresponding refresh token, thus a single authorization per application instance is usually sufficiant.
For a PublicClientApplication, the easiest login type to configure would likely be hardcoding a username/password combination on disk, however, I couldn't bring myself to submit to this method.
As I'm running this remotely, I eventually opted for a device flow login, allowing me to submit a code to microsoft.com/devicelogin to auth the application.

Ideally a ConfidentialClientApplication would allow for a certification or personal token authorization which could be stored long term on the server machine.


# References to explore:
https://github.com/maxi07/Teams-Presence/blob/master/teams-presence.py
https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow
https://msal-python.readthedocs.io/en/latest/#msal.PublicClientApplication.initiate_device_flow
https://stackoverflow.com/questions/56393182/how-to-get-access-token-without-sign-up-or-sign-in-to-web-app
https://github.com/pimoroni/unicornhatmini-python/blob/master/examples/text.py