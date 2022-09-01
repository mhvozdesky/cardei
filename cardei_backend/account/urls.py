from django.urls import path, include
from account import views


urlpatterns = [
    path('account/reg/', views.RegistrationCardeiUserView.as_view(), name='url_reg'),
    path('account/login/', views.LoginCardeiUserView.as_view(), name='url_login'),
    path('account/logout/', views.LogoutCardeiUserView.as_view(), name='url_logout'),
    path('profile/', views.CardeiUserProfile.as_view({
        'get': 'retrieve',  # 'put': 'update', 'patch': 'partial_update'
    }), name='url_profile'),
]
