# Python imports
from time import time
from base64 import b64encode

# Django imports
from django.utils import simplejson as json

# Helper imports
from .hash import js_connect_embedded_hash
from .photo import fetch_photo
from .settings import CLIENT_ID
from .settings import SECRET


def get_sso_string(user):

    if user.is_authenticated() is False:
        return ''

    user_data = {}
    user_data['uniqueid'] = user.id
    user_data['name'] = user.username
    user_data['email'] = user.email
    user_data['photourl'] = fetch_photo(user)
    user_data['client_id'] = CLIENT_ID

    timestamp = int(time())
    signature_string = b64encode(json.dumps(user_data))
    signature = js_connect_embedded_hash("%s %s" % (signature_string, timestamp), SECRET)

    return "%s %s %s hmacsha1" % (signature_string, signature, str(timestamp))
