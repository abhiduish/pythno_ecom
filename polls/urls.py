from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    
    # path('', views.index, name='index'),
    # path('<int:question_id>/', views.detail, name='detail'),
    # path('<int:question_id>/results/', views.results, name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),

    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    # path('login/', views.getName, name='getName'),
    path('contact/', views.contactForm, name='contactForm'),
    path('login/', views.loginpage, name='login'),
    # path('your-name/', views.your_name, name='your_name'),
    # path('otp_verify/', views.otpVerification, name='otpVerification')
]