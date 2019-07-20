from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import SCHOOL_CLASS, Student, SchoolSubject, StudentGrades

# Create your views here.
class SchoolView(View):

    def get(self, request):
        return render(request, "school.html",
                      { "SCHOOL_CLASS": SCHOOL_CLASS })


class SchoolClassView(View):

    def get(self, request, school_class):
        students = Student.objects.filter(school_class=school_class)
        return render(request, "class.html", {"students": students,
                                              "class_name": SCHOOL_CLASS[int(school_class)-1][1]})


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

        if len(average)>0:
            av = sum(average)/len(average)
        else:
            av = 0
        return render(request, "grades.html", {"student": student,
                                               "grades": grades,
                                               "average": av})
