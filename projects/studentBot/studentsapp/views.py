from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from . import forms
from . import models
from .forms import SignUpForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied


import google.generativeai as genai
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.db import connection
import requests
from bs4 import BeautifulSoup


genai.configure(api_key=settings.GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# ✅ সকল টেবিল থেকে ডাটা সংগ্রহ করুন
def fetch_database_info():
    data = {}
    try:
        with connection.cursor() as cursor:
            cursor.execute("SHOW TABLES;")
            tables = cursor.fetchall()

            for table in tables:
                table_name = table[0]
                cursor.execute(f"SELECT * FROM `{table_name}` LIMIT 5;")  # প্রথম ৫টি রো দেখানো
                rows = cursor.fetchall()
                column_names = [desc[0] for desc in cursor.description]
                data[table_name] = [dict(zip(column_names, row)) for row in rows]

    except Exception as e:
        return {"error": f"Database Fetch Error: {str(e)}"}

    return data

# ✅ ওয়েবসাইট কন্টেন্ট লাইভভাবে পড়ুন
def fetch_website_content():
    url = "http://127.0.0.1:8000"  # আপনার সাইটের URL দিন
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            text = soup.get_text(separator=" ")
            return text[:3000]  # শুধু প্রথম 3000 ক্যারেক্টার পাঠাবো
        return "Could not fetch website content."
    except Exception as e:
        return f"Error fetching website: {str(e)}"

@csrf_exempt
def chatbot(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_question = data.get("question", "")

        if not user_question:
            return JsonResponse({"error": "No question provided"}, status=400)

        try:
            # ✅ ডাটাবেজ ও ওয়েবসাইটের তথ্য সংগ্রহ করুন
            database_data = fetch_database_info()
            website_data = fetch_website_content()

            # ✅ Gemini API-তে ডাটাবেজ ও ওয়েব তথ্য পাঠানো
            chat = model.start_chat(history=[])
            full_prompt = f"""
            You are a smart chatbot that answers questions dynamically using database information and live website content.

            🔹 Database Info:
            {json.dumps(database_data, indent=2)}

            🔹 Website Content:
            {website_data}

            User Question: {user_question}
            """

            response = chat.send_message(full_prompt)
            return JsonResponse({"answer": response.text})

        except Exception as e:
            return JsonResponse({"error": f"API Error: {str(e)}"}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=400)






#..........................................................................................................
class studentList(ListView):
    model = models.Student
    template_name = 'home.html'
    context_object_name = 'students'

class ownStudents(LoginRequiredMixin, ListView):
    model = models.Student
    template_name = 'own_students.html'
    context_object_name = 'students'

    def get_queryset(self):
        return models.Student.objects.filter(user=self.request.user)
    
class studentDetails(DetailView):
    model = models.Student
    template_name = 'details.html'
    context_object_name = 'student'
    

class studentCreate(LoginRequiredMixin, CreateView):
    form_class = forms.StudentForm
    success_url = reverse_lazy('home')
    template_name = 'create_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create'] = True 
        return context

    def form_valid(self, form):
        student = form.save(commit=False)
        student.user = self.request.user
        student.save()
        messages.add_message(self.request, messages.SUCCESS, 'Student create successfully.')
        return super().form_valid(form)
    
from django.core.exceptions import PermissionDenied

class studentUpdate(LoginRequiredMixin, UpdateView):
    """Update student details - Only allow the owner to edit"""
    model = models.Student
    form_class = forms.StudentForm
    template_name = 'create_update.html'
    success_url = reverse_lazy('own')

    def get_object(self, queryset=None):
        """Ensure only the student owner can edit"""
        obj = super().get_object(queryset)
        
        if obj.user != self.request.user:  # Check if the logged-in user is the owner
            raise PermissionDenied("You are not allowed to edit this student!")  # Restrict access
        
        return obj

    def form_valid(self, form):
        """Show success message on successful update"""
        messages.success(self.request, "Student updated successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        """Show error messages on form errors"""
        messages.error(self.request, "❌ Something went wrong! Please check the form.")
        return self.render_to_response(self.get_context_data(form=form))
    

class studentDelete(LoginRequiredMixin, DeleteView):
    """Allow only the owner to delete their students"""
    model = models.Student
    template_name = 'create_update.html'
    success_url = reverse_lazy('own')

    def get_object(self, queryset=None):
        """Ensure only the student owner can delete"""
        obj = super().get_object(queryset)
        if obj.user != self.request.user:
            raise PermissionDenied("You are not allowed to delete this student!")
        return obj

    def delete(self, request, *args, **kwargs):
        """Show success message on successful delete"""
        messages.success(self.request, "Student deleted successfully!")
        return super().delete(request, *args, **kwargs)


class signup(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'login.html'
    success_url = reverse_lazy('userLogin')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['signup'] = True 
        return context

    def form_valid(self, form):
        user = form.save()
        # login(self.request, user)   # user login directly when complete registratoin
        messages.success(self.request, 'Registratoin successfully!!')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"❌ {form.fields[field].label}: {error}")
        return self.render_to_response(self.get_context_data(form=form))
    
class UserLoginView(LoginView):
    template_name = "login.html"
    form_class = forms.LoginForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, 'Login successfully!')
        return super().form_valid(form)

    def form_invalid(self, form):
        if 'username' in form.errors:
            messages.error(self.request, "❌ Username or Email is incorrect!")
        if 'password' in form.errors:
            messages.error(self.request, "❌ Password is incorrect!")

        if form.non_field_errors():
            for error in form.non_field_errors():
                messages.error(self.request, f"❌ {error}")

        return self.render_to_response(self.get_context_data(form=form))
    
    

    

        
        
        
    
    
    




