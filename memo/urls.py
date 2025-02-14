from django.urls import path
from . import views

app_name = 'memo'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('createMemo/', views.MemoCreateView.as_view(), name='create'), 
    path('<int:pk>/update/', views.UpdateView.as_view(), name="update"),
    path('<int:pk>/delete/', views.DeleteView.as_view(), name="delete"),
    path('createTag/', views.TagCreateView.as_view(), name="tag"),
    path('search/', views.search, name='search'),
]