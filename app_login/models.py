from django.db import models
import re

class UserManager(models.Manager):
    def user_validator(self, post_data):
        errors = {}
       
        name_regex = re.compile(r'^[a-zA-Z]{1,}$')
        if not name_regex.match(post_data['name']):
            errors['name'] = "Name must be all letters and one more characters."

        try:
            User.objects.get(email = post_data['email'])
            errors['email_unique'] = "This email address is already in use."
        except:
            pass

        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not email_regex.match(post_data['email']):
            errors['email'] = "Email address format must be correct."

        try:
            User.objects.get(company = post_data['company'])
            errors['company_unique'] = "This company has already been registered."
        except:
            pass
        
        if len(post_data['company']) < 1:
            errors['company_name'] = "You must enter a company name."

        if len(post_data['password']) < 8:
            errors['password_length'] = "Password must be 8 characters or more."

        if post_data['password'] != post_data['confirm_pw']:
            errors['password_confirm'] = "Password does not match password confirmation."

        return errors

    def edit_validator(self, post_data, session_data):
        errors = {}
       
        name_regex = re.compile(r'^[a-zA-Z]{1,}$')
        if not name_regex.match(post_data['name']):
            errors['name'] = "Name must be all letters and one more characters."

        if post_data['email'] != session_data['email']:
            try:
                User.objects.get(email = post_data['email'])
                errors['email_unique'] = "This email address is already in use."
            except:
                pass

            email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
            if not email_regex.match(post_data['email']):
                errors['email'] = "Email address format must be correct."
        
        if post_data['company'] != session_data['company']:
            try:
                User.objects.get(company = post_data['company'])
                errors['company_unique'] = "This company has already been registered."
            except:
                pass
        
        if len(post_data['company']) < 1:
            errors['company_name'] = "You must enter a company name."

        if len(post_data['password']) == 0:
            pass
            
        elif len(post_data['password']) < 8:
            errors['password_length'] = "Password must be 8 characters or more."

        elif post_data['password'] != post_data['confirm_pw']:
            errors['password_confirm'] = "Password does not match password confirmation."

        return errors

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    password = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()