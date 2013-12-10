"""@package res.views.res_list
@author Zosia Sobocinska
@date Dec 10, 2013
"""
from utils.decorators import authenticate
from django.shortcuts import render
from res.models import Resource


@authenticate
def resource_list(user, request):

    resources = Resource.objects.all()

    return render(request, 'resources/resource_list.html',
                  {'resource_list': resources})
