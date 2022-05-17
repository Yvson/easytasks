from django.conf import settings
from datetime import datetime
from ipware import get_client_ip


class Cookie(object):

    def __init__(self, request) -> None:
        """
        Initializing cookie management.
        """
        self.session = request.session
        cookie = self.session.get(settings.COOKIES_SESSION_ID)
        if not cookie:
            cookie = self.session[settings.COOKIES_SESSION_ID] = {}
            cookie['IP'] = self.get_ip_address(request)
            cookie['username'] = 'anonymous' if request.user.username == '' else request.user.username
            cookie['cookie_functional'] = {'status': 'OFF'}
            cookie['cookie_marketing'] = {'status': 'OFF'}
            cookie['created_at'] = str(datetime.now())
            cookie['updated_at'] = 'None'
        if cookie:
            if request.user.is_authenticated:
                cookie['username'] = request.user.username
        self.cookie = cookie
        
        super().__init__()

    def add(self, cookie_name, cookie_content):
        """
        Add a specific cookie if it is not currently in the session property.
        """
        if cookie_name not in self.cookie:
            self.cookie[cookie_name] = cookie_content
            self.save()

    def remove(self, cookie_name):
        """
        Remove a specific cookie.
        """
        if cookie_name in self.cookie:
            del self.cookie[cookie_name]
            self.save()

    def update(self, cookie_name, cookie_content):
        """
        Update a specific cookie that is currently in the session property.
        """
        if cookie_name in self.cookie:
            self.cookie[cookie_name] = cookie_content
            self.save()

    def remove(self, cookie_name):
        """
        Remove a specific cookie.
        """
        if cookie_name in self.cookie:
            del self.cookie[cookie_name]
            self.save()


    def activate(self, cookie_name):
        """
        Activate a specific cookie.
        """
        if cookie_name in self.cookie:
            self.cookie[cookie_name] = {'status': 'ON'}
            self.save()

    def deactivate(self, cookie_name):
        """
        Deactivate a specific cookie.
        """
        if cookie_name in self.cookie:
            self.cookie[cookie_name] = {'status': 'OFF'}
            self.save()

    def save(self):
        """
        Save any modification done to Cookie object in the session property
        """
        self.session.modified = True
    
    def clear(self):
        """
        Remove cookie parameter from session
        """
        del self.session[settings.COOKIES_SESSION_ID]
        self.save()

    def set_expiry_zero(self):
        """
        Set expiry setting to zero.
        Session cookie will expire when the user’s Web browser is closed.
        """
        self.session.set_expiry(0)
        self.save()

    def set_expiry_none(self):
        """
        Set expiry setting to none.
        Session reverts to using the global session expiry policy.
        """
        self.session.set_expiry(None)
        self.save()
    
    def get_ip_address(self, request):
        """
        Get IP address of the original user request 
        """
        client_ip, is_routable = get_client_ip(request)
        if client_ip is None:
            return {
                    'address':'unknown',
                    'type': 'unknown'
                } # Unable to get the client's IP address
        else:
            # We got the client's IP address
            if is_routable:
                return {
                        'address': client_ip,
                        'type': 'public'
                    } # The client's IP address is publicly routable on the Internet
            else:
                return {
                        'address': client_ip,
                        'type': 'private'
                    } # The client's IP address is private
        # Order of precedence is (Public, Private, Loopback, None)        