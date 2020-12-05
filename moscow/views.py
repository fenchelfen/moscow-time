import pytz
from django.http import JsonResponse
from datetime import datetime


def moscow_time(request, *args, **kwargs):
    tz = pytz.timezone('Europe/Moscow')
    moscow_now = datetime.now(tz)

    return JsonResponse(dict(
        moscow_time=moscow_now
    ))
