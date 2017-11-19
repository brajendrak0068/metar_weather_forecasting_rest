from django.shortcuts import render
from weather_forecasting.services import http_service
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.conf import settings

class GetWeatherInfo(APIView):
    def get (self, request):
        station_code = request.query_params.get('scode', None)
        nocache = request.query_params.get('nocache', None)
        if station_code:
            url = settings.METAR_REPORT_API['URL']
            url = url+station_code+'.TXT' 
        else:
            raise exceptions.ParseError("scode is not supplied")

        response_dict  =  http_service.get_data(url, settings.METAR_REPORT_API['REDIS_KEY_EXPIRY'], nocache)  #call http service to get data from third party api
        return Response({'data':response_dict['data']}, status=response_dict['status_code'])   #send the json response and forward the http status code received from metar api

class GetPingResponse(APIView):
    def get (self, request):    
        return Response({'data':'pong'}, status=status.HTTP_200_OK)

