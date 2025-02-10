from flask import Flask
from flask_restful import Api
from models import db
from api import UserResource
from admin import setup_admin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  # 使用 SQLite 数据库
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 初始化数据库
db.init_app(app)

# 初始化 API
api = Api(app)
api.add_resource(UserResource, '/users', '/users/<int:user_id>')

# 初始化后台管理系统
setup_admin(app)

# 创建数据库表
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)