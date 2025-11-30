from django.contrib import admin
from .models import ModelMember

class MemberAdmin(admin.ModelAdmin):
    list_display = ('__str__','codeforces_id', 'org')
    search_fields = ('ho', 'ten', 'codeforces_id')
admin.site.register(ModelMember, MemberAdmin)