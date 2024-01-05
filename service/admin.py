from django.contrib import admin
from service.models import cric_stats

class CricketAdmin(admin.ModelAdmin):
    list_display=('player_name','fiftees','hundreds','wickets','average')

admin.site.register(cric_stats,CricketAdmin)