from django.urls import path , include
from . views import register_view, Login_View, Logout_View

app_name = 'users'

urlpatterns = [
    path("register/", register_view, name="register"),
    path("login/", Login_View, name="login"),
    path("logout/", Logout_View, name="logout"),
]
