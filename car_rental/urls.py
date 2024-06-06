from django.contrib import admin
from django.urls import path, include
from .authentication import login_page, signup_page, logout_account

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_app.urls'), name="home"),
    path('authentication/login', login_page, name="login"),
    path('authentication/signup', signup_page, name="signup"),
    path('authentication/logout', logout_account, name="logout"),
    path("__reload__/", include("django_browser_reload.urls")),
]
