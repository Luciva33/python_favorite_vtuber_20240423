# Generated by Django 5.0.4 on 2024-04-30 14:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MFavoriteVideoTags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=30)),
                ('tag_name', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'm_favorite_video_tags',
            },
        ),
        migrations.CreateModel(
            name='MOffices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('office_name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'm_offices',
            },
        ),
        migrations.CreateModel(
            name='MUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'm_users',
            },
        ),
        migrations.CreateModel(
            name='MVtubers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ja', models.CharField(max_length=30)),
                ('name_en', models.CharField(blank=True, max_length=30, null=True)),
                ('image_filename', models.CharField(max_length=20)),
                ('thumbnail_filename', models.CharField(max_length=20)),
                ('catch_text', models.TextField(blank=True, null=True)),
                ('introduction_video_url', models.CharField(blank=True, max_length=150, null=True)),
                ('youtube_url', models.CharField(max_length=150)),
                ('twitter_url', models.CharField(max_length=150)),
                ('recommended_video1', models.CharField(blank=True, max_length=150, null=True)),
                ('recommended_video2', models.CharField(blank=True, max_length=150, null=True)),
                ('recommended_video3', models.CharField(blank=True, max_length=150, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('office', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='favorite_vtuber_app.moffices')),
            ],
            options={
                'db_table': 'm_vtubers',
            },
        ),
        migrations.CreateModel(
            name='MVtubersProfiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('vtuber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='favorite_vtuber_app.mvtubers')),
            ],
            options={
                'db_table': 'm_vtubers_profiles',
            },
        ),
        migrations.CreateModel(
            name='MVtuberTags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=30)),
                ('tag_name', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('office', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='favorite_vtuber_app.moffices')),
            ],
            options={
                'db_table': 'm_vtuber_tags',
            },
        ),
        migrations.AddField(
            model_name='mvtubers',
            name='tag1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tag1_vtubers', to='favorite_vtuber_app.mvtubertags'),
        ),
        migrations.AddField(
            model_name='mvtubers',
            name='tag2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tag2_vtubers', to='favorite_vtuber_app.mvtubertags'),
        ),
        migrations.CreateModel(
            name='TFavoriteVideos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_url', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('tag1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tag1_videos', to='favorite_vtuber_app.mfavoritevideotags')),
                ('tag2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tag2_videos', to='favorite_vtuber_app.mfavoritevideotags')),
                ('tag3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tag3_videos', to='favorite_vtuber_app.mfavoritevideotags')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='favorite_vtuber_app.musers')),
                ('vtuber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='favorite_vtuber_app.mvtubers')),
            ],
            options={
                'db_table': 't_favorite_videos',
            },
        ),
        migrations.CreateModel(
            name='TFavoriteVtubers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='favorite_vtuber_app.musers')),
                ('vtuber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='favorite_vtuber_app.mvtubers')),
            ],
            options={
                'db_table': 't_favorite_vtubers',
                'unique_together': {('user', 'vtuber')},
            },
        ),
    ]
