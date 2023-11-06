from django.urls import path, include, re_path
from .views import ProfileFormView

urlpatterns = [
    re_path(r'^api/profile/(?P<pk>[0-9]+)/$', ProfileFormView.as_view()),
]