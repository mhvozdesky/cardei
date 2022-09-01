from django.urls import path, include
from account import views


urlpatterns = [
    path('account/reg/', views.RegistrationCardeiUserView.as_view()),
    path('account/login/', views.LoginCardeiUserView.as_view()),
    path('account/logout/', views.LogoutCardeiUserView.as_view()),
    path('profile/', views.CardeiUserProfile.as_view({
        'get': 'retrieve',  # 'put': 'update', 'patch': 'partial_update'
    })),
]
