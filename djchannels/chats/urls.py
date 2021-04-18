from django.urls import path
from .views import RoomView

urlpatterns = [
    path('rooms/<int:pk>/', RoomView.as_view())
]
