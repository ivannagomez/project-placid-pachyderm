import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)



# variables
class Hobby:
    def __init__(self, img_url, title, description):
        self.img_url = img_url
        self.title = title
        self.description = description


my_hobbies = [Hobby('https://picsum.photos/id/217/200/300', 'title1', 'description1'),
                Hobby('https://picsum.photos/id/27/200/300', 'title2', 'description2'),
                Hobby('https://picsum.photos/id/237/200/300', 'title3', 'description3') ]

class Education:
    def __init__(self, school_name, grad_year, description):
        self.school_name = school_name
        self.grad_year = grad_year
        self.description = description

my_education = [Education('Current School', 'Graduation year', 'brief  description of your program of study, major and the like... Est iure fugit in nulla officia hic delectus quia qui veniam voluptas vel consequuntur placeat qui esse dignissimos aut tempora laudantium! Aut repellat doloremque aut quod dolores ut repellat iusto quo nihil aperiam ut animi maxime et quia dolor.'),
                Education('Previous School', 'Graduation year', 'brief  description of your program of study, major and the like... Est iure fugit in nulla officia hic delectus quia qui veniam voluptas vel consequuntur placeat qui esse dignissimos aut tempora laudantium! Aut repellat doloremque aut quod dolores ut repellat iusto quo nihil aperiam ut animi maxime et quia dolor.')]

class Experience:
    def __init__(self, experience_name, description):
        self.experience_name = experience_name
        self.description = description

my_experiences = [Experience('Title1', 'description of your working experience... Est iure fugit in nulla officia hic delectus quia qui veniam voluptas vel consequuntur placeat qui esse dignissimos aut tempora laudantium! Aut repellat doloremque aut quod dolores ut repellat iusto quo nihil aperiam ut animi maxime et quia dolor.'),
                 Experience('Title2', 'description of your working experience... Est iure fugit in nulla officia hic delectus quia qui veniam voluptas vel consequuntur placeat qui esse dignissimos aut tempora laudantium! Aut repellat doloremque aut quod dolores ut repellat iusto quo nihil aperiam ut animi maxime et quia dolor.')]

my_additional_experiences = [Experience('Title1', 'description of volunteer work, hackathons etc... Est iure fugit in nulla officia hic delectus quia qui veniam voluptas vel consequuntur placeat qui esse dignissimos aut tempora laudantium! Aut repellat doloremque aut quod dolores ut repellat iusto quo nihil aperiam ut animi maxime et quia dolor.'),
                            Experience('Title2', 'description of volunteer work, hackathons etc... Est iure fugit in nulla officia hic delectus quia qui veniam voluptas vel consequuntur placeat qui esse dignissimos aut tempora laudantium! Aut repellat doloremque aut quod dolores ut repellat iusto quo nihil aperiam ut animi maxime et quia dolor.')]


class Project:
    def __init__(self, img_url, title, description):
        self.img_url = img_url
        self.title = title
        self.description = description

my_projects = [Project('https://picsum.photos/id/17/200/300','project title1', 'project title1'),
                Project('https://picsum.photos/id/200/200/300','project title2', 'project title2'),
                Project('https://picsum.photos/id/110/200/300','project title3', 'project title3')]

@app.route('/')
@app.route('/index.html')
def index():
   return render_template('index.html', title="About Me", firstname="First", lastname="Last", url=os.getenv("URL"))

@app.route('/hobbies.html')
def hobbies():
    return render_template('hobbies.html', hobbies=my_hobbies)


@app.route('/experiences.html')
def experiences():
    return render_template('experiences.html', education=my_education, experiences=my_experiences, add_experiences=my_additional_experiences, title="My Experiences")

@app.route('/projects.html')
def projects():
    return render_template('projects.html', projects=my_projects)

# start the development server using the run() method
if __name__ == "__main__":
    app.run(debug=True)
