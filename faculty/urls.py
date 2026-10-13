from django.urls import path

from faculty import views

app_name = "faculty"

urlpatterns = [
    path("", views.home, name="home"),
    path("programs", views.programs, name="programs"),
    path("programs/<id>", views.program_details, name="program_details"),
    path("departments", views.departments, name="departments"),
    path("departments/<id>", views.department_details, name="department_details"),
    path("exchange_programs", views.exchange_programs, name="exchange_programs"),
]
