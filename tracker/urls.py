from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/dashboard/'), name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('colleges/', views.college_search, name='college_search'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]