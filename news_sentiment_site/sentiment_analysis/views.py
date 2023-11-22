from django.shortcuts import render
from .models import Article, ViewAvgSentimentBySource, ViewNationalMood, ViewSentimentHeatmap, ViewSentimentOverTime
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AvgSentimentBySourceSerializer, NationalMoodSerializer, SentimentHeatmapSerializer, SentimentOverTimeSerializer


def article_list(request):
    articles = Article.objects.all()
    return render(request, 'sentiment_analysis/article_list.html', {'articles': articles})

def home(request):
    return render(request, 'sentiment_analysis/home.html')

"""
class AvgSentimentBySourceList(APIView):
    def get(self, request, format=None):
        data = list(ViewAvgSentimentBySource.objects.all().values())
        return Response(data)

class NationalMoodList(APIView):
    def get(self, request, format=None):
        data = list(ViewNationalMood.objects.all().values())
        return Response(data)
    
class SentimentHeatmap(APIView):
    def get(self, request, format=None):
        data = list(ViewSentimentHeatmap.objects.all().values())
        return Response(data)
    
class SentimentOverTime(APIView):
    def get(self, request, format=None):
        data = list(ViewSentimentOverTime.objects.all().values())
        return Response(data)
"""  

    
class AvgSentimentBySourceList(APIView):
    def get(self, request, format=None):
        queryset = ViewAvgSentimentBySource.objects.all()
        serializer = AvgSentimentBySourceSerializer(queryset, many=True)
        return Response(serializer.data)

class NationalMoodList(APIView):
    def get(self, request, format=None):
        queryset = ViewNationalMood.objects.all()
        serializer = NationalMoodSerializer(queryset, many=True)
        return Response(serializer.data)
    
class SentimentHeatmap(APIView):
    def get(self, request, format=None):
        queryset = ViewSentimentHeatmap.objects.all()
        serializer = SentimentHeatmapSerializer(queryset, many=True)
        return Response(serializer.data)
    
class SentimentOverTime(APIView):
    def get(self, request, format=None):
        queryset = ViewSentimentOverTime.objects.all()
        serializer = SentimentOverTimeSerializer(queryset, many=True)
        return Response(serializer.data)