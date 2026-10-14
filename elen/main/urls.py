from django.urls import path, include
from .views import HomePageView, blo


urlpatterns = [
    path("", HomePageView.as_view(), name="home-page")
    path("", HomePageView.as_view(), name="home-page")
    
]
