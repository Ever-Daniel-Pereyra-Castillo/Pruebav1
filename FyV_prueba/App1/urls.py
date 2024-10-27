from django.urls import path
from App1 import views
urlpatterns = [
    path("",views.listadofyv,name="listadofyv")
]
