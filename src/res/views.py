# Create your views here.
from utils.decorators import authenticate
from django.shortcuts import render, render_to_response
from res.models import Resource, Occupation
from calendar import Calendar, month_name, day_name
from django.utils.timezone import now
from datetime import date
from django.utils.datetime_safe import datetime
from django.db.models import Q


@authenticate
def resource_list(user, request):

    resources = Resource.objects.all()

    return render(request, 'resources/resource_list.html',
                  {'resource_list': resources})


@authenticate
def resource_calendar(user, request, resource_slug, year, month):
    year, month = int(year), int(month)
    calendar = Calendar()
    month_days = calendar.itermonthdays(year, month)
    days = [[]]
    week = 0
    resource = Resource.objects.get(slug=resource_slug)

    today = date.timetuple(now())

    for day in month_days:
        hours = []
        entries = current = False   # are there entries for this day; current day?
        if day:
            day_date = datetime(year, month, day)
            pass
            bookings = [occ for occ in Occupation.objects.filter(level=Occupation.BOOK) if occ.date_overlaps(day_date)]
            print bookings
            for hour in range(0, Occupation.HOURS):
                quarters = []
                for quarter in range(0, Occupation.QUARTERS):
                    ownership = "free"
                    for occ in bookings:
                        if occ.quarter_overlaps(hour, quarter):
                            if occ.user == user:
                                ownership = "booked"
                            else:
                                ownership = "occupied"
                    quarters.append((quarter, ownership))
                hours.append((hour, quarters))
            entries = None
            #entries = Entry.objects.filter(date__year=year, date__month=month, date__day=day)
            current = today.tm_year == year and today.tm_mon == month and today.tm_mday == day

        dname = day_name[len(days[week])]
        days[week].append((day, entries, current, dname[:3], hours))
        if len(days[week]) == 7:
            days.append([])
            week += 1

    n_year = year
    n_month = month + 1
    if n_month > 12:
        n_month = 1
        n_year += 1

    p_year = year
    p_month = month - 1
    if p_month < 1:
        p_month = 12
        p_year -= 1

    return render_to_response("resources/resource_calendar.html",
                dict(
                     resource=resource,
                     year=year, month=month, month_days=days,
                     mname=month_name[month],
                     n_month=n_month, n_year=n_year,
                     p_month=p_month, p_year=p_year))
