# API Workshop

In this workshop the API will be modulerized into a basic file structure. 

```
Project/
    main.py
    requirements.txt
    api/
        __init__.py
        
        movies/
            __init__.py
            models.py
            routes.py
            controllers.py

        admin/
           __init__.py
           admin.py
       
        accounts/
            __init__.py
            models.py
            routes.py
            controllers.py        
    
    common/
        __init__.py
        utils.py
        config.py
        security.py
        
```
This file structure is basic and meets our needs for the scope of this project, but it should also be scalable.
