import sqlite3 as sql
from actor import Actor, GENDERS, ALIGNMENTS


class World:
    def __init__(self, database):
        self.database = database
        self._player_actor_id = None

    def sql_query(self, query_string, parameters=()):
        with sql.connect(self.database) as conn:
            c = conn.cursor()
            c.execute(query_string, parameters)
            return c.fetchall()

    def query_to_actor(self, query, parameters):
        query_result = self.sql_query(query, parameters)
        (actor_id, name, image, gender, alignment, location, health_per, energy_per,
         strength_tier, strength_rank, power_tier, power_rank, speed_tier, speed_rank,
         brawl_tier, brawl_rank, accuracy_tier, accuracy_rank, toughness_tier,
         toughness_rank) = query_result[0]
        gender = GENDERS[gender]
        alignment = ALIGNMENTS[alignment]
        return Actor(actor_id, name, image, gender, alignment, location, health_per, energy_per,
                     strength_tier, strength_rank, power_tier, power_rank, speed_tier, speed_rank,
                     brawl_tier, brawl_rank, accuracy_tier, accuracy_rank, toughness_tier,
                     toughness_rank)

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

    @property
    def player_actor(self):
        return self.get_actor_by_id(self._player_actor_id)

    @player_actor.setter
    def player_actor(self, value):
        self._player_actor_id = value.actor_id

    def set_player_actor_id(self, value):
        self._player_actor_id = value


def set_world(w):
    world.database = w


world = World('database.db')
