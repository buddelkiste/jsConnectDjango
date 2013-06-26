# Django imports
from django.http import HttpResponse
from django.views.generic.base import ContextMixin

# Helper imports
from .helpers import embed as embedded_helper
from .helpers import photo as photo_helper
from .helpers import settings as settings_helper
from .helpers.response import js_connect_response


# Local imports
from .forms import JsConnectForm


# Our actual view
def js_connect_auth_view(request):
    user = {}
    if request.user.is_authenticated():
        u = request.user
        user['uniqueid'] = u.id
        user['name'] = u.username
        user['email'] = u.email
        user['photourl'] = photo_helper.fetch_photo(u)

    # Our sercret Server Data
    server_data = {
        'server_client_id': settings_helper.CLIENT_ID,
        'server_secret': settings_helper.SECRET,
    }

    # Prepare form data
    form_data = request.GET.dict()
    form_data.update(server_data)

    form = JsConnectForm(form_data)

    is_valid = form.is_valid()

    # Get data to return from form
    response_data = form.get_response_data(user)
    callback = form.data.get('callback', None)

    return js_connect_response(response_data, callback=callback)


# A simple ContectMixin to use in class-based views to provide
# vanilla_sso_string context variable into template
class EmbeddedSsoMixin(ContextMixin):

    def get_context_data(self, **kwargs):
        context = super(EmbeddedSsoMixin, self).get_context_data(**kwargs)
        context['vanilla_sso_string'] = embedded_helper.get_sso_string(self.request.user)
        return context
