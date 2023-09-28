# Your-Mini-Mart
It is an e-commerce website which can be used for buying  day
to day goods it is built with the help of django, HTML, CSS

# important commands
python manage.py runserver ----> to run on local host
python manage.py create superuser name_of_user ----> to create a superuser
python manage.py makemigrations ----> to save changes in model.py file
pthon manage.py migrate ----> to commit changes to your database

# how to find files
check the branches for fles all the files are stored in branches the files are below mentioned

# views.py file
It is the file in which we code diffrent functionalities of the project and then connect it to the front end of project

# templates
these are the HTML files which are used to create diffrent pages and are conneced to the views.py file and views.py switch between these templates based on the function performed
various templates in the project are
cart.html , index.html, signin.html,search_prod.html,view_product.html

# urls.py
This file is used to connect different functions in views.py to templates through specific urls

# models.py
This file is used to create a database and store the information of products,customers and cart
