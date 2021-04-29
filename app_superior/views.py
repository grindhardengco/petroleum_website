from django.shortcuts import render, redirect

def home(request):

    return render(request, 'home.html')

#Add acqisition proposal
def sell(request):
    
    return render(request, 'sell.html')

def add_property(request):
    #add form to property model ...
    return redirect('/superior/thank_property')

def thank_property(request):

    return render(request, 'thank_property.html')

#Add consulting project
def help(request):

    return render(request, 'help.html')

def add_project(request):
    #add form to property model...
    return redirect('/superior/thank_project')

def thank_project(request):

    return render(request, 'thank_project.html')

#Add partnership proposal
def partner(request):

    return render(request, 'partner.html')

def add_partner(request):
    #add form to partner model...
    return redirect('/superior/thank_partner')

def thank_partner(request):

    return render(request, 'thank_partner.html')

#Render dashboard after login
def dashboard(request):

    return render(request, 'dashboard.html')

def admin(request):

    return render(request, 'admin.html')

def edit_prop(request, prop_id):
    context = {
        'property': Property.objects.get(id=prop_id),
    }
    return render(request, 'edit_prop.html', context)
