from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from django.contrib import messages

from .forms import SignUpForm

# Create your views here.  
def home(request):
    
    form = SignUpForm(request.POST or None)
    
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        messages.success(request, 'Thanks dude')
        return HttpResponseRedirect('/thank-you/')
    
    return render_to_response("signup.html", locals(),
                              context_instance=RequestContext(request))


def thankyou(request):
    
    return render_to_response("thankyou.html", locals(),
                              context_instance=RequestContext(request))

def aboutme(request):
    
    return render_to_response("aboutme.html", locals(),
                              context_instance=RequestContext(request))

def datastuff(request):
    
    return render_to_response("datastuff.html", locals(),
                              context_instance=RequestContext(request))

def bikeaccidents(request):
    
    return render_to_response("bikeaccidents.html", locals(),
                              context_instance=RequestContext(request))

def codeexplanation(request):
    
    return render_to_response("codeexplanation.html", locals(),
                              context_instance=RequestContext(request))