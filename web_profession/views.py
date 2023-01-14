from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from web_profession.models import AboutParagraph, YearStats, ImageStat, CitySal, CityFract


# Create your views here.

class MainView(ListView):

    model = AboutParagraph
    template_name = 'main.html'


class DemandView(TemplateView):

    template_name = 'demand.html'

    def get_context_data(self, **kwargs):
        return {
            "rows": YearStats.objects.all(),
            "salary": ImageStat.objects.get(name='year_salary'),
            "count": ImageStat.objects.get(name='year_count')
        }


class GeographyView(TemplateView):

    template_name = 'geography.html'

    def get_context_data(self, **kwargs):
        return {
            "rows_sal": CitySal.objects.all(),
            "rows_fr": CityFract.objects.all(),
            "salary": ImageStat.objects.get(name="geo_salary"),
            "fraction": ImageStat.objects.get(name="geo_fract"),
        }