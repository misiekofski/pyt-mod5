"""coderslab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from exercises.views import SchoolView, SchoolClassView, StudentView, GradesView, StudentSearchFormView, \
    StudentAddFormView, PizzaToppingsView, UserValidationView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', SchoolView.as_view(), name="index"),
    url(r'^class/(?P<school_class>(\d)+)', SchoolClassView.as_view(), 
        name="school-class"),
    url(r'^students/(?P<student_id>(\d)+)', StudentView.as_view(), name="students"),
    url(r'^grades/(?P<student_id>(\d)+)/(?P<subject_id>(\d)+)', GradesView.as_view(), name="grades"),
    url(r'^student_search/', StudentSearchFormView.as_view(), name="search_student"),
    url(r'^student_add/', StudentAddFormView.as_view(), name="add_student"),
    url(r'^pizza/', PizzaToppingsView.as_view(), name="pizza"),
    url(r'^d2_p3_e1/', UserValidationView.as_view(), name="user_validation")
]
