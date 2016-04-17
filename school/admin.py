from django.contrib import admin
from .models import *

# Register your models here.
class KidAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'team', 'school')
    search_fields = ('team', )
    list_filter = ('team', )

    def school(self, instance):
        return instance.team.school

class TeamAdmin(admin.ModelAdmin):
    list_display = ('team_name', 'school')
    search_fields = ('team_name', 'school')
    list_filter = ('team_name', 'school')

class LeaderAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'team', 'school')
    search_fields = ('team', )
    list_filter = ('team', )

class BitacoraAdmin(admin.ModelAdmin):
    list_display = ('kid_name', 'date')
    search_fields = ('kid__first_name', 'date')
    list_filter = ('kid__first_name', 'date')

    def kid_name(self, instance):
        return instance.kid.first_name

admin.site.register(Kid, KidAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Leader, LeaderAdmin)
admin.site.register(Bitacora, BitacoraAdmin)