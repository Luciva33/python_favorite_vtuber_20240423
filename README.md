# Favorite Vtuber
Vtuverの一覧から気になる「Vtuber」を選択し、一覧で確認できる。
※2024年5月1日時点では「ホロライブ」事務所のJPのみ対応

# DEMO
![readme](https://github.com/sishikawa-rop2312/python_favorite_vtuber_20240423/assets/155729870/06e9cd1a-1ca2-4ec6-9de6-f3613f1cfaf2)

# Features
DBでキャラ情報を管理しているので、データ更新が容易。

# Requirement
* Django 5.0.4
* Python 3.12.3

# Usage
### 1.環境構築
```bash
$ git clone git@github.com:sishikawa-rop2312/python_favorite_vtuber_20240423.git

# クローンしたディレクトリに移動
$ cd python_favorite_vtuber_20240423

$ pip install virtualenv

$ virtualenv appenv

$ source appenv/Scripts/activate

# http://127.0.0.1:8000のサーバが立ち上がれば成功
$ python manage.py runserver
```

### 2.アカウント作成
```
http://127.0.0.1:8000/signup/
```
※アカウント作成後にトップにリダイレクトします

# Note
テスト未実施のため、バグ頻発する可能性大

# Author
* ishikawa
