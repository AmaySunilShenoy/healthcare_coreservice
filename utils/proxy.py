from django.shortcuts import render
import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import HttpResponse

class ProxyView(APIView):
    def proxy_request(self, request):
        try:
            headers = {
                'Authorization': request.headers.get('Authorization'),
                'Content-Type': 'application/json'
            }
            

            
            # Send the request to the actual service
            response = requests.request(
                method=request.method,
                url=self.url,
                headers=headers,
                data=request.body,
            )
            
            
            # Return the response with the same status code
            return HttpResponse(
                content=response.content,
                status=response.status_code,
            )
        except:
            return HttpResponse({'detail': 'Service temporarily unavailable, try again later.'}, status=503)