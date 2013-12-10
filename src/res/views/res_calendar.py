"""@package res.views.res_calendar
@author: Zosia Sobocinska
@date Dec 10, 2013
"""
from utils.decorators import authenticate
from django.shortcuts import render_to_response
from res.models import Resource, Occupation
from calendar import Calendar, month_name, day_name
from django.utils.timezone import now
from datetime import date
from django.utils.datetime_safe import datetime


@authenticate
def resource_calendar(user, request, resource_slug, year, month):
    year, month = int(year), int(month)
    calendar = Calendar()
    month_days = calendar.itermonthdays(year, month)
    week = 0
    days = [([], week)]
    resource = Resource.objects.get(slug=resource_slug)

    today = date.timetuple(now())

    for day in month_days:
        hours = []
        entries = curr_day = None   # are there entries for this day; current day?
        if day != 0:
            day_date = datetime(year, month, day)
            pass
            bookings = [occ for occ in Occupation.objects.filter(level=Occupation.BOOK) if occ.date_overlaps(day_date)]
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
                    quarters.append(("%s:%s" % (hour, quarter * 15), ownership))
                hours.append((hour, quarters))
            entries = None
            #entries = Entry.objects.filter(date__year=year, date__month=month, date__day=day)
            curr_day = today.tm_year == year and today.tm_mon == month and today.tm_mday == day

        dname = day_name[len(days[week][0])]
        day = day if (day >= today.tm_mday or (month != today.tm_mon or year != today.tm_year)) else 0
        days[week][0].append((day, entries, curr_day, dname[:3], hours))
        if len(days[week][0]) == 7:
            valid = False
            for day in days[week][0]:
                if day[0] != 0:
                    valid = True
                    break
            if valid:
                week += 1
            else:
                days.pop(-1)
            days.append(([], week))
    days.pop(-1)

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

    return render_to_response("resources/resource_detail.html",
                dict(
                     resource=resource,
                     year=year, month=month, month_days=days,
                     mname=month_name[month],
                     n_month=n_month, n_year=n_year,
                     p_month=p_month, p_year=p_year))
