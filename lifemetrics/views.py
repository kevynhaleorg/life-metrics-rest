from django.http import JsonResponse
from lifemetrics.account.models import Organization
import requests
import json

def test(request):
    organization = Organization(name='test')
    organization.save()
    return JsonResponse(json.dumps(list(Organization.objects.all())), safe=False)