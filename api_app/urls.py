from django.urls import path
from .views import * # importing all views

urlpatterns = [
    # just checking that request is work is fine
    path('checking-api/', checking_api),

    # here is student-api endpoints
    path('student-api/', student_api),
]
