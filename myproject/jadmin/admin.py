from django.contrib import admin
from .models import Board
from .models import Category
from .models import Clue

# Register your models here.
admin.site.register(Board)
admin.site.register(Category)
admin.site.register(Clue)