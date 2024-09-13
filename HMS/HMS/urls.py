
from django.contrib import admin
from django.urls import path
from hospital import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',views.about,name='about'),
    path('nav/',views.navs,name='navs'),
    path('',views.Index,name='home'),
    path('admin_login/',views.Login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('contact',views.contact,name='contact'),
    path('view_doctor/',views.view_doctor,name='view_doctor'),
    path('add_doctor/',views.add_doctor,name='add_doctor'),
    path('edit/doctor/<int:doctor_id>/', views.edit_doctor, name='edit_doctor'),
    path('view_patient/',views.view_patient,name='view_patient'),
    path('add_patient/',views.add_patient,name='add_patient'),
    path('edit_patient/<int:patient_id>/', views.edit_patient, name='edit_patient'),
    path('delete_doctor/<int:pid>/', views.delete_doctor, name='delete_doctor'),
    path('delete_patient/<int:pid>/', views.delete_patient, name='delete_patient'),
    path('view_appontment/',views.view_appointment,name='view_appointment'),
    path('add_appointment/',views.add_appointment,name='add_appointment'),
    path('delete_appointment/<int:pid>/', views.delete_appointment, name='delete_appointment'),
    path('edit_appointment/<int:appointment_id>/', views.edit_appointment, name='edit_appointment'),
    
]
