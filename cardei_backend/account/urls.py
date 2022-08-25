from django.urls import path
from account import views

urlpatterns = [
    path(r'account/<int:pk>/', views.CardeiUserView.as_view({
        'get': 'retrieve', 'put': 'update', 'patch': 'partial_update'
    })),
]
