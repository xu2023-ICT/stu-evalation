import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'database.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')  # 存 zip 包
STATIC_FOLDER = os.path.join(BASE_DIR, 'static_pages')   # 存解压后的 html 资源
