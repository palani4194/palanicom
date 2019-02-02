from django.conf.urls import include, url
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'musicfile'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='contentofindex'),
    url(r'^register/$', views.LoginView.as_view(), name='register'),

    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='DetailOfAlbums'),

    url(r'^album/add/$', views.AlbumCreate.as_view(), name='AlbumCreate'),
    url(r'^album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='AlbumUpdate'),
    url(r'^album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='AlbumDelete'),


    url(r'^(?P<album_id>[0-9]+)/favourite/$', views.favourite, name='favourite'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
