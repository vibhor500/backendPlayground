from django.urls import path,include

urlpatterns = [
    path('developer/', include('developer.urls')),
]
