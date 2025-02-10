from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login_view'),
    path('vote/', views.vote_view, name='vote_page'),
    path('vote/status/', views.vote_status, name='vote_status'),
    path('admin-panel/', views.admin_panel, name='admin_panel'),
    path('logout/', views.logout_view, name='logout_view'),
]
