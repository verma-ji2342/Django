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

    def validate_age(self, age):
        if age < 18:
            raise serializers.ValidationError('Age should be greater than 17')
        
        return age
    
    def validate_name(self, name):
        specialcharacter = '!@#$%%^&*(:)'
        if any(c in specialcharacter for c in name):
            raise serializers.ValidationError('Name should not contain any special character')
        
        return name
    
    def get_country(self, data):
        return "India"