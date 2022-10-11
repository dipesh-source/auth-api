from django.contrib import admin
from django.urls import path, include
from api.urls import router
from api.apiview import Register_api, Login_api, Changepassword_api

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',include(router.urls)),
    path("register/",Register_api.as_view(),name="api_register"),
    path("login/",Login_api.as_view(),name="api_login"),
    path("change/",Changepassword_api.as_view(),name="api_change_password"),
]