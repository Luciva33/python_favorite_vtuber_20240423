# add_data.py

import os
import django

# Djangoの設定を読み込む
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'favorite_vtuber_project.settings')
django.setup()

# データ追加に必要なモデルをインポート
from favorite_vtuber_app.models import MOffices, MVtuberTags

# データ追加の処理を記述
def add_data():
    # VTuber事務所の追加
    MOffices.objects.create(id=1, office_name='ホロライブ')

    # VTuberタグの追加
    MVtuberTags.objects.bulk_create([
        MVtuberTags(id=1, office_id=1, tag='gen-0', tag_name='ホロライブ0期生'),
        MVtuberTags(id=2, office_id=1, tag='1stgen', tag_name='ホロライブ1期生'),
        MVtuberTags(id=3, office_id=1, tag='gen-2', tag_name='ホロライブ2期生'),
        MVtuberTags(id=4, office_id=1, tag='gamers', tag_name='ホロライブゲーマーズ'),
        MVtuberTags(id=5, office_id=1, tag='gen-3', tag_name='ホロライブ3期生'),
        MVtuberTags(id=6, office_id=1, tag='gen-4', tag_name='ホロライブ4期生'),
        MVtuberTags(id=7, office_id=1, tag='gen-5', tag_name='ホロライブ5期生'),
        MVtuberTags(id=8, office_id=1, tag='holox', tag_name='秘密結社holoX'),
        MVtuberTags(id=9, office_id=1, tag='regloss', tag_name='ReGLOSS'),
        MVtuberTags(id=10, office_id=1, tag='tag_office-staff', tag_name='事務所スタッフ'),
    ])

# スクリプトを実行するための条件を設定
if __name__ == '__main__':
    add_data()
