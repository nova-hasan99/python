from django.urls import path
from . import views

urlpatterns = [
    # ....................................................................functional based views url
    # path('home/', views.home, name='home'),
    # path('create/', views.create_student, name='create_student'),
    # path('edit/<int:id>', views.update_student, name='update_student'),
    # path('delete/<int:id>', views.delete_student, name='delete_student'),

    #.....................................................................class based virws url
    path('home/', views.StudentList.as_view(), name='home'),
    path('edit/<int:id>', views.UpdateStudentData.as_view(), name='update_student'),
    path('delete/<int:id>', views.DeleteStudent.as_view(), name='delete_student'),
    path('create/', views.CreateStudent.as_view(), name='create_student'),

]
