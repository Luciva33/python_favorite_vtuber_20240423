from django.contrib import admin
from .models import MOffices, MVtuberTags, MVtubers, MVtubersProfiles, MFavoriteVideoTags, MUsers, TFavoriteVtubers, TFavoriteVideos

# Register your models here.
admin.site.register(MOffices)
admin.site.register(MVtuberTags)
admin.site.register(MVtubers)
admin.site.register(MVtubersProfiles)
admin.site.register(MFavoriteVideoTags)
admin.site.register(MUsers)
admin.site.register(TFavoriteVtubers)
admin.site.register(TFavoriteVideos)