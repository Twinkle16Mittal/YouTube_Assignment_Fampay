from .models import Youtube_details
from .views import YoutubeDataView,background_view
from django.urls import path

urlpatterns = [
    path('data/',YoutubeDataView),
    path('',background_view)
    
]