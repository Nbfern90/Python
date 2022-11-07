from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.password = data['password']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM user"
        results = connectToMySQL('recipe').query_db(query)
        users = []

        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def save(cls, data):
        query = "INSERT INTO user(first_name,last_name,password,email,created_at,updated_at) VALUES(%(first_name)s,%(last_name)s,%(password)s,%(email)s,NOW(),NOW())"
        return connectToMySQL('recipe').query_db(query, data)

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM user WHERE email = %(email)s;"
        result = connectToMySQL('recipe').query_db(query, data)

        if len(result) < 1:
            return False
        return cls(result[0])

    @staticmethod
    def validate_user(user):
        is_valid = True
        query = "SELECT * FROM user WHERE email = %(email)s;"
        results = connectToMySQL('recipe').query_db(query, user)
        if len(results) >= 1:
            flash("Email already exists; choose another")
            is_valid = False
        if len(user['first_name']) == 0:
            flash("First name required.")
            is_valid = False
        elif len(user['first_name']) < 3:
            flash("First name must be greater than 3 characters.")
            is_valid = False
        if len(user['last_name']) == 0:
            flash('Last name required.')
            is_valid = False
        elif len(user['last_name']) < 3:
            flash("Last name must be greater than 2 characters")
            is_valid = False
        if len(user['password']) == 0:
            flash("Password required")
            is_valid = False
        elif len(user['password']) < 8:
            flash("Password must be at Least 8 characters")
            is_valid = False
        if user['password'] != user['confirm_password']:
            flash("Passwords don't match")
            print(user)
        if len(user['confirm_password']) == 0:
            flash("Please confirm password")
            is_valid = False
        if len(user['email']) == 0:
            flash('Email required')
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid Email")
            is_valid = False

        return is_valid
