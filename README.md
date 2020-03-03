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
$ pip install django -U
```

List libraries used in the current environment:
```
$ pip freeze
```

