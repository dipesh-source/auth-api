from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, login, logout
from .serializers import (
    Register_serializers,
    Changepassword_serializers,
    Login_serializers,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


"""
    will return token to new registered user 
"""


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


"""
    Register APIView
"""


class Register_api(APIView):
    def post(self, request, formate=None):
        serializer = Register_serializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response(
                {"data": "User registered successfully", "token": token},
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""
    Login APIView for user login
"""


class Login_api(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request, formate=None):
        serializer = Login_serializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get("email")
            password = serializer.data.get("password")
            user = authenticate(email=email, password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response(
                    {"data": "Login success", "token": token}, status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {
                        "errors": {
                            "non_fields_errors": [
                                "email or password wrong, check again"
                            ]
                        }
                    }
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""
    User change password APIView
"""


class Changepassword_api(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request, formate=None):
        serializer = Changepassword_serializers(
            data=request.data, context={"user": request.user}
        )
        if serializer.is_valid(raise_exception=True):
<<<<<<< HEAD
            return Response(
                {"data": "Password Changed Successfully"},
                status=status.HTTP_201_CREATED,
            )
=======
            return Response({'data':'Password Changed Successfully'}, status=status.HTTP_201_CREATED)
>>>>>>> origin/master
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
