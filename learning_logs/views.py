from django.shortcuts import render, redirect
#We import the function redirect, which we’ll use to redirect the user back to the topics 
#page after they submit their topic. The redirect() function takes in the name of a view and redirects the user to that view
from .models import Topic#We first import the model associated with the data we need
from .models import Entry
from .forms import TopicForm, EntryForm#We also import the form we just wrote, TopicForm.
from django.contrib.auth.decorators import login_required
from django.http import Http404
# Create your views here.

def index(request):
    """the home page fpr learning log"""
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    """show all the topics"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')#we query the database by asking for the Topic objects sorted by the date_added attribute
    context = {'topics' : topics }#context is a dict that key is the name we ll use in the template to access data and value is a data that we need to send in the template. here is the topics.
    return render(request, 'learning_logs/topics.html', context)
@login_required
def topic(request, topic_id):#we pass also topic_id in arg because the func accept the value captured by <int:topic_id> and store it in topic_id
    """show the indivuadual topic and its entry"""
    topic = Topic.objects.get(id=topic_id)#we are retrieving the topic by id 
    if topic.owner != request.user:
        raise Http404

    entries =  topic.entry_set.order_by('-date_added')#we get entries associated with this topic
                                            #the minus in front of date_added sort the result in reverse order which display by most recent
    context = {'topic': topic, 'entries': entries}#storing topic and entries in context
    return render(request, 'learning_logs/entries.html', context )#sending context to template
@login_required
def new_topic(request):
    """add a new topic"""
    if request.method != 'POST':#we check if the request method is Get or post(see book for explanation of these keyword).
                                #if request isnt Post , then its probably Get so we return a blank form even if its not post, its safe to reurn a blank
        form = TopicForm()##no data submitted , create a blank form
    else:
        #post data submitted ; process data
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')
    #display a blank or invalid form
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):

    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
    context = {'form': form, 'topic': topic}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if topic.owner != request.user:
        raise Http404
    #initial requests; pre-fill form with current entry
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry , data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)
    context = {'form': form, 'entry':entry, 'topic': topic}
    return render(request, 'learning_logs/edit_entry.html', context)




