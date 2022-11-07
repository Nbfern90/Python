from mysqlconnection import connectToMySQL


class Peeps:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM people;"
        results = connectToMySQL('peeps').query_db(query)

        peeps = []

        for i in results:
            peeps.append(cls(i))
        return peeps

    @classmethod
    def save(cls, data):
        query = "INSERT INTO people(first_name,last_name,email,created_at,updated_at) VALUES(%(first_name)s,%(last_name)s,%(email)s,NOW(),NOW());"
        result = connectToMySQL('peeps').query_db(query, data)
        return result

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM people WHERE id = %(id)s"

        result = connectToMySQL('peeps').query_db(query, data)
        return cls(result[0])

    @classmethod
    def edit(cls, data):
        query = "UPDATE people SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s,updated_at=NOW() WHERE id = %(id)s"
        return connectToMySQL('peeps').query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM people WHERE id = %(id)s"
        return connectToMySQL('peeps').query_db(query, data)
