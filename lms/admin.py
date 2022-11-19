from django.contrib import admin

# Register your models here.
from lms.models import Curator, Direction, Disciplina, Group, Student

admin.site.register(Curator)
admin.site.register(Direction)
admin.site.register(Disciplina)
admin.site.register(Group)
admin.site.register(Student)
