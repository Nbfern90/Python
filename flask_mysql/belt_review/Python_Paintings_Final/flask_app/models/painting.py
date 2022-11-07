from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from flask import flash


class Painting:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.price = data['price']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.empty = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM painting;"

        results = connectToMySQL('painting').query_db(query)
        painting = []

        for i in results:
            painting.append(cls(i))
        return painting

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM painting LEFT JOIN user on painting.user_id = user.id WHERE painting.id = %(id)s"
        results = connectToMySQL('painting').query_db(query, data)
        painting = cls(results[0])
        for row in results:
            new_user = {
                'id': row['user.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'password': row['password'],
                'email': row['email'],
                'created_at': row['user.created_at'],
                'updated_at': row['user.updated_at']
            }
            painting.empty.append(user.User(new_user))
        return painting

    # @classmethod
    # def get_painting_with_users(cls):
    #     query = "SELECT * FROM painting LEFT JOIN user on painting.user_id = user.id;"
    #     results = connectToMySQL('painting').query_db(query)
    #     return results

    @classmethod
    def save(cls, data):
        query = "INSERT INTO painting(title,description,price,created_at,updated_at,user_id) VALUES(%(title)s,%(description)s,%(price)s,NOW(),NOW(),%(user_id)s)"

        return connectToMySQL('painting').query_db(query, data)

    @classmethod
    def edit(cls, data):
        query = "UPDATE painting SET title=%(title)s,description=%(description)s,price=%(price)s,updated_at=NOW() WHERE id= %(id)s"

        return connectToMySQL('painting').query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM painting WHERE id = %(id)s;"
        return connectToMySQL('painting').query_db(query, data)

    @staticmethod
    def validate_painting(painting):
        is_valid = True

        if not painting['title']:
            flash('Title is Required')
            is_valid = False
        elif len(painting['title']) < 2:
            flash('Title must be at least 2 characters')
            is_valid = False

        if not painting['description']:
            flash('Description is Required')
            is_valid = False
        elif len(painting['description']) < 10:
            flash('Description must be at least 10 characters')
            is_valid = False

        if not painting['price']:
            flash('Price is Required')
            is_valid = False
        elif len(painting['price']) < 0:
            flash('Price must have a value above $0')
            is_valid = False

        return is_valid
