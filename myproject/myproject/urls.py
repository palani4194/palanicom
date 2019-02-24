from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from webapp import views
from django.conf.urls import handler404
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf.urls import url, include
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),

    url(r'^admin/', admin.site.urls, name='about'),

    url(r'^employees/', views.employeesList.as_view()),
    url(r'^music/', include('musicfile.urls'), name='about-music'),

    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url('', include('blog.urls')),
    url('', include('errorapp.urls')),
    url('api/', include('posts.urls')),
    url('', include('data.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.sites.AdminSite.site_header = 'Administration'
admin.sites.AdminSite.site_title = 'Administration'
admin.sites.AdminSite.index_title = 'Administration'

handler404 = 'errorapp.views.error_404_view'
