from django.urls import path
from . import views

urlpatterns = [
    
    path("", views.login_view, name="login"),
    path("logout_view/", views.logout_view, name="logout_view"),
    path("register/", views.register, name="register"),
    
    
    path("home", views.home , name="home"),
    path("employeedata/", views.Employeedata , name="employeedata"),
    path("employeeupdate/<int:pk>/", views.updatedata , name="employeeupdate"),
    path("employeeDeletedata/<int:pk>/", views.Deletedata , name="employeeDelete"),
    
    
]
