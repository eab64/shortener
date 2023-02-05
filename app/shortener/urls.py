from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# router = DefaultRouter()
# router.register(r'', views.UrlViewSet, basename="urls")




urlpatterns = [
    path('', views.short_url, name='short_url'),
    path('<str:hash>', views.redirect_url, name='redirect_url'),
    path('click_statistics/', views.click_statistics, name='click_statistics'),
]
