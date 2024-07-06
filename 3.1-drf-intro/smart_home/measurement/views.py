# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Sensor, Measurement
from .serializers import MeasurementSerializer, SensorDetailSerializer, SensorSerializer


class SensorAPIView(APIView):
    def get(self, request):
        id = request.data.get("id", False)
        if id:
            sensor = Sensor.objects.get(id=id)
        else:
            sensor = Sensor.objects.all()
        serializer = SensorDetailSerializer(sensor, many=False if id else True)
        return Response(serializer.data)


    def post(self, request):
        serializer = SensorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request):
        id = request.data.get("id")
        sensor = Sensor.objects.get(id=id)
        serializer = SensorSerializer(sensor,
                                            data=request.data,
                                            partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MeasurementListCreateAPIView(generics.ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer







