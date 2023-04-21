# Admin

```python
python manage.py createsuperuser
```

make ID
make Email
make password

and go to **localhost:8000/admin**

login by ID, password before you make

add this in admin.py

```python
from .models import YourModel

admin.site.register(YourModel)
```

you can create, change, delete data
