from rest_framework import serializers
from .models import Person
from django.contrib.auth.models import User


class PeopleSerializer(serializers.ModelSerializer):

    country = serializers.SerializerMethodField()

    class Meta:
        model = Person
        fields = "__all__"

    def validate_age(self, age):
        if age < 18:
            raise serializers.ValidationError("Age should be greater than 17")

        return age

    def validate_name(self, name):
        specialcharacter = "!@#$%%^&*(:)"
        if any(c in specialcharacter for c in name):
            raise serializers.ValidationError(
                "Name should not contain any special character"
            )

        return name

    def get_country(self, data):
        return "India"


class LoginSerializer(serializers.Serializer):
    """
    email verification
    """

    username = serializers.CharField()
    password = serializers.CharField()


class RegisterSerializer(serializers.Serializer):
    """
    register
    """

    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        """
        validation for an user
        """
        if data["username"]:
            if User.objects.filter(username=data["username"]).exists():
                raise serializers.ValidationError("Username is taken")

        if data["email"]:
            if User.objects.filter(email=data["email"]).exists():
                raise serializers.ValidationError("Email is already taken by user")

        return data

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"]
        )
        user.set_password(validated_data['password'])
        user.save()
        # you can use 
        # user.set_password(validated_data['password'])
        print(validated_data)
        return validated_data
