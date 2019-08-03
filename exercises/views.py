from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages

from exercises.forms import SearchStudentForm, AddStudentForm, PizzaToppingsForm, UserValidationForm, UserForm, \
    ResetPasswordForm
from .models import SCHOOL_CLASS, Student, SchoolSubject, StudentGrades


# Create your views here.
class SchoolView(View):

    def get(self, request):
        return render(request, "school.html",
                      {"SCHOOL_CLASS": SCHOOL_CLASS})


class SchoolClassView(View):
    def get(self, request, school_class):
        students = Student.objects.filter(school_class=school_class)
        return render(request, "class.html", {"students": students,
                                              "class_name": SCHOOL_CLASS[int(school_class) - 1][1]})


class StudentView(View):
    def get(self, request, student_id):
        student = Student.objects.get(pk=student_id)
        subjects = SchoolSubject.objects.all()
        return render(request, "students.html", {"student": student,
                                                 "subjects": subjects})


class GradesView(View):
    def get(self, request, student_id, subject_id):
        student = Student.objects.get(pk=student_id)
        grades = StudentGrades.objects.filter(school_subject=subject_id, student=student_id)
        average = []
        for g in grades:
            average.append(g.grade)

        if len(average) > 0:
            av = sum(average) / len(average)
        else:
            av = 0
        return render(request, "grades.html", {"student": student,
                                               "grades": grades,
                                               "average": av})


class StudentSearchFormView(View):
    def get(self, request):
        form = SearchStudentForm()
        if "last_name" in request.GET:
            search_ctx = request.GET["last_name"]
            students = Student.objects.filter(last_name__icontains=search_ctx)
        else:
            students = None
        return render(request, "student_search_form.html", {"form": form,
                                                            "students": students})


class StudentAddFormView(View):
    def get(self, request):
        form = AddStudentForm()
        return render(request, "student_add.html", {"form": form})

    def post(self, request):
        form = AddStudentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            klasa = form.cleaned_data['klasa']
            Student.objects.create(first_name=name, last_name=surname, school_class=klasa)
            return HttpResponseRedirect('/student_add/')


class PizzaToppingsView(View):
    def get(self, request):
        form = PizzaToppingsForm()
        return render(request, "pizza_toppings.html", {"form": form})


class UserValidationView(View):
    def get(self, request):
        form = UserValidationForm()
        return render(request, "user_validation.html", {"form": form})

    def post(self, request):
        form = UserValidationForm(request.POST)
        if form.is_valid():
            return render(request, "user_validation.html", {"form": form})
        else:
            return render(request, "user_validation.html", {"form": form})


class UsersView(View):
    def get(self, request):
        users = User.objects.all()
        return render(request, "users.html", {"users": users})


class LoginView(View):
    def get(self, request):
        form = UserForm()
        return render(request, 'login.html', {"form": form})

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('users_view')
        return redirect('login')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('users_view')


class ResetPassword(PermissionRequiredMixin, View):
    permission_required = 'auth.change_user'
    def get(self, request, user_id):
        form = ResetPasswordForm()
        return render(request, 'reset_password.html', {"form": form,
                                                       "user_id": user_id})

    def post(self, request, user_id):
        form = ResetPasswordForm(request.POST)
        if form.is_valid(): # and request.user.has_perm("auth.change_user"):
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            if password == repeat_password:
                user = User.objects.get(pk=user_id)
                user.password = password
                user.save()
                messages.success(request, 'Your password was successfully changed')
            else:
                print("Warning is added")
                messages.warning(request, 'Something went horribly wrong!')
        else:
            messages.warning(request, 'You dont have permissions to do that')
        return redirect('reset_password', user_id=user_id)
