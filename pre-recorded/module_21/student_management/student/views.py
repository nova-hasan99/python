from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from . import models
from . import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

#..............................................................................
def home(request):  # ............................functional view
    students = models.Student.objects.all()
    return render(request, 'student/index.html', {'students' : students})

class StudentList(ListView):  # ..................class view
    model = models.Student
    template_name = 'student/index.html'
    context_object_name = 'students'
#..............................................................................

#.................................this function use for only when using html form method
# def create_student(request):
#     print(request.POST)
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         password = request.POST.get('password')
#         photo = request.FILES.get('photo')
#         checkbox = request.POST.get('checkbox')

#         if checkbox == 'on':
#             checkbox = True
#         else:
#             checkbox = False

#         student = models.Student(name=name, email=email, phone=phone, password=password, checkbox=checkbox, photo=photo)
#         student.save()
#         return render(request, 'student/index.html')

#     return render(request, 'student/index.html')
#............................................................................................

#.................................thsi function using for only using django forms method & its advanced

def create_student(request):  # ......................functional create view
    if request.method == 'POST':
        form = forms.StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Student create successfully.')
            return redirect('home')
    else:
        form = forms.StudentForm()
    return render(request, 'student/create_edit_student.html', {'form' : form})

class CreateStudent(CreateView):         #.....................class create virw
    form_class = forms.StudentForm
    success_url = reverse_lazy('home')
    template_name = 'student/create_edit_student.html'
    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, 'Student create successfully.')
        return super().form_valid(form)

#......................................................................................................

def update_student(request, id):              # ...............functional update view
    student = models.Student.objects.get(id=id)
    form = forms.StudentForm(instance=student)
    if request.method == 'POST':
        form = forms.StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Student info update successfully.')
            return redirect('home')
    return render(request, 'student/create_edit_student.html', {'form' : form, 'edit' : True})

class UpdateStudentData(UpdateView):   # ...............class update view
    form_class = forms.StudentForm
    model = models.Student
    template_name = 'student/create_edit_student.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'
    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, 'Student create successfully.')
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['edit'] = True
        return context
#......................................................................................................

def delete_student(request, id):                  # ...............functional delete view
    student = models.Student.objects.get(id=id)
    student.delete()
    messages.add_message(request, messages.WARNING, 'Student info delete successfully.')
    return redirect('home')

class DeleteStudent(DeleteView):
    model = models.Student
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')
    template_name = 'student/delete_student.html'
    def delete(self, request, *args, **kwargs):
        messages.add_message(request, messages.WARNING, 'Student info delete successfully.')
        return super().delete(self, request, *args, **kwargs)
    
def signup(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Registration Complete')
            return redirect('home')
    else:
        form = forms.SignUpForm()
    return render(request, 'student/auto_form.html', {'form' : form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)

            if user is not None:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, 'User Login Successfully')
                return redirect('home')
            else:
                messages.add_message(request, messages.WARNING, 'Invalid Credentials')
    else:
        form = AuthenticationForm()
    return render(request, 'student/auto_form.html', {'form' : form, 'login' : True})

def user_logout(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, 'Logout Successfully')
    return redirect('home')