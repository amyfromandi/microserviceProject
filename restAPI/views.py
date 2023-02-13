from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
import json

def get_birds(lat, lng):
    api_url = f"https://api.ebird.org/v2/data/obs/geo/recent?lat={lat}&lng={lng}"
    response = requests.get(api_url, headers={'X-eBirdApiToken':'s4sb8r00n02s'})
    myjson = response.json()
    return myjson

@api_view(['POST'])
def post_birds(request):
    resp = json.loads(request.body.decode('utf-8'))
    latitude = resp[0].get("lat")
    longitude = resp[0].get("lng")
    myjson = get_birds(latitude, longitude)
    return Response(myjson)


