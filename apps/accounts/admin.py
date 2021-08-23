from django.contrib import admin
from apps.communities import models


class CommunityMemberInline(admin.TabularInline):
    model = models.CommunityMember


admin.site.register(models.Community)
