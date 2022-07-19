from rest_framework import serializers
from .models import Subject, Sheet, Reference, Tutorial, Exam


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['pk', 'name', 'sheets', 'references', 'tutorials', 'exams']


class SheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sheet
        fields = ['pk', 'name', 'content']


class ReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reference
        fields = ['pk', 'name', 'content']


class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutorial
        fields = ['pk', 'name', 'content']


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['pk', 'name', 'content']
