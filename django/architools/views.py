#from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


from .models import TENANTLIST

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
    
    
def detail(request, TENANTLIST_id):
    return HttpResponse("You're looking at question %s." % TENANTLIST_id)


class DetailView(generic.DetailView):
    model = TENANTLIST
    template_name = 'architools/detail.html'



def results(request, id):
    response = "You're looking at the results of question id: %s."
    return HttpResponse(response % id)
    
#    
#def index(request):
#    latest_TENANTLIST_list = TENANTLIST.objects.order_by('-OS_TENANT_NAME')[:5]
#    output = ', '.join([q.OS_TENANT_NAME for q in latest_question_list])
#    return HttpResponse(output)


def index2(request):
    latest_TENANTLIST_list = TENANTLIST.objects.order_by('-OS_TENANT_NAME')[:5]
    template = loader.get_template('architools/index.html')
    context = {
        'latest_TENANTLIST_list': latest_TENANTLIST_list,
    }
    return HttpResponse(template.render(context, request))
    
    
def index(request):
    latest_TENANTLIST_list = TENANTLIST.objects.order_by('-OS_TENANT_NAME')[:5]
    context = {'latest_TENANTLIST_list': latest_TENANTLIST_list}
    return render(request, 'architools/index.html', context)    