from django.urls import path
from .views import (AvgSentimentBySourceList, NationalMoodList, 
                    SentimentHeatmap, SentimentOverTime, article_list, home)

urlpatterns = [
    path('articles/', article_list, name='article_list'),
    path('', home, name='home'),
    path('api/avg-sentiment-by-source/', AvgSentimentBySourceList.as_view(), name='avg-sentiment-by-source'),
    path('api/national-mood/', NationalMoodList.as_view(), name='national-mood'),
    path('api/sentiment-heatmap/', SentimentHeatmap.as_view(), name='sentiment-heatmap'),
    path('api/sentiment-over-time/', SentimentOverTime.as_view(), name='sentiment-over-time'),
]
