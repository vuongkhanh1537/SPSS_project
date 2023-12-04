from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r"printer-lists", views.ListPrinterView)
#router.register(r'printer', views.PrinterViewSet, basename='printer')
app_name = "printers"

urlpatterns = [
    path("", include(router.urls)),
    path("floor/", views.FloorListAPIView.as_view()),
    path("floor/<pk>/", views.FloorAPIView.as_view()),
    path("list/", views.ListPrinterAPIView.as_view()),
    path("create/", views.CreatePrinterAPIView.as_view()),
    path("<pk>/update-page/", views.UpdatePagesRemainingAPIView.as_view()),
    path("<pk>/delete/", views.DestroyPrinterAPIView.as_view()),
    path("<pk>/", views.PrinterDetailView.as_view()),
]
