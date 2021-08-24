# F1 Blog
Django project that acts as a social media web application for Formula 1 fans. This project is completed as final
clone project in [Python and Django Full Stack Web Developer Bootcamp](https://www.udemy.com/course/python-and-django-full-stack-web-developer-bootcamp/).
I have experimented with Django using the tutorials that course provided for the project. You can see my certificate of
completion at [this site](https://www.udemy.com/certificate/UC-78551911-caa2-438a-8993-9fb88170b74d/). 

Note that I am planning to experiment with the testing in Django as the next part for the project and add more 
functionalities over time to learn more features of the framework.

## Usage
Python 3.9 and Conda environment with dependencies as given in requirements.txt is used. To start the server, perform
following steps:

Create the conda environment and obtain the dependencies:
```
conda create --name f1-blog-env python=3.9
source activate f1-blog-env
pip install -r requirements.txt
```

Create necessary variables for settings by creating `.env` file in project root where manage.py lives in. 
Create 2 variables: 

* SECRET_KEY: for more information [use this link](https://docs.djangoproject.com/en/dev/ref/settings/#secret-key)
* DEBUG: Boolean variable

Migrate for database setup:
```
python3 manage.py migrate
```

Run the development server:
```
python3 manage.py runserver
```

## Features
Currently, F1 Blog provides following functionalities:

* Register, Login, Logout functionalities
* Ability to create community
* Ability to create post belonging to a community
* Joining and leaving communities
* Viewing posts created by users in user's page
* Viewing posts in each community in community's page

## License
[MIT](https://choosealicense.com/licenses/mit/)
