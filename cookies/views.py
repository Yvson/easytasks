from django.shortcuts import render
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST
from django.http import JsonResponse, HttpResponseRedirect

from .cookie import Cookie

from ast import literal_eval
from datetime import datetime


class CookieView(View):

    def post(self, request, *args, **kwargs):
        cookie = Cookie(request)
        request = dict(request.POST)
        cookie_functional = request.get('cookie-functional')
        cookie_marketing = request.get('cookie-marketing')
        cookie.update('updated_at', str(datetime.now()))

        
        if cookie_functional and cookie_functional[0] == 'on':
            cookie.activate('cookie_functional')
            cookie.set_expiry_none()
        else:
            cookie.deactivate('cookie_functional')
            cookie.set_expiry_zero()
            

        if cookie_marketing and cookie_marketing[0] == 'on':
            cookie.activate('cookie_marketing')
        else:
            cookie.deactivate('cookie_marketing')

        return JsonResponse({'status': 'updated'})


