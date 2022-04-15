from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin

from inueron_course_handler import CourseHandler
from mongodb_handler import MongoDBHandler


app = Flask(__name__)

@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    mongo_handler = MongoDBHandler()
    courses = mongo_handler.get_courses()
    print(courses)
    return render_template("index.html",courses=courses)


if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
	app.run(debug=True)