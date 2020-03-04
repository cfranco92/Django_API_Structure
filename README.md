# Django_API_Structure
Django_API_Structure

---
# Preparing the work environment on Mac
We go to python.org, in the downloads section, we download the latest version and do the installation process.

Virtual environments allow ut to isolate multiple dependencies for project develpment, it can happen for example when you work with different versions of python or django.

Python 3 brings the creation and management of virtual environments as part of the core module.

```
$ python3 -m venv .env
$ source .env/bin/activate
$ deactivate
```

Install Django from the terminal:
```
$ pip3 install django -U
```

List libraries used in the current environment:
```
$ pip3 freeze
```

---
# Project creation: First Hello, world!. in Django
Validate the installed extensions:
```
$ pip3 freeze
```

Creation of the project
```
$ django-admin startproject [PROJECT_NAME] .
```

Run server
```
$ python3 manage.py runserver
```

---
# The request object
We will create more views, we will play with the different urls patterns that django allows us to have, we will review how django processes the reuqests.

Debugger:
```python
import pdb; pdb.set_trace()
```

Request atribut
* request.meta: Headers
* request.method: Methods
* request.get: Arguments received

---
# Sent arguments in the URL
We sort the numbers passed from the URL, respond to the request in JSON format and see other ways to pass arguments through the URL.

Links: 

sorted:
```
http://localhost:8000/sorted/?numbers=400,34,123,12,1,0
```
hi:
```
http://localhost:8000/hi/cristian/11/
```