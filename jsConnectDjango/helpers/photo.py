# Python imports
import importlib

# Django imports
from django.conf import settings

# Local imports
from .settings import PHOTO_BACKEND


class DummyPhotoBackend(object):
    default_photo = ''

    # Get the actual profile photo
    def fetch(self, user, default_photo=None):
        return default_photo


# Choose the fetcher class
backend_klass = DummyPhotoBackend
try:
    backend_module_name, backend_klass_name = PHOTO_BACKEND.rsplit('.', 1)
    backend_module = __import__(backend_module_name,
                                fromlist=[backend_klass_name, ])
    backend_klass = getattr(backend_module, backend_klass_name)
except (ImportError, TypeError, AttributeError):
    backend_klass = DummyPhotoBackend


# API function to call
def fetch_photo(user):
    backend = backend_klass()
    return backend.fetch(user, backend.default_photo)
