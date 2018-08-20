from developer import views
from django.urls import path,include

urlpatterns = [
    path('', views.respond, name="hello"),
]
