from django.urls import path

from .views import SensorListCreateAPIView, SensorRetrieveAPIView, MeasurementListCreateAPIView, TransformSensor

urlpatterns = [
    path('sensors/', SensorListCreateAPIView.as_view()),
    path('measurements/', MeasurementListCreateAPIView.as_view()),
    path('sensor/<pk>/', SensorRetrieveAPIView.as_view()),
    path('transformer/<pk>/', TransformSensor.as_view()),
    # TODO: зарегистрируйте необходимые маршруты
]
