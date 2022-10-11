from rest_framework.routers import DefaultRouter
from .apiview import Register_api, Login_api, Changepassword_api

router = DefaultRouter()

router.register("register",Register_api, basename="register")
router.register("login",Login_api, basename="login")
router.register("changepass",Changepassword_api, basename="change_password")