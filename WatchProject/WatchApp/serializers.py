from rest_framework import serializers
from .models import Watch

class WatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watch
        fields  = ['id', 'name', 'brand','price','image','created','updated']
