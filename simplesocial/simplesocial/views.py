from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name='index.html'


class testpage(TemplateView):
    template_name='test.html'

class thankspage(TemplateView):
    template_name='thanks.html'