from django.urls import path, include
from users_items import views


urlpatterns = [
    path('items/', views.ItemsViewSet.as_view({
        'get': 'items_list', 'post': 'create'
    }), name='url_items'),
]
