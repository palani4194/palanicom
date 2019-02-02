
from django.urls import include,path
from . import views
from django.views.generic.base import TemplateView # new

# app_name = 'webapp'
urlpatterns = [
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    # url(r'^blogs/', include('blog.urls', namespace='blog')),


]
