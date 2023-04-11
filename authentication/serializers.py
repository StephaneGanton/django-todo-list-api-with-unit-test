from rest_framework import serializers
from authentication.models import User

class RegisterSerializer(serializers.ModelSerializer):
    password =  serializers.CharField(max_length=128, min_length=6, write_only=True)

    class Meta:
        model =  User
        fields = ('username', 'email', 'password')

    # we need to be sure that our serializer implement the create method

    def create(self, validated_data):
        return User.objects.create_user( **validated_data )

class LoginSerializer(serializers.ModelSerializer):
    password =  serializers.CharField(max_length=128, min_length=6, write_only=True)

    class Meta:
        model =  User
        fields = ('email', 'username', 'password', 'token')

        read_only_fields = ['token'] # as the token is served my our app; so we don't it to be send to the server by the user

