from flask import request
from flask_restful import Resource
from models import db, User

class UserResource(Resource):
    def get(self, user_id=None):
        if user_id:
            user = User.query.get(user_id)
            if user:
                return user.to_dict(), 200
            return {"message": "User not found"}, 404
        else:
            users = [user.to_dict() for user in User.query.all()]
            return users, 200

    def post(self):
        data = request.json
        new_user = User(username=data['username'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        return new_user.to_dict(), 201

    def delete(self, user_id):
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return {"message": "User deleted"}, 200
        return {"message": "User not found"}, 404