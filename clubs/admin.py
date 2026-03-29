from django.contrib import admin
from .models import Club, Membership

class MembershipInline(admin.TabularInline):
	model = Membership
	extra = 0

class ClubAdmin(admin.ModelAdmin):
	inlines = [MembershipInline]
	list_display = ('name', 'created_at')

class MembershipAdmin(admin.ModelAdmin):
	list_display = ('user', 'club', 'joined_at')

admin.site.register(Club, ClubAdmin)
admin.site.register(Membership, MembershipAdmin)
