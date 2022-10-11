from rest_framework import serializers
from account.models import CustomUser

'''
    new user registration serializers
'''
class Register_serializers(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = CustomUser
        fields = ['email','username','password','password2']
        extra_kwargs = {
            'password':{'write_only':True}
        }


    def validate(self, data):
        password_one = data.get('password')
        password_two = data.get('password2')
        if password_one != password_two:
            raise serializers.ValidationError("Both password does not match, try again !!!")
        return data

    def create(self, validated_data):
        return CustomUser.objects._create_user(**validated_data)

'''
    user login serializer
'''
class Login_serializers(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=200)
    class Meta:
        model = CustomUser
        fields = ["email","password"]

'''
    user password change serializer
'''
class Changepassword_serializers(serializers.ModelSerializer):
    password = serializers.CharField(max_length=200, style={"input_type":"password"},write_only=True)
    password2 = serializers.CharField(max_length=200, style={"input_type":"password"},write_only=True)
    class Meta:
        model = CustomUser
        fields = ['password','password2']   

    def validate(self, data):
        password = data.get('password')
        password2 = data.get('password2')
        user = self.context.get('user')
        print('Change user password is available ', user)
        if password != password2:
            raise serializers.ValidationError("Kindly check both entered password again")
        user.set_password(password)
        user.save()
        return data