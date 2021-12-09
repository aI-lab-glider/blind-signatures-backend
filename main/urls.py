"""BlindSignatrueAPI URL Configuration

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
from django.urls import path

import controllers.test_controller
import controllers.polls_controller
import controllers.users_controller

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', controllers.test_controller.test_endpoint, name='test_endpoint'),
    path('polls/', controllers.polls_controller.polls, name='polls'),
    path('polls/<int:id_arg>', controllers.polls_controller.polls_by_id, name='polls_by_id'),
    path('polls/<int:id_arg>/questions', controllers.polls_controller.questions_by_id, name='questions_by_id'),
    path('verify', controllers.polls_controller.verify, name='verify'),
    path('login', controllers.users_controller.login, name='login'),
    path('register', controllers.users_controller.register, name='register'),
    path('delete', controllers.users_controller.delete, name='delete')
]
