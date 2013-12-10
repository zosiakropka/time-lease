"""@package res.views.res_book
@author Zosia Sobocinska
@date Dec 10, 2013
"""
from utils.decorators import authenticate, not_implemented
from res.models import Resource
from django.shortcuts import render


@not_implemented
@authenticate
def resource_book(user, request, resource_slug, year, month, day, hour, minute):

    return render(request, 'resources/resource_book.html', {})
