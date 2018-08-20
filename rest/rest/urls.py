from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from HlloWrld import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hllowrld/', views.TextView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
