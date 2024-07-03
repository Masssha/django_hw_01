# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Sensor, Measurement
from .serializers import MeasurementSerializer, SensorDetailSerializer

# вот благодаря наследованию этого классу можно делать пост и гет?
class SensorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

class SensorRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

# записать новые данные получилось, но эта таблица, кажется, ничего
# не знает о таблице с датчиками :D в таблице про счетчики этих данных нет
class MeasurementListCreateAPIView(generics.ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

# вроде благодаря наследованию от основного класса получилось сделать
# пут и патч, но как-то тут много всякого дописано, смысл чего я не очень поняла
class TransformSensor(APIView):
    def patch(self, request, pk):
        transformer = Sensor.objects.get(pk=pk)
        serializer = SensorDetailSerializer(transformer,
                                           data=request.data,
                                           partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# а это кусок кода из урока, вроде нам говорили, что если наследовать ListAPIView,
# то можно сделать гет и пост, но пост реализовать не получилось, а потом я прочитала,
# что ListAPIView работает только для гет. хм. вообще хотелось бы побольше узнать,
# какие еще есть расширенные классы от апивью
    # class SensorAPIView(generics.ListAPIView):
#     serializer_class = SensorDetailSerializer
#     # queryset = Sensor.objects.all()
#     def get_queryset(self):
#         queryset = Sensor.objects.all()
#     def post(self, request):
#         return self.list(request)



