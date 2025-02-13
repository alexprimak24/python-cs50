from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    # priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)

# Create your views here.
def index(request):
    # Check if there is already a list of tasks in the session
    if "tasks" not in request.session:
        # So if there is no - then we would like to create it
        request.session["tasks"] = []
    return render(request, "tasks/index.html",{
        "tasks": request.session["tasks"]
    })

def add(request):
    # Check if the request method is post
    if request.method == 'POST':
        # Then we figure out all submitted data and store it in the 'form'
        form = NewTaskForm(request.POST)
        # We see then if the provided data is really valid, in the right format
        if form.is_valid():
            # if yes, then we add get it and add to the lsit of tasks
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            # After I submit a task and add it to the list of tasks
            # I will be redirected to the index page of tasks application
            return HttpResponseRedirect(reverse("tasks:index"))
        else: 
            # If the form is not valid, return the form (it will show errors on the page too)
            return render(request, "tasks/add.html", {
                "form": form
            })
    # If the request method is not POST at all, then we send a user a clean form
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })