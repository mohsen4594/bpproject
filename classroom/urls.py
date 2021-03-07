from django.contrib.auth import views as auth_views
from .import views
from django.urls import path,include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import  settings


urlpatterns = [
    path("alluploads/", views.home, name="home"),
    path("", views.homepage, name="homepage"),
    path('<int:id>', views.problem_detail, name="problem_detail"),
    path('uploads/', views.model_form_upload, name='model_form_upload'),
    path('addingvideo/', views.addingvideo, name='addingvideo'),
    path("register/", views.user_register, name="user_register"),
    path("logout/", views.logout_request, name="logout"),
    path("login/", views.login_request, name="login"),
    path('teacher_video_upload/',views.upload_video,name='teacher_video_upload'),
    path('video/<int:video_id>', views.video_detail, name="video_detail"),
    path('document<int:id>/', views.document_details, name="document_details"),
    path('teacher_problem_upload/',views.upload_problem,name='teacher_problem_upload'),
    
]
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
#if settings.DEBUG:
    #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
