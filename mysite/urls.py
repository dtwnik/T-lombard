from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('item/<int:id>/', views.detail, name='product'),
    path('login/', views.MyprojectLoginView.as_view(), name='login_page'),
    path('register/', views.RegisterUserView.as_view(), name='register_page'),
    path('logout/', views.MyProjectLogout.as_view(), name='logout_page'),
]