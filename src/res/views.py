# Create your views here.
from utils.decorators import authenticate
from django.shortcuts import render, render_to_response
from res.models import Resource
from calendar import Calendar, month_name, day_name


@authenticate
def resource_list(user, request):

    resources = Resource.objects.all()

    return render(request, 'resources/resource_list.html',
                  {'resource_list': resources})


@authenticate
def resource_detail(user, request, resource_slug, year, month):
    year, month = int(year), int(month)
    calendar = Calendar()
    month_days = calendar.itermonthdays(year, month)
    days = [[]]
    week = 0
    resource = Resource.objects.get(slug=resource_slug)

    for day in month_days:
        entries = current = False   # are there entries for this day; current day?
        if day:
            pass
            entries = None
            #entries = Entry.objects.filter(date__year=year, date__month=month, date__day=day)

        dname = day_name[len(days[week])]
        days[week].append((day, entries, current, dname))
        if len(days[week]) == 7:
            days.append([])
            week += 1

    return render_to_response("resources/resource_detail.html",
                dict(
                     resource=resource,
                     year=year, month=month, month_days=days,
                     mname=month_name[month]))
