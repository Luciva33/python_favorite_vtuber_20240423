# add_data.py

import os
import django

# Djangoの設定を読み込む
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'favorite_vtuber_project.settings')
django.setup()

# データ追加に必要なモデルをインポート
from django.db import models

# データ追加の処理を記述
def add_data():
   print(models.DateTimeField(auto_now=True))

# スクリプトを実行するための条件を設定
if __name__ == '__main__':
    add_data()
