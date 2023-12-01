from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r"printer-lists", views.ListPrinterView)

app_name = "printers"

urlpatterns = [
    path("", include(router.urls)),
    path("category/", views.FloorListAPIView.as_view()),
    path("category/<pk>/", views.FloorAPIView.as_view()),
    path("list/printer/", views.ListPrinterAPIView.as_view()),
    path("create/printer/", views.CreatePrinterAPIView.as_view()),
    path("printer/<pk>/delete/", views.DestroyPrinterAPIView.as_view()),
    path("printer/<pk>/", views.PrinterDetailView.as_view()),
    path("printer/views/", views.PrinterViewsAPIView.as_view()),
]
