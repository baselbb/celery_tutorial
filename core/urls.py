from django.conf.urls import url

from . import views

app_name = "core"

urlpatterns = [
    url(r"generate/", views.GenerateRandomUserView.as_view(), name="generate"),
]