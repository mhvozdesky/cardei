from django.urls import path, include
from account import views

from rest_framework.routers import SimpleRouter, DefaultRouter

# router = SimpleRouter()
# router.register('account', views.RegistrationCardeiUserViewSet,
#                  basename='account')
# router.register('account/auth',
#                 views.AuthCardeiUserViewSet,
#                 basename='account/auth')
# for i in router.urls:
#     print(i)

urlpatterns = [
    path('account/reg/', views.RegistrationCardeiUserView.as_view()),
    path('profile/', views.CardeiUserProfile.as_view({
        'get': 'retrieve', 'put': 'update', 'patch': 'partial_update'
    })),
]
