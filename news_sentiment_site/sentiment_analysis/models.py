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
