"""
serializer
"""

from rest_framework import serializers
from .models import Person


class PeopleSerializer(serializers.ModelSerializer):

    country = serializers.SerializerMethodField()
    class Meta:
        model = Person
        fields = '__all__'

    def get_country(self, obj):
        return "India"

    def validate_age(self, age):
        if age < 18:
            raise serializers.ValidationError('age should be greator than 18')
        
        return age
    
    def validate_name(self, name):
        special_characters = "!@#$%^&*()_+|"
        print("data", name)
        if any (c in special_characters for c in name):
            raise serializers.ValidationError('Name should not contain any special character')        
        return name
