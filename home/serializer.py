"""
serializer
"""

from rest_framework import serializers
from .models import Person


class PeopleSerializer(serializers.ModelSerializer):

    country = serializers.SerializerMethodField()
<<<<<<< HEAD
=======
    
>>>>>>> testing
    class Meta:
        model = Person
        fields = '__all__'

<<<<<<< HEAD
    def get_country(self, obj):
        return "India"

    def validate_age(self, age):
        if age < 18:
            raise serializers.ValidationError('age should be greator than 18')
=======
    def validate_age(self, age):
        if age < 18:
            raise serializers.ValidationError('Age should be greater than 17')
>>>>>>> testing
        
        return age
    
    def validate_name(self, name):
<<<<<<< HEAD
        special_characters = "!@#$%^&*()_+|"
        print("data", name)
        if any (c in special_characters for c in name):
            raise serializers.ValidationError('Name should not contain any special character')        
        return name
git 
=======
        specialcharacter = '!@#$%%^&*(:)'
        if any(c in specialcharacter for c in name):
            raise serializers.ValidationError('Name should not contain any special character')
        
        return name
    
    def get_country(self, data):
        return "India"
>>>>>>> testing
