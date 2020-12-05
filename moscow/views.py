from django.http import HttpResponseBadRequest, JsonResponse

from moscow.settings import MOSCOW_TIME_API

import requests


def moscow_time(request, *args, **kwargs):
    res = requests.get(MOSCOW_TIME_API)

    if res.status_code != 200 or not hasattr(res, 'json'):
        return HttpResponseBadRequest('External service temporarily unavailable')

    return JsonResponse(dict(
        utc_datetime=res.json().get('utc_datetime')
    ))
