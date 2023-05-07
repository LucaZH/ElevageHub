from django.conf import settings
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('mesanimaux/', views.mesanimaux, name='mesanimaux'),
    path('activites/', views.activites, name='activites'),
    path('stocks/', views.stocks, name='stocks'),
    path('accounts/signup/', views.signup, name='signup'),
    path('animal_list/', views.animal_list, name='animal_list'),
    path('animal/delete/<int:animal_id>/', views.delete_animal, name='delete_animal'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='index.html'), name='logout'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
