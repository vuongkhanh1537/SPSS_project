# urls.py
from django.urls import path
from .views import PrinterListAPIView, PrinterDetailAPIView
app_name = 'printers'
urlpatterns = [
    path('', PrinterListAPIView.as_view(), name='printer-list'),
    path('<int:id>/', PrinterDetailAPIView.as_view(), name='printer-detail'),
]
