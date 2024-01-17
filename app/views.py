from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect 

job_title = [
    "First Job",
    "Second Job"
]

job_description = [
    "First Job description",
    "Second Job description",
]

# Create your views here.
def hello(request):
    list_job = []
    for count in range(2):
        str = f"<ul><li>Job {count}: Title: {job_title[count]}, Description: {job_description[count]}</ul></li>"
        list_job.append(str)
        
    return HttpResponse(list_job)

def job_detail(request, id):
    print(type(id))
    
    if id == 0:
        return redirect('/')
    return_html = f"<h1>{job_title[id]}</h1> <h3>{job_description[id]}</h3>"
    return HttpResponse(return_html)