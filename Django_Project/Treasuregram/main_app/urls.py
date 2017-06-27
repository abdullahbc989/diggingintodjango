from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    # This URL looks for a number and captures that value to send to the detail view
    url(r'^([0-9]+)/$', views.detail, name="detail"),
]
