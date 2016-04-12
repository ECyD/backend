from django.contrib import admin
from .models import *

# Register your models here.
class KidAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'team', 'school')
    search_fields = ('team', )

    def school(self, instance):
        return instance.team.school

class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'school')
    search_fields = ('name', 'school')


class LeaderAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'team', 'school')
    search_fields = ('team', )

admin.site.register(Kid, KidAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Leader, LeaderAdmin)