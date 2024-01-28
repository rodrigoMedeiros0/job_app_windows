from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse
from django.template import loader
from app.models import JobPost

job_title = [
    "First Job",
    "Second Job",
    "Third  Job"
]

job_description = [
    "First Job description",
    "Second Job description",
    'Third Job Description'
]

# Create your views here.

class TempClass:
    x = 5

def job_list(request):
    jobs = JobPost.objects.all()
    context={"jobs": jobs} 
    return render(request, "app/index.html", context)


def job_detail(request, id):

    try:
        if id == 1:
            return redirect(reverse('jobs_home'))
        job = JobPost.objects.get(id=id)
        context={"job": job }
        return render(request, "app/job_detail.html", context)
    except:
        return HttpResponseNotFound("Page not found.")
    
def hello(request):
    list = ["Elefante", "Tigre"]
    temp = TempClass()
    is_authenticated = False
    context={"name": "Django", "first_list": list, "temp_object": temp, "age": 29,
             "is_authenticated": is_authenticated}
    return render(request, "app/hello.html", context)
    