from django.urls import path
from .views import (
    LinksListCreateAPIView,
    LinksRetrieveUpdateDestroyAPIView,
    ContatsListCreateAPIView,
    ContatsRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path('links/', LinksListCreateAPIView.as_view(), name='links-list-create'),
    path('links/<int:pk>/', LinksRetrieveUpdateDestroyAPIView.as_view(), name='links-retrieve-update-destroy'),
    path('contacts/', ContatsListCreateAPIView.as_view(), name='contats-list-create'),
    path('contacts/<int:pk>/', ContatsRetrieveUpdateDestroyAPIView.as_view(), name='contats-retrieve-update-destroy'),
]
