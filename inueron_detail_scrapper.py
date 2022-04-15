
""""
    Module is used to scrap the course details
"""
from asyncio.log import logger
from pickletools import read_uint1
import re
#from tkinter import E
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
from logger import logging
import json
import util

import traceback

class CourseDetailScrapper:
    """
        Course used to sracpe the course details
    """

    def __init__(self, url, base_info) -> None:
        print("url, ", url )
        self.url = url
        self.base_info = base_info
        self.page =  util.get_page(url)
        self.html = util.get_page_html(self.page)
        self.info = self.html.body.script.string
        self.json_info = json.loads(self.info)

    
    def get_header(self):
        """
            Get the course header
        """
        header = ""        
        try:

            header =  self.json_info['props']['pageProps']['data']['title']
            print(header)
            return header
        except Exception as ex:
            logging.error(traceback.format_exc())
            logging.error(ex)
        return header
            

    def get_description(self):
        """
            Get the description of the course
        """

        description = ""

        try:
            description = self.json_info['props']['pageProps']['data']['details']['description']
            return description
        except Exception as ex:
            logging.error(traceback.format_exc())
            logging.error(ex)

        return description

    def get_learn(self):
        """
            Get what you will learn details 
        """
        learn = ""
        try:
            learn =  self.json_info['props']['pageProps']['data']['meta']['overview']['learn']
            return learn
        except Exception as ex:
            logger.error("Error in learn")
            logging.error(traceback.format_exc())
            logging.error(ex)
        
        return learn
    
    def get_timing(self):
        """
            Get course timings
        """

        timings = ""
        try:
            timings = self.json_info['props']['pageProps']['initialState']['init']['courses'][self.base_info]['batches'][0]['timings']
        except Exception as ex:
            logging.error(traceback.format_exc())
            logging.error(ex)

        return timings

    def get_course_features(self):
        """
            Get course features
        """
        features = ""
        try:

            features =  self.json_info['props']['pageProps']['data']['meta']['overview']['features']
            return features
        except Exception as ex:
            logging.error(traceback.format_exc())
            logging.error(ex)

    def get_requirements(self):
        """
        Get the course requirements 
        """
        requirement = ""
        
        try:
            requirement =  self.json_info['props']['pageProps']['data']['meta']['overview']['requirements']
            return requirement

        except Exception as ex:
            logging.error(traceback.format_exc())
            logging.error(ex)

    def get_curriculum(self):
        """
            get course curriculum
        """
        course_details = []
        try:

            for course_info in self.json_info['props']['pageProps']['data']['meta']['curriculum'].values():
                name = course_info["title"] + ": " 
                for crce in course_info["items"]:
                    name += crce["title"]
                course_details.append(name)

            return course_details
        except Exception as ex:
            logging.error(traceback.format_exc())
            logging.error(ex)

    def get_mentors(self):
        """
            Get mentor information
        """
        mentor_names = []
        try:
            mentor_ids =  self.json_info['props']['pageProps']['initialState']['init']['courses'][self.base_info]['courseMeta'][0]['instructors']
            for mentor in mentor_ids:
                name =  self.json_info['props']['pageProps']['initialState']['init']['instructors'][mentor]['name']
                mentor_names.append(name)
            return mentor_names
        except Exception as ex:
            logging.error(traceback.format_exc())
            logging.error(ex)

    def get_info(self):
        """
            Combine all the reults
        """
        return self.get_header(),self.get_description(),self.get_learn(),self.get_timing(),self.get_course_features(), self.get_requirements(), self.get_curriculum(),self.get_mentors()
