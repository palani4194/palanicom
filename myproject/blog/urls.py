
from django.urls import include,path
from . import views
from django.contrib.auth import views as auth_views
# app_name = 'blog'


urlpatterns = [
    # path(' ', views.home, name='home'),

    path('blog/', views.post_list, name='post_list'),
    path('blog/post/<int:pk>', views.post_detail_view, name='post_detail_view'),
    path('blog/post/new', views.post_new, name='post_new'),
    path('blog/post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('blog/drafts/', views.post_draft_list, name='post_draft_list'),

    path('blog/post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('blog/post/<int:pk>/remove/', views.post_remove, name='post_remove'),

    path('blog/post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),

    # path('about/', views.about, name='about'),

    path('blog/login/', auth_views.LoginView.as_view(), {'template_name': 'registration/login.html'}, name='login'),
    path('blog/logouts/', auth_views.LogoutView.as_view(), {'template_name': 'registration/logged_outs.html'}, name='logout'),
    path('blog/register/', views.register, name='register'),
    path('blog/profile/', views.profile, name='profile'),
    path('blog/profile/edit/', views.profile_edit, name='profile_edit'),
    path('blog/change-password/', views.change_password, name='change_password'),
    path('blog/password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('blog/password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('blog/password-reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('blog/password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),







]
