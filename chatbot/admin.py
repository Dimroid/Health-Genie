# In chatbot/admin.py
from django.contrib import admin
from .models import UserQuery

admin.site.register(UserQuery)