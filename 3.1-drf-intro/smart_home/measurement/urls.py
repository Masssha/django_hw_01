from django.urls import path

from .views import SensorAPIView, MeasurementListCreateAPIView

urlpatterns = [
    path('sensors/', SensorAPIView.as_view()),
    path('measurements/', MeasurementListCreateAPIView.as_view())
    # TODO: зарегистрируйте необходимые маршруты
]
