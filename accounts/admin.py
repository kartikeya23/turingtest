from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from accounts.models import School
 
# Register your models here.
class SchoolInline(admin.StackedInline):
	model = School
	can_delete = False
	verbose_name_plural = 'School'

class UserAdmin(BaseUserAdmin):
	inlines = (SchoolInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)