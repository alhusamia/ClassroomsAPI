from rest_framework import serializers
from classes.models import Classroom


class ClassListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['teacher','year','subject','name','id']

class ClassroomDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['teacher','year','subject','name','id']

class CreatClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['year','subject','name']

class UpdateClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['year','subject','name']
