""""
    Module is used to save the courses to mongodb 
"""
import json
import pymongo
from  logger import logging
from bson import json_util


class MongoDBHandler:
    """"
        Class is used to interact with the Monogb database
    """
    def __init__(self) -> None:
        self.__client =  pymongo.MongoClient("mongodb+srv://admin:admin123@cluster0.tsqtv.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        self.db = self.__client["ineuron"]
        self.collection = self.db['courses']

    def save_courses(self,courses_dict : list) -> bool:
        """
            Save the course details to the database

            Parameters:
                courses_dict : All courses and its details in dictionary
            
            Returns:
             True or False based on the result

        """
        isSurcess = True
        try:
            self.collection.insert_many(courses_dict)
            logging.info("Sucessfully saved to database")
        except Exception as ex:
            isSurcess = False
            logging.error(ex)
            
        return isSurcess


    def parse_json(self,data):
        """
            Utility function to convert the datato json

            Parameters:
              Result set from Mongodb

            Returns:
             Json converted results
        """
        return json.loads(json_util.dumps(data))

    
    def get_courses(self) -> list:
        """
            Get the ineuron courses details

             Parameters:
                None
            
            Returns:
             list of course details
        """
        try:
            db = self.__client["ineuron"]
            result = db.courses.find({})
            result = self.parse_json(list(result))
            return list(result)
        except Exception as ex:
            logging.error(ex)
        finally:
            pass

     