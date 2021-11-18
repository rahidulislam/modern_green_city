from django.shortcuts import redirect, render
from django.views.generic import TemplateView,FormView
from core.models import OurTeam, Slider, Testimonial
from property.models import LandType, Land
from property.forms import AddLandQueryForm
from django.contrib import messages
# Create your views here.

class HomeView(TemplateView, FormView):
    template_name ='core/index.html'
    form_class = AddLandQueryForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        land_types = LandType.objects.all().order_by('-id')[:5]
        context["land_types"] = land_types
        context["lands"] = Land.objects.filter(land_type__in = land_types)
        context["hero_sliders"] = Slider.objects.all().order_by('-id')[:5]
        context["our_teams"] = OurTeam.objects.all()[:3]
        context["testimonials"] = Testimonial.objects.all().order_by('-id')[:4]
        return context
    
    def post(self, request):
        form = AddLandQueryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your query is submited successfully')
        return redirect('core:home')



    