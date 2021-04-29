from django.db import models
from app_login.models import User

class Property(models.Model):
    # User inputs
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    owner = models.ForeignKey(User, related_name='properties', on_delete=models.CASCADE)
    phone = models.IntegerField()
    operated = models.BooleanField()
    non_op = models.BooleanField()
    royalty = models.BooleanField()
    operator = models.CharField(max_length=250)
    state = models.TextField()
    county = models.TextField()
    field = models.TextField()
    lease = models.TextField()
    api_list = models.FileField(upload_to='api_list/')
    comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #Admin inputs
    deliverables = models.TextField()
    deadline = models.DateField()
    description = models.TextField()
    approved = models.BooleanField()
    date_evaluation_complete = models.DateField()
    offer = models.IntegerField()
    accepted = models.BooleanField()
    active_display = models.BooleanField()

class Project(models.Model):
    # User inputs
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    phone = models.IntegerField()
    owner = models.ForeignKey(User, related_name='projects', on_delete=models.CASCADE)
    geology = models.BooleanField()
    engineering = models.BooleanField()
    field_sup = models.BooleanField()
    contract_pump = models.BooleanField()
    challenge = models.TextField()
    assist = models.TextField()
    urgent = models.BooleanField()
    start_date = models.DateField()
    completion_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #Admin inputs
    progress = models.DecimalField(max_digits=3, decimal_places=2)
    well_count = models.IntegerField()
    project_nickname = models.CharField(max_length=250)
    description = models.TextField()
    current_step = models.CharField(max_length=250)
    next_step = models.CharField(max_length=250)
    starting_date = models.DateField()
    est_completion_date = models.DateField()
    deliverables = models.TextField()
    deadline = models.DateField()
    accum_invoice = models.DecimalField(max_digits=8, decimal_places=2)
    approvals_request = models.TextField()
    actual_complete_date = models.DateField()
    active_display = models.BooleanField()

class Partner(models.Model):
    # User inputs
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    phone = models.IntegerField()
    owner = models.ForeignKey(User, related_name='partners', on_delete=models.CASCADE)
    corp_name = models.CharField(max_length=250)
    list_partners = models.TextField()
    contribute = models.IntegerField()
    describe = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #Admin inputs
    well_count = models.IntegerField()
    description = models.TextField()
    active_display = models.BooleanField()

# class Admin(models.Model):
    # project_type = models.CharField(max=250)
    # progress = models.DecimalField(max_digits=3, decimal_places=2)
    # well_count = models.IntegerField()
    # project_nickname = models.CharField(max_length=250)
    # description = models.TextField()
    # current_step = models.CharField(max_length=250)
    # next_step = models.CharField(max_length=250)
    # starting_date = models.DateField()
    # est_completion_date = models.DateField()
    # deliverables = models.TextField()
    # deadline = models.DateField()
    # accum_invoice = models.DecimalField(max_digits=8, decimal_places=2)
    # approvals_request = models.TextField()
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

#**********************************************
# The below classes are entirely input by admin though will be automated at future dates

class Lease(models.Model):
    lease_name = models.CharField(max_length=250)
    legal_description = models.TextField()
    gross_acres = models.DecimalField(max_digits=14, decimal_places=3)
    net_acres = models.DecimalField(max_digits=14, decimal_places=3)
    top_depth = models.IntegerField()
    bottom_depth = models.IntegerField()
    lease_owners = models.ManyToManyField(User, related_name='leases')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class WorkingInterest(models.Model):
    value = models.DecimalField(max_digits=11, decimal_places=10)
    lease = models.ForeignKey(Lease, related_name='working_interests', on_delete=models.CASCADE)
    owner = models.ForeignKey(User, related_name='working_interests', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class RoyaltyInterest(models.Model):
    value = models.DecimalField(max_digits=11, decimal_places=10)
    lease = models.ForeignKey(Lease, related_name='royalty_interests', on_delete=models.CASCADE)
    owner = models.ForeignKey(User, related_name='royalty_interests', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Jib(models.Model):
    date_production = models.DateField()
    bill = models.DecimalField(max_digits=8, decimal_places=2)
    lease = models.ForeignKey(Lease, related_name='jibs', on_delete=models.CASCADE)
    owner = models.ForeignKey(User, related_name='jibs', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class RunCheck(models.Model):
    date_production = models.DateField()
    date_mailed = models.DateField()
    pay = models.DecimalField(max_digits=8, decimal_places=2)
    lease = models.ForeignKey(Lease, related_name='run_checks', on_delete=models.CASCADE)
    owner = models.ForeignKey(User, related_name='run_checks', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Production(models.Model):
    lease = models.ForeignKey(Lease, related_name='production', on_delete=models.CASCADE)
    date_production = models.DateField()
    oil = models.IntegerField()
    gas = models.IntegerField()
    water = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
