"""
    This module is responsible for inueron course scrapper main page
"""

from asyncio.log import logger
from logger import logging
from collections import defaultdict
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
from inueron_course_handler import CourseHandler
from inueron_detail_scrapper import CourseDetailScrapper
from mongodb_handler import MongoDBHandler

from util import to_json,get_page,get_page_html


class InueronCourseScrapper:
    """
        Class used scrap the main course
    """
    def __init__(self, url) -> None:
        self.base_url = url
    
    def build_category_subcategory(self,course_categories:dict) -> dict:
        """
            Get the course information

             Parameters:
                None
            
            Returns:
             list of course details
        """

        cate_sub = {}

        try:

            for item in course_categories.keys():
                #print(item)
                cate_sub[course_categories[item]['title']] = []
                subCategory = course_categories[item]['subCategories']
                for sub in subCategory.keys():
                    cate_sub[course_categories[item]['title']].append(subCategory[sub])
           # print("*******")
            #print(cate_sub)
                
        except Exception as ex:
            logging.error(ex)            

        return cate_sub
        
    def get_course_base_info(self, courses, cat) -> str:
        """
            Get the course information using category id

             Parameters:
                course tag and cat
            
            Returns:
             Course base information
        """

        
        master_key = None

        try:
            for key, value in courses.items():
                
                if cat['id'] == value['categoryId']:
                    
                    master_key = key
                    break

        except Exception as ex:
            logging.error(ex)
        
        return master_key

    def get_course_details_url(self,base_url):
        """
            Get the course details from the url

             Parameters:
                url parameters
            
            Returns:
             base url
        """

        try:
            base_replace_space = base_url.replace(" ", "-")
            root_url =  f"https://courses.ineuron.ai/{base_replace_space}"
            return root_url
        except Exception as ex:
            logger.error(ex)

    def scrap(self):
        try:

            homePage =  get_page(self.base_url)
            homt_page_html = get_page_html(homePage)
            info = homt_page_html.body.script.string
            info_dict = to_json(info)
            course_categories = info_dict["props"]["pageProps"]["initialState"]["init"]["categories"]
            courses = info_dict["props"]["pageProps"]["initialState"]["init"]["courses"]

            course_subcategory  = self.build_category_subcategory(course_categories)
                    

            course_handler = CourseHandler()
            i = 0
            for id, sub_cate in course_subcategory.items():
                print(i)
                i = i+1
                print(id)
                for cat in sub_cate:
                    try:
                        base_info = self.get_course_base_info(courses, cat)
                        course_details_root_url = self.get_course_details_url(base_info)
                        detailScrapper = CourseDetailScrapper(course_details_root_url,base_info)
                        print("base info")
                        subject,description,learn,timing,course_feature,requirements,curriculum,mentors = detailScrapper.get_info()
                        course_handler.add_course_details(id, cat['title'],subject,description,learn,timing, course_feature, requirements, curriculum, mentors)
                        #break
                    except Exception as ex:
                        print(ex)
                #break
            print("******")
            courses_dict = course_handler.get_course_details()
            print(courses_dict)

            db = MongoDBHandler()
           # db.save_courses(courses_dict=courses_dict)
            df = course_handler.get_frame()
            #print(df)
            df.to_csv("c1.csv")
            db.save_courses(courses_dict=courses_dict)
        except Exception as ex:
            logger.error(ex)

 

scrapper = InueronCourseScrapper("https://courses.ineuron.ai/")
scrapper.scrap()