from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django import forms
# Create your views here.
from django.urls import reverse


class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = [];
    return render(request, "tasks/index.html",{
        "tasks":request.session["tasks"]
    })
def add(request):
    if request.method == "POST":
        form=NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request,"tasks/add.html",{
                "form":form
            })
    return render(request, "tasks/add.html",{
        "form": NewTaskForm()
    })