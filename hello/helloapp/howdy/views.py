from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class homePageView(TemplateView):
	def get(self, request, **kwargs):
		return render(request, 'index.html', context=None)
		
#Add this view		
class AboutPageView(TemplateView):
	template_name = "about.html"
	
class ViewPageView(TemplateView):
	template_name = "view.html"