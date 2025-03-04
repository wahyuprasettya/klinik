from .doctor import DoctorListCreate,DoctorDetail,DoctorDetailView,AddDoctor,ListDoctorView,DeleteDoctor,UpdateDoctor
from .patient import PatientListCreate,PatientDetail,PatienteDetailView,AddPatient,ListPatientView,UpdatePatient,PatientDelete
from .article import ArticleDetailView,ListArticleView
from .usertoken import RegisterUserTokenView
from .custom_404 import custom_404
from .custom_exception_handler import custom_exception_handler,exception_handler