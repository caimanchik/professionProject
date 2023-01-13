from django.urls import path

import web_profession.views

urlpatterns = [
    path('', web_profession.views.MainView.as_view(), name='main')
]