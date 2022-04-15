
"""
Module is used to handle the course details 
"""
import pandas as pd
from logger import logging
from inueron_detail_scrapper import CourseDetailScrapper


class CourseHandler:
    """
        Class is used to handle the Course Details
    """

    inueron_infos = []

    def add_course_details(self,course,category,subject,description,learn,timing,course_feature,requirements,curriculum,mentors) -> None:
        """
            Add Course Details

             Parameters:
                course : Course 
                category : Course Category
                subject : Course Sub Category 
                description :  Subject description 
                learn : What you learn 
                timing : Course timing 
                course_feature : Feature's in the course 
                requirements : basic requirements needed in the course
                curriculum : course curriculum
                mentors : Mentor names

            
            Returns:
             list of course details
        """
        try:

            inueron_info = {}
            inueron_info['courses'] = course
            inueron_info["categories"]= category
            inueron_info["subject"]=  subject
            inueron_info["descriptions"]= description
            inueron_info["learn"] = learn
            inueron_info["timing"]= timing
            inueron_info["course_features"]= course_feature
            inueron_info["requirements"]= requirements
            inueron_info["curriculum"] = curriculum
            inueron_info["mentors"]= mentors
            self.inueron_infos.append(inueron_info)

        except Exception as ex:
            logging.error(ex)
        
    
    def get_course_details(self) -> list:
        """
            Get the course information

             Parameters:
                None
            
            Returns:
             list of course details
        """
        return self.inueron_infos
    
    def get_frame(self) -> pd.DataFrame:
        """
            Convert the course in to dataframe 

            Parameters: 
                None
            
            Returns:
             dataframe details

        """
        try:

            df = pd.DataFrame(self.inueron_infos)
            return df
        except Exception as ex:
            logging.error(ex)
            
        return None




