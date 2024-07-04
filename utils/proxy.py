from django.shortcuts import render
import requests
from rest_framework.views import APIView
from rest_framework.response import Response

class ProxyView(APIView):
    def proxy_request(self, request, service_url):
        headers = {
            'Authorization': request.headers.get('Authorization')
        }
        response = requests.request(
            method=request.method,
            url=service_url,
            headers=headers,
            data=request.data,
            params=request.query_params
        )
        return Response(response.json(), status=response.status_code)