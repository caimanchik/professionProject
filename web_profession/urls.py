from django.urls import path

import web_profession.views

urlpatterns = [
    path('', web_profession.views.MainView.as_view(), name='main'),
    path('demand/', web_profession.views.DemandView.as_view(), name='demand'),
    path('geography', web_profession.views.GeographyView.as_view(), name='geo')
]