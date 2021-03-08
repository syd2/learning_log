from django import forms
from .models import Topic, Entry#importig the models that we wanna work with

class TopicForm(forms.ModelForm):#defining a class that inherits from forms.ModelForm
                                #The simplest version of a ModelForm consists of a nested Meta class telling Django which model to base the form on and which fields to include in the form
    class Meta:
        model = Topic#we build a form from the Topic mode
        fields = ['text']#we include only the text fields in the forms
        labels = {'text': ''}#we tell to djnago to not generate a label for the text field

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        label = {'text' : 'Entry : '}#we want the form to add a label 'entry'
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}#we use the forms.Textarea of the widget and add cols attrs of 80  to give users much space