from django.shortcuts import render

# Create your views here.

import datetime
from django.shortcuts import render
import datetime

def index(request):
    now = datetime.datetime.now()
    bday_month = 5
    bday_day = 23
    bday_year = 1996
    age = now.year - bday_year;
    return render(request, "mybirthday/index.html",{
        "bday": now.month == bday_month and now.day == bday_day,
         "age":age
    })
