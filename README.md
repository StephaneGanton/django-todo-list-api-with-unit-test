# django-todo-list-api-with-unit-test
A project to develop a **todolist API** in order to go through the main basics of `Django and Django Rest Framework`

## Motivation

This project is part of a serie of projects we build to get dive into **Django web Framework**.
It was originally devoloped by [Cryce Truly](https://www.youtube.com/watch?v=zpz5OeNKUug&list=PLx-q4INfd95FWHy9M3Gt6NkUGR2R2yqT8)

## Keys Takeaways

Going through this projects helps us understand:   
    
- Customize **User Model** to register and login by **email**
- Unit test using [Coverage](https://coverage.readthedocs.io/en/7.2.3/)
- **JWT** authentication
- APIView, GenericAPIView
- API Pagination
- Test API views (native test)
- [drf-yasg](https://drf-yasg.readthedocs.io/en/stable/) for **API documentation**


## Deployment

To launch this project after cloning it, run:

- Create and activate a virtual environment:
    
```bash
    virtualenv <name>

    source <name>/bin/activate
```

- Install dependencies:
    ```bash
        pip install -r requirements.txt
    ```
- Run migrations:
```bash
    python manage.py makemigrations 

    python manage.py migrate 
```
- Run server:
```bash
    python manage.py runserver
```


