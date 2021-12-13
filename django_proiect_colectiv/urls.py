"""django_proiect_colectiv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from back_end.views import *

from django.conf.urls.static import static
from django.conf import settings

from back_end.views.reviewViews import ReviewList


urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', CourseList.as_view()),
    path('courses/<int:pk>/', CourseDetail.as_view()),
    path('mycourses/', MyCourses.as_view()),
    path('courses/<int:courseId>/tutorials', TutorialList.as_view()),
    path('courses/create', AddCourseView.as_view()),
    path('tutorials/<int:tutorialID>/comments', CommentList.as_view()),
    path('courses/<int:courseId>/reviews', ReviewList.as_view()),
    path('courses/create/<int:courseId>/quiz', AddQuiz.as_view()),
    path("", include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
