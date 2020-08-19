from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from space_pi_api.models import TempHistory, HumidityHistory
from space_pi_api.serializers import TempHistorySerializer, HumidityHistorySerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def temp_history_list(request):
    if request.method == 'GET':
        tempHistorical = TempHistory.objects.all()
        temp_history_serializer = TempHistorySerializer(tempHistorical, many=True)
        return JsonResponse(temp_history_serializer.data, safe=False)


    elif request.method == 'POST':
        temp_history_data = JSONParser().parse(request)
        temp_history_serializer = TempHistorySerializer(data=temp_history_data)
        if temp_history_serializer.is_valid():
            temp_history_serializer.save()
            return JsonResponse(temp_history_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(temp_history_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def temp_history_detail(request, pk):
    # find tutorial by pk (id)
    try: 
        temp_history = TempHistory.objects.get(pk=pk) 
    except TempHistory.DoesNotExist: 
        return JsonResponse({'message': 'The requested Temp History does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        temp_history_serializer = TempHistorySerializer(temp_history) 
        return JsonResponse(temp_history_serializer.data) 
    # GET / PUT / DELETE tutorial
