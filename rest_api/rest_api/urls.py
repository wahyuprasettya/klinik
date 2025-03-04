from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt import views as jwt_views
from .views import DoctorDetailView,AddDoctor,ListDoctorView,DeleteDoctor,UpdateDoctor
from .views import PatienteDetailView,AddPatient,ListPatientView,PatientDelete,UpdatePatient
from .views import RegisterUserTokenView
from .views import ArticleDetailView,ListArticleView

#todo feature

# from .views import AppointmentListCreate,AppointmentDetail


urlpatterns = [
    path('', views.DoctorListCreate.as_view(), name='doctors'),
    path('admin/', admin.site.urls), 
    path('api/', views.DoctorListCreate.as_view(), name='doctors'),
    path('api/doctor/', views.DoctorListCreate.as_view(), name='doctors'),
    path('api/doctor/<int:pk>/', views.DoctorDetail.as_view(), name='doctor-detail'),
    path('api/patient/', views.PatientListCreate.as_view(), name='patient'),
    path('api/patient/<int:pk>/', views.PatientDetail.as_view(), name='patient-detail'),
    # path('api/Appointment/', views.AppointmentListCreate.as_view(), name='Appointment'),
    # path('api/Appointment/<int:pk>/', views.AppointmentDetail.as_view(), name='Appointment-detail'),
    
    
    #doctor
    path('api/doctor/get_doctor/',ListDoctorView.as_view(), name='doctor-list'),
    path('api/doctor/get_doctor_detail/<int:pk>/', DoctorDetailView.as_view(), name='doctor-get'),
    path('api/doctor/add_doctor/',AddDoctor.as_view(), name='add-doctor'),
    path('api/doctor/doctor_update/<int:pk>/', UpdateDoctor.as_view(),name='update-doctor'),
    path('api/doctor/doctor_delete/<int:doctor_id>/', DeleteDoctor.as_view(),name='doctor-delete'),
    # path('api/doctor/update_doctor/',)
    
    #patient
    path('api/patient/get_patient/',ListPatientView.as_view(), name='patient-list'),
    path('api/patient/get_patient_detail/<int:pk>/', PatienteDetailView.as_view(), name='patient-get'),
    path('api/patient/add_patient/',AddPatient.as_view(), name='add-patient'),
    path('api/patient/patient_update/<int:pk>/', UpdatePatient.as_view(),name='update-patient'),
    path('api/patient/patient_delete/<int:pk>/', PatientDelete.as_view(),name='patienr-delete'),
    
    #token
    path('api/token/login', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/register/',RegisterUserTokenView.as_view(), name='register'),
    
    #article
    path('api/article/get_article/',ListArticleView.as_view(), name='article-list'),
    path('api/article/get_article_detail/<int:pk>/',ArticleDetailView.as_view(), name='article-detail'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)