# ensuring that user credentials work

# local imports
from webscraper.scraper.schoology.ensure import ensure_schoology
from webscraper.creds import get_creds

def ensure(user_id, platform_code, encryption_key):
    # get creds
    creds = get_creds(user_id, platform_code, encryption_key)
    if 'message' in creds:
        return creds['message']
    else:
        username = creds['username']
        password = creds['password']

    # test creds
    if platform_code == "sc":
        return ensure(username, password)
