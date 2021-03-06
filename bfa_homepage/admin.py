from django.contrib import admin

from .models import *

class HomepageSpotlightLinkAdmin(admin.ModelAdmin):
    class Meta:
        model = HomepageSpotlightLink
admin.site.register(HomepageSpotlightLink, HomepageSpotlightLinkAdmin)

class HomepageLearnMoreLinkAdmin(admin.ModelAdmin):
    class Meta:
        model = HomepageLearnMoreLink
admin.site.register(HomepageLearnMoreLink, HomepageLearnMoreLinkAdmin)

class HomepageTestimonialAdmin(admin.ModelAdmin):
    class Meta:
        model = HomepageTestimonial
admin.site.register(HomepageTestimonial, HomepageTestimonialAdmin)

class HomepagePhotosAdmin(admin.ModelAdmin):
    class Meta:
        model = HomepagePhotos
admin.site.register(HomepagePhotos, HomepagePhotosAdmin)

class TeamPageTeamMemberAdmin(admin.ModelAdmin):
    class Meta:
        model = TeamPageTeamMember
admin.site.register(TeamPageTeamMember, TeamPageTeamMemberAdmin)