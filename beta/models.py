from django.db import models

# Create your models here.

class MainData(models.Model):
    word = models.CharField(max_length=50, unique=True)
    definition = models.TextField()

    def __str__(self):
        return self.word

class FeedData(models.Model):
    related_word = models.CharField(max_length=30, default='')
    feedstored = models.CharField(max_length=100, blank=True)
    #browsed_word = models.CharField(max_length=30, default='')

    def __str__(self):
        return f'{self.related_word} | {self.feedstored}'
    
class BData(models.Model):
    choice = models.CharField(max_length=30, default='')
    comment = models.CharField(max_length=100, blank=True)
    #browsed_word = models.CharField(max_length=30, default='')

    def __str__(self):
        return f'{self.choice} | {self.comment}'
