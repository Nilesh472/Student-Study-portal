
from django.urls import path

from dashboard.models import Category
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index,name='index'),
    path('home/', views.home,name='home'),
    path('Category', views.category, name='Category'),
    path('Question/<int:pk>/', views.question, name='Question'),
    path('Result/', views.result, name='result'),
    path('Reference/<str:pk>/', views.reference, name='reference'),
    path('Academic', views.academic, name='Academic'),
    path('<int:pk>', views.subject, name='subject')
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)