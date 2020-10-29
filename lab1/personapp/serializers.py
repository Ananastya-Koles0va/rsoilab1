from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Person
        fields = '__all__'

