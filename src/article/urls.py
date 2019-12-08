from django.urls import path
from .views import ArticlesListView, CategoryListView
urlpatterns=[
    path('', ArticlesListView.as_view(), name='home'),
    path('<str:category>/', CategoryListView.as_view(), name='category')
]