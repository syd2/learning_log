from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#a models tell django how to works with the data that will be stored in the currents app.
#see the book for more explanation.
class Topic(models.Model):
    """a topic the user is learning about """
    text = models.CharField(max_length=200)#this create a string field for small to large sized of string(such as name, city...) and its arg tell django how much space it should reserve in the database
    date_added = models.DateTimeField(auto_now_add=True)#this record the date and time the arg tell django to automativally set this attr to the current date and time 
    owner = models.ForeignKey(User, on_delete=models.CASCADE)#a foreign key relation btw user and topic
    def __str__(self):
        """returning a string representation of the model """
        return self.text

class Entry(models.Model):
    """something specific leaned about the topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)#This is the code that connects each entry to a specific topic
    text = models.TextField()#this reserve a large text field in the db
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self):
        return self.text[:50] + '...'
