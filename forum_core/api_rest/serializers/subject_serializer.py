from rest_framework import serializers
from  .models import Subject
class ForumSerialiizer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'