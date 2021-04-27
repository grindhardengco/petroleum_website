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

        if len(post_data['password']) < 8:
            errors['password_length'] = "Password must be 8 characters or more."

        if post_data['password'] != post_data['confirm_pw']:
            errors['password_confirm'] = "Password does not match password confirmation."

        return errors

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()