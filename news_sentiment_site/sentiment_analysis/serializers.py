# serializers.py

from rest_framework import serializers
from .models import ViewAvgSentimentBySource, ViewNationalMood, ViewSentimentOverTime, ViewSentimentHeatmap

class AvgSentimentBySourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewAvgSentimentBySource
        fields = '__all__'

class NationalMoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewNationalMood
        fields = '__all__'
        
class SentimentOverTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewSentimentOverTime
        fields = '__all__'

class SentimentHeatmapSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewSentimentHeatmap
        fields = '__all__'
