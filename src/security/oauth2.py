```python
import os
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

# Get user credentials from environment variables
USER_EMAIL = os.getenv('USER_EMAIL')
USER_CREDENTIALS = os.getenv('USER_CREDENTIALS')

# OAuth2 client setup
client = BackendApplicationClient(client_id=USER_EMAIL)
oauth = OAuth2Session(client=client)

def get_token():
    """
    Function to get OAuth2 token
    """
    token = oauth.fetch_token(token_url='https://provider.com/oauth2/token',
                              client_id=USER_EMAIL,
                              client_secret=USER_CREDENTIALS)
    return token

def oauth2_authenticate():
    """
    Function to authenticate user using OAuth2
    """
    token = get_token()
    if token:
        print("Authentication successful")
    else:
        print("Authentication failed")

oauth2_authenticate()
```