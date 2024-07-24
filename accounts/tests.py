from django.test import TestCase

# Create your tests here.
from .models import CustomUser

user = CustomUser(email='user@example.com', fullname='Full Name')
user.set_password('password123')
user.save()
