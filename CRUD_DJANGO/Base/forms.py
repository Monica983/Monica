from django import forms
from .models import Student,Module,Course

class StudentForms(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'username', 'email', 'is_active', 'course']

class ModuleForms(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['name', 'start_date', 'code', 'finish_date']


class CourseForms(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
