"""@package utils.decorators
@author: Zosia Sobocinska
@date Dec 7, 2013
"""
from django.shortcuts import redirect
from timelease.settings import LOGIN_URL


class authenticate:
    __name__ = None
    __module = None
    f = None
    user = None

    def __init__(self, f):
        self.f = f
        self.__name__ = f.__name__
        self.__module__ = f.__module__

    def __call__(self, request, *args, **kwargs):
        user = request.user
        if not (user and user.is_authenticated()):
            return redirect('%s/?next=%s' % (LOGIN_URL, request.path))
        else:
            return self.f(user, request, *args, **kwargs)


class not_implemented:
    f = None
    user = None

    def __init__(self, f):
        self.f = f

    def __call__(self, request, *args, **kwargs):
        raise Exception("Function %s.%s not implemented." % (self.f.__module__, self.f.__name__))
