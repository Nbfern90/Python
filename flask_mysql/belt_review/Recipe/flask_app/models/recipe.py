from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from flask import flash


class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.under_30 = data['under_30']
        self.instructions = data['instructions']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.empty = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipe;"

        results = connectToMySQL('recipe').query_db(query)
        recipe = []

        for i in results:
            recipe.append(cls(i))
        return recipe

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM recipe LEFT JOIN user on recipe.user_id = user.id WHERE recipe.id = %(id)s"
        results = connectToMySQL('recipe').query_db(query, data)
        recipe = cls(results[0])
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
            recipe.empty.append(user.User(new_user))
        return recipe

    @classmethod
    def get_recipe_with_users(cls):
        query = "SELECT * FROM recipe LEFT JOIN user on recipe.user_id = user.id;"
        results = connectToMySQL('recipe').query_db(query)
        return results

    @classmethod
    def save(cls, data):
        query = "INSERT INTO recipe(name,description,under_30,instructions,created_at,updated_at,user_id) VALUES(%(name)s,%(description)s,%(under_30)s,%(instructions)s,NOW(),NOW(), %(user_id)s )"

        return connectToMySQL('recipe').query_db(query, data)

    @classmethod
    def edit(cls, data):
        query = "UPDATE recipe SET name=%(name)s, description=%(description)s, under_30=%(under_30)s, instructions=%(instructions)s, updated_at=NOW() WHERE id= %(id)s"

        return connectToMySQL('recipe').query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM recipe WHERE id = %(id)s;"
        return connectToMySQL('recipe').query_db(query, data)

    @staticmethod
    def validate_recipe(recipe):
        is_valid = True

        if not recipe['name']:
            flash('Name is Required')
            is_valid = False
        elif len(recipe['name']) < 3:
            flash('Name must be at least 3 characters')
            is_valid = False

        if not recipe['description']:
            flash('Description is Required')
            is_valid = False
        elif len(recipe['description']) < 3:
            flash('Description must be at least 3 characters')
            is_valid = False

        if not recipe['under_30']:
            flash('Under 30 min. is Required')
            is_valid = False
        elif len(recipe['under_30']) < 3:
            flash('Under 30 min. must be at least 3 characters')
            is_valid = False

        if not recipe['instructions']:
            flash('Instructions is Required')
            is_valid = False
        elif len(recipe['instructions']) < 3:
            flash('Instructions must be at least 3 characters')
            is_valid = False

        return is_valid
