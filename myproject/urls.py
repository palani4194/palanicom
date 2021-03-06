from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from webapp import views

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf.urls import url, include
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    # path('about/', views.AboutPageView.as_view(), name='about'),
    url(r'^admin/', admin.site.urls, name='about'),
    url(r'^employees/', views.employeesList.as_view()),
    url(r'^music/', include('musicfile.urls'), name='about-music'),

    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url('', include('blog.urls')),


]
