from django.db import models

# VTuber事務所
class MOffices(models.Model):
    office_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'm_offices'

# VTuberタグ情報
class MVtuberTags(models.Model):
    office = models.ForeignKey('MOffices', on_delete=models.CASCADE)
    tag = models.CharField(max_length=30)
    tag_name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'm_vtuber_tags'

# VTuber情報
class MVtubers(models.Model):
    office = models.ForeignKey('MOffices', on_delete=models.CASCADE)
    name_ja = models.CharField(max_length=30)
    name_en = models.CharField(max_length=30, blank=True, null=True)
    tag1 = models.ForeignKey('MVtuberTags', related_name='tag1_vtubers', on_delete=models.CASCADE)
    tag2 = models.ForeignKey('MVtuberTags', related_name='tag2_vtubers', on_delete=models.CASCADE, blank=True, null=True)
    image_filename = models.CharField(max_length=20)
    thumbnail_filename = models.CharField(max_length=20)
    catch_text = models.TextField(blank=True, null=True)
    introduction_video_url = models.CharField(max_length=150, blank=True, null=True)
    youtube_url = models.CharField(max_length=150)
    twitter_url = models.CharField(max_length=150)
    recommended_video1 = models.CharField(max_length=150, blank=True, null=True)
    recommended_video2 = models.CharField(max_length=150, blank=True, null=True)
    recommended_video3 = models.CharField(max_length=150, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'm_vtubers'

# VTuberプロフィール情報
class MVtubersProfiles(models.Model):
    vtuber = models.ForeignKey('MVtubers', on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'm_vtubers_profiles'

# お気に入り動画タグ情報
class MFavoriteVideoTags(models.Model):
    tag = models.CharField(max_length=30)
    tag_name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'm_favorite_video_tags'

# ユーザ情報
class MUsers(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'm_users'

class TFavoriteVtubers(models.Model):
    user = models.ForeignKey('MUsers', on_delete=models.CASCADE)
    vtuber = models.ForeignKey('MVtubers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 't_favorite_vtubers'
        unique_together = [['user', 'vtuber']]

class TFavoriteVideos(models.Model):
    user = models.ForeignKey('MUsers', on_delete=models.CASCADE)
    vtuber = models.ForeignKey('MVtubers', on_delete=models.CASCADE)
    video_url = models.CharField(max_length=50)
    tag1 = models.ForeignKey('MFavoriteVideoTags', related_name='tag1_videos', on_delete=models.CASCADE, blank=True, null=True)
    tag2 = models.ForeignKey('MFavoriteVideoTags', related_name='tag2_videos', on_delete=models.CASCADE, blank=True, null=True)
    tag3 = models.ForeignKey('MFavoriteVideoTags', related_name='tag3_videos', on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 't_favorite_videos'