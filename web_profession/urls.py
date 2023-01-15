from django.urls import path

import web_profession.views

urlpatterns = [
    path('', web_profession.views.MainView.as_view(), name='main'),
    path('demand/', web_profession.views.DemandView.as_view(), name='demand'),
    path('geography/', web_profession.views.GeographyView.as_view(), name='geo'),
    path('skills/', web_profession.views.SkillsView.as_view(), name='skills'),
    path('latest/', web_profession.views.LatestView.as_view(), name='latest'),
]