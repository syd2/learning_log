
"""defines url patterns for learning_logs"""

from django.urls import path#this func help us when mapping urls to views
from . import views

app_name = 'learning_logs'#helps Django distinguish this urls.py file from files of the same name in other apps within the project

urlpatterns = [
    #home page
    path('', views.index , name='index' ),#se the book for the explanation of the args
    #topic page
    path('topics/', views.topics, name='topics'),
    #individual topic page
    path('topics/<int:topic_id>/', views.topic, name='topic'),#the url will use the topic id attribute to show which topic was requested
                                                            #to do this we use <int:topic_id> as topic_id s are int
    #new topic url (when users wanna create a new topic)
    path('new_topic/', views.new_topic, name='new_topic'),
    #new entry url. we use the int topic_id because we can add multiple entries
    path('new_entry/<int:topic_id>', views.new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry' )
]#this variable urlspatterns is a list of individual page that can be requested to learning_logs app
 