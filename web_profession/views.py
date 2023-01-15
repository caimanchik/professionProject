from django.views.generic import TemplateView, ListView

from web_profession.models import AboutParagraph, YearStats, ImageStat, CitySal, Skill, CityLevel


# Create your views here.

class MainView(ListView):

    model = AboutParagraph
    template_name = 'main.html'


class DemandView(TemplateView):

    template_name = 'demand.html'

    def get_context_data(self, **kwargs):
        return {
            "rows": YearStats.objects.all().order_by('year'),
            "salary": ImageStat.objects.get(name='year_salary'),
            "count": ImageStat.objects.get(name='year_count')
        }


class GeographyView(TemplateView):

    template_name = 'geography.html'

    def get_context_data(self, **kwargs):
        return {
            "rows_sal": CitySal.objects.all().order_by('-salary'),
            "rows_fr": CityLevel.objects.all().order_by('-fraction'),
            "salary": ImageStat.objects.get(name="geo_salary"),
            "fraction": ImageStat.objects.get(name="geo_fract"),
        }


class SkillsView(TemplateView):

    template_name = 'skills.html'

    def get_context_data(self, **kwargs):
        years = Skill.objects.values('year').distinct().order_by('year')
        ctx = {}

        for y in years:
            ctx[y['year']] = Skill.objects.filter(year=y['year']).order_by('-count')

        return {'data': ctx}


class LatestView(TemplateView):

    template_name = 'latest.html'

    def get_context_data(self, **kwargs):
        return {
            'days': range(1, 32)
        }
