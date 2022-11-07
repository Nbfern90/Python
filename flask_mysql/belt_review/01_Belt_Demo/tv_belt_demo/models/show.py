from tv_belt_demo.config.mysqlconnection import connectToMySQL
from flask import flash
from tv_belt_demo.models import user

class Show:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.network = data['network']
        self.release_date = data['release_date']
        self.description = data['description']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.posted_by = ''

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM shows;"
        results = connectToMySQL('tv_belt_demo_db').query_db(query) 

        shows = []

        for row_in_db in results:
            shows.append(cls(row_in_db))
        return shows

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM shows LEFT JOIN users ON shows.user_id = users.id WHERE shows.id = %(id)s;"

        results = connectToMySQL('tv_belt_demo_db').query_db(query, data)

        if not results or len(results) == 0:
            return False 
        else:
            show = cls(results[0])
            show.posted_by = results[0]['first_name'] + ' ' + results[0]['last_name']
            return show

    @classmethod
    def update_one(cls, data):
        query = "UPDATE shows SET title = %(title)s, network = %(network)s, release_date = %(release_date)s, description = %(description)s, updated_at = NOW() WHERE id = %(id)s;"

        connectToMySQL('tv_belt_demo_db').query_db(query, data)

    @classmethod
    def save(cls, data):
        query = "INSERT INTO shows (title, network, release_date, description, user_id, created_at, updated_at) VALUES (%(title)s, %(network)s, %(release_date)s, %(description)s, %(user_id)s, NOW(), NOW());"
        return connectToMySQL('tv_belt_demo_db').query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM shows WHERE id = %(id)s;"
        connectToMySQL('tv_belt_demo_db').query_db(query, data)

    @staticmethod
    def validate_show(show):
        is_valid = True 

        if not show['title']:
            flash('Title is required', 'title')
            is_valid = False
        elif len(show['title']) < 3:
            flash('Title must be at least 3 characters', 'title')
            is_valid = False

        if not show['network']:
            flash('Network is required', 'network')
            is_valid = False
        elif len(show['network']) < 3:
            flash('Network must be at least 3 characters', 'network')
            is_valid = False
            
        if not show['description']:
            flash('Description is required', 'description')
            is_valid = False
        elif len(show['description']) < 3:
            flash('Description must be at least 3 characters', 'description')
            is_valid = False

        return is_valid