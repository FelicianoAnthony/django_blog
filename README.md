# Django Blog -- How to start your own 

> virtualenv venv -p python3 && source venv/bin/activate && cd django_blog &&  pip install -r requirements.txt


> python manage.py migrate blog 


> python manage.py migrate blog 


> python manage.py createsuperuser
	- login to 127.0.0.1:800/admin add a new post to Posts group  


> python manage.py runserver 127.0.0.1:8000	



### http://127.0.0.1:8000/	-- see all posts 

![alt text](screenshots/post_list.png)




### http://127.0.0.1:8000/post/new	-- form to create new post

![alt text](screenshots/post_new.png)



### http://127.0.0.1:8000/post/2/edit/		-- if post exists

![alt text](screenshots/post_edit.png)



### http://127.0.0.1:8000/post/2/  -- doesn't work yet 

##### https://tutorial.djangogirls.org/en/django_forms/

