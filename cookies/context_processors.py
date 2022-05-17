from .cookie import Cookie


def cookies(request):
    return {'cookies': Cookie(request)}