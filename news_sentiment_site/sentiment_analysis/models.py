from django.db import models

# Create your models here.
class Article(models.Model):
    article_id = models.AutoField(primary_key=True, db_column='ArticleID')
    title = models.CharField(max_length=255, db_column='Title_EN')
    sentiment_score = models.FloatField(null=True, blank=True, db_column='SentimentScore')
    source = models.CharField(max_length=100, db_column='Source')
    url = models.URLField(db_column='URL')
    
    class Meta:
        db_table = 'Articles'
        managed = False

    def __str__(self):
        return self.title

class ViewAvgSentimentBySource(models.Model):
    source = models.CharField(max_length=255, primary_key=True)
    avgsentiment = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'View_AvgSentimentBySource'
        
        
class ViewNationalMood(models.Model):
    mood = models.CharField(max_length=255, primary_key=True)
    score = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'View_NationalMood'
        
        
class ViewSentimentHeatmap(models.Model):
    source = models.CharField(max_length=255, primary_key=True)
    verynegative = models.IntegerField()
    negative = models.IntegerField()
    neutral = models.IntegerField()
    positive = models.IntegerField()
    verypositive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'View_SentimentHeatmap'
        
class ViewSentimentOverTime(models.Model):
    date = models.DateField(primary_key=True)
    avgsentiment = models.DecimalField(max_digits=5, decimal_places=2)
    
    class Meta:
        managed = False
        db_table = 'View_SentimentOverTime'
        