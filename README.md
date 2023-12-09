
# Django Blog Website

The Simple Django Blog is a basic web application designed to facilitate blogging and content creation. It leverages the Django framework, a powerful Python web framework, to provide an intuitive and user-friendly interface for managing and publishing blog posts. This project aims to empower users to share their thoughts, ideas, and expertise with others through the creation of engaging blog content.


## Project Overview

The project's database includes the following four tables:

- **Users:** This table contains all the users of this blog and also contains their names and emails.

- **Posts:** This table contains all the posts on this blog. It also contains the title, content, category of the post, the names of those who published the post, and the date of publication.

- **Categories:** This table contains the most popular categories that help the user determine the category of post he would like to publish.

- **Comments:** Of course, when publishing any post, there will be comments, so this table was created, which contains the name of the post, the username, and the content of the comment.


## Admin panel 

![img.png](img.png)

## Installation

1. Install Django:

   ```bash
   pip install Django
 
2. Create Django Project:

   ```bash
   django-admin startproject BlogWebsite
 
3. Create App:
   ```bash
   python manage.py startapp blog

4. Apply database migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate

5. Create a superuser account to access the admin panel:

   ```bash
   python manage.py createsuperuser

6. Start the development server:

   ```bash
    python manage.py runserver
   
## Usage

The project should now be running locally at http://localhost:8000/. You can access the admin panel at http://localhost:8000/admin/  .

1. Home page :
http://127.0.0.1:8000/




2. Base Page :
http://127.0.0.1:8000/base/




3. Users Page :
http://127.0.0.1:8000/users/

![img_3.png](img_3.png)


4. Blogs Page :
http://127.0.0.1:8000/blogs/




5. Comments Page :
http://127.0.0.1:8000/comments/




6. Categories Page :
http://127.0.0.1:8000/categories/




7. blog details Page :
http://127.0.0.1:8000/blogdetails/2/



## Dependencies

The main libraries and packages used in this project include:

    Django framework :  is a Python framework that makes it easier to create web sites using Python.






