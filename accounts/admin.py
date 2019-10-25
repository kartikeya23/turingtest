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
	list_display = ('username', 'get_school', 'get_level', 'get_time')
	list_select_related = ('school', )

	def get_level(self, instance):
		return instance.school.level
	get_level.short_description = 'Level' 

	def get_school(self, instance):
		return instance.school.display_name
	get_school.short_description = 'School'

	def get_time(self, instance):
		return instance.school.time
	get_time.short_description = 'Latest'

	def get_inline_instances(self, request, obj=None):
		if not obj:
			return list()
		return super(CustomUserAdmin, self).get_inline_instances(request, obj)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)