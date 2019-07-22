from rest_framework import serializers
from .models import Person


class ChoiceField(serializers.ChoiceField):
    def to_representation(self, obj):
        return self._choices[obj]



class PersonSerializer(serializers.ModelSerializer):
    sex = serializers.CharField(source='get_sex_display')
    race = serializers.CharField(source='get_race_display')
    relationship = serializers.CharField(source='get_relationship_display')
    class Meta:
        model = Person
        fields = '__all__'


class RelationshipGraphSerializer(serializers.Serializer):
    relationship = ChoiceField(choices=Person.RELATIONSHIP_CHOICES)
    count = serializers.IntegerField()


class SexGraphSerializer(serializers.Serializer):
    sex = ChoiceField(choices=Person.SEX_CHOICES)
    count = serializers.IntegerField()
