from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostList.as_view()),

    path('<int:pk>/', views.PostDetail.as_view(), name='read'),
    path('create/', views.PostCreate.as_view(), name='create'),
    path('update/<int:pk>/', views.PostUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', views.PostDelete.as_view(), name='delete'),

]
