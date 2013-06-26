jsConnectDjango
===============

Django implementation of jsConnect for VanillaForums

## Check example for test code

It implements the std interface for a jsConnect addon
you may need to provide your own backend for returning URLs

Basic usage
-----------

### Site-wide Vanilla Forums setup

Steps below should be enough to get you started with the basic jsConnect/SSO integration to your Django project.

1. In your settings.py:

        JS_CONNECT_CLIENT_ID = '[client_id]'
        JS_CONNECT_SECRET = '[secret]'

2. In your urls.py:

        url(r'jsconnect/', include('jsConnectDjango.urls'))
    
3. In the Vanilla Forums dashboard go to jsConnect settings and populate **Authenticate Url** field:

        http://yourdomain.com/jsconnect/
        
### Embedded Vanilla Forums setup

In order to use SSO for embedded Vanilla Forums instance, you need to generate a value for the ``vanilla_sso`` JavaScript variable and put it into the template containing embedded VF snippet. 

There's a simple ``EmbeddedSsoMixin`` which will provide exactly that value in the ``vanilla_sso_string`` context variable.

     from jsConnectDjango.views import EmbeddedSsoMixin
    
     class EmbeddedForumView(EmbeddedSsoMixin, TemplateView):
        template_name = 'forum/embedded.html'
        
        
Then in the ``forum/embedded.html`` template:
    
    <script type="text/javascript">
        var vanilla_sso = '{{ vanilla_sso_string }}';
    </script>
    <script type="text/javascript" src="http://YOURFORUM.vanillaforums.com/js/embed.js"></script>
        
