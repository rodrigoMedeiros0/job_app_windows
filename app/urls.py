from django.urls import path

from app.views import hello, job_detail

urlpatterns = [
    path('', hello),
    path('job/<int:id>', job_detail)
]