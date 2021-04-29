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
    if 'user_id' not in request.session:
        messages.error(request, "Please log in to view this page.")
        return redirect('/')
    return render(request, 'dashboard.html')

def admin(request):
    if 'user_id' not in request.session:
        messages.error(request, "Please log in to view this page.")
        return redirect('/')

    return render(request, 'admin.html')

def edit_prop(request, prop_id):
    if 'user_id' not in request.session:
        messages.error(request, "Please log in to view this page.")
        return redirect('/')
        
    context = {
        'property': Property.objects.get(id=prop_id),
    }
    return render(request, 'edit_prop.html', context)

def update_prop(request, prop_id):
    prop = Property.objects.get(id=prop_id)
    prop.name = request.POST['name']
    prop.email = request.POST['email']
    prop.phone = request.POST['phone']
    prop.operated = request.POST['operated']
    prop.non_op = request.POST['non_op']
    prop.royalty = request.POST['royalty']
    prop.operator = request.POST['operator']
    prop.state = request.POST['state']
    prop.county = request.POST['county']
    prop.field = request.POST['field']
    prop.lease = request.POST['lease']
    prop.comments = request.POST['comments']
    prop.deliverables = request.POST['deliverables']
    prop.deadline = request.POST['deadline']
    prop.description = request.POST['description']
    prop.approved = request.POST['approved']
    prop.date_evaluation_complete = request.POST['date_evaluation_complete']
    prop.offer = request.POST['offer']
    prop.accepted = request.POST['accepted']
    prop.active_display = request.POST['active_display']
    messages.success(requets, 'Your update was successful.')
    return redirect(f'/superior/admin/property/{prop_id}')