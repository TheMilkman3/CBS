import sqlite3 as sql
from actor import Actor, GENDERS, ALIGNMENTS


class World:
    def __init__(self, database):
        self.database = database

    def sql_query(self, query_string, parameters=()):
        with sql.connect(self.database) as conn:
            c = conn.cursor()
            c.execute(query_string, parameters)
            return c.fetchall()

    def query_to_actor(self, query, parameters):
        query_result = self.sql_query(query, parameters)
        actor_id, name, image, gender, alignment, location = query_result[0]
        gender = GENDERS[gender]
        alignment = ALIGNMENTS[alignment]
        return Actor(actor_id, name, image, gender, alignment, location)

    def get_actor_by_id(self, actor_id):
        query = 'SELECT * FROM actors WHERE id=?'
        parameters = (actor_id,)
        return self.query_to_actor(query, parameters)

    def get_actor_list(self):
        query = 'SELECT id, name FROM actors ORDER BY name DESC'
        return self.sql_query(query)

    def add_actor(self, actor):
        query = 'INSERT INTO actors (name, image, gender, alignment, location) VALUES (?, ?, ?, ?, ?)'
        alignment = ALIGNMENTS.index(actor.alignment)
        gender = GENDERS.index(actor.gender)
        parameters = actor.name, actor.image, gender, alignment, actor.location
        return self.sql_query(query, parameters)

    def update_actor(self, actor):
        query = 'UPDATE actors SET name=?, image=?, gender=?, alignment=?, location=? WHERE id=?'
        alignment = ALIGNMENTS.index(actor.alignment)
        gender = GENDERS.index(actor.gender)
        parameters = actor.name, actor.image, gender, alignment, actor.location, actor.actor_id
        return self.sql_query(query, parameters)

world = World('database.db')
