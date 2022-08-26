from django.urls import path, include
from account import views

from rest_framework.routers import SimpleRouter, DefaultRouter

router = DefaultRouter()
router.register('account', views.AuthenticatedCardeiUserViewSet, basename='me')
# for i in router.urls:
#     print(i)

urlpatterns = [
    # path(r'account/<int:pk>/', views.CardeiUserView.as_view({
    #     'get': 'retrieve', 'put': 'update', 'patch': 'partial_update'
    # })),
    path('', include(router.urls)),
]
