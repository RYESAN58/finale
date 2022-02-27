from flask_app.config.connectToMySQL import connectToMySQL
from flask import flash

#from flask_app.models import book



class Sighting:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.location = db_data['location']
        self.what = db_data['what']
        self.date = db_data['date']
        self.number = db_data['number']
        self.User_id = db_data['User_id']
        self.reported = db_data['reported']


    #Create instance of data
    @classmethod
    def create(cls, data):
        query = "INSERT INTO `red_finale`.`sightings` (`location`, `what`, `date`, `number`, `User_id`, `reported`) VALUES (%(location)s, %(what)s, %(date)s, %(number)s, %(User_id)s, %(reported)s);"
        return connectToMySQL("red_finale").query_db(query,data)


    #retrieve all the data
    @classmethod
    def retrieve(cls):
        query = 'SELECT * FROM sightings'
        which = connectToMySQL('red_finale').query_db(query)
        numbers = []
        for i in which:
            numbers.append(cls(i))
        return numbers


    #retriever all specific data
    @classmethod
    def retrieve_by(cls, data):
        query = "SELECT * FROM sightings WHERE id = %(id)s"
        return connectToMySQL('red_finale').query_db(query, data)


    #update data
    @classmethod
    def update(cls, data):
        query = "UPDATE `red_finale`.`sightings` SET `location` = %(location)s, `what`=%(what)s, `date`= %(date)s, `number`= %(number)s, `User_id` = %(User_id)s WHERE (`id` = %(id)s);"
        return connectToMySQL('red_finale').query_db(query)


    #delete row 
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM `red_finale`.`sightings` WHERE (`id` = %(id)s);"
        return connectToMySQL('red_finale').query_db(query, data)


    @staticmethod
    def validate(user):
        is_valid = True
        if len(user['location']) < 1:
            flash("Location requiered")
            is_valid = False
        if len(user['what']) < 1:
            flash("Must say what happened")
            is_valid = False
        if len(user['date']) < 1:
            flash("Must have a date")
            is_valid = False
        if int(user['number']) < 1 :
            flash("Must have seen at least 1")
            is_valid = False
        return is_valid