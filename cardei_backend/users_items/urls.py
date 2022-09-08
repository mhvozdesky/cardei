from django.urls import path, include
from users_items import views


urlpatterns = [
    path('items/', views.ItemsViewSet.as_view({
        'get': 'items_list', 'post': 'create_item'
    }), name='url_items'),
    path('items/<int:pk>/', views.ItemsViewSet.as_view(
        {'patch': 'partial_update', 'get': 'items_detail'}),
        name='url_items_detail'
         ),
    path('taglist/', views.TagListView.as_view()),
    path('categorylist/', views.CategoryListView.as_view())
]
