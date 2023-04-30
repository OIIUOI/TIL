# User

##### contrib

```python
django.contrib
```

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-26-21-44-39-image.png)

##### authentication

<img src="file:///C:/Users/jin47/AppData/Roaming/marktext/images/2023-04-26-21-36-17-image.png" title="" alt="" width="401">

<img src="file:///C:/Users/jin47/AppData/Roaming/marktext/images/2023-04-26-21-37-14-image.png" title="" alt="" width="499">

<img src="file:///C:/Users/jin47/AppData/Roaming/marktext/images/2023-04-26-21-37-46-image.png" title="" alt="" width="339"><img title="" src="file:///C:/Users/jin47/AppData/Roaming/marktext/images/2023-04-26-21-38-11-image.png" alt="" width="191">

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-26-21-38-52-image.png)

##### admin

<img src="file:///C:/Users/jin47/AppData/Roaming/marktext/images/2023-04-26-21-39-29-image.png" title="" alt="" width="195"><img title="" src="file:///C:/Users/jin47/AppData/Roaming/marktext/images/2023-04-26-21-39-43-image.png" alt="" width="319">

##### staticfiles

<img src="file:///C:/Users/jin47/AppData/Roaming/marktext/images/2023-04-26-21-40-46-image.png" title="" alt="" width="346"><img src="file:///C:/Users/jin47/AppData/Roaming/marktext/images/2023-04-26-21-41-06-image.png" title="" alt="" width="426">

## django.contrib.auth

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-26-21-50-55-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-26-21-51-12-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-26-21-51-32-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-26-21-51-48-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-26-21-52-12-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-26-21-52-28-image.png)

## django-allauth

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-26-21-54-03-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-26-21-52-55-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-26-21-53-18-image.png)

<img src="file:///C:/Users/jin47/AppData/Roaming/marktext/images/2023-04-26-21-54-47-image.png" title="" alt="" width="417"><img title="" src="file:///C:/Users/jin47/AppData/Roaming/marktext/images/2023-04-26-21-55-03-image.png" alt="" width="226">

<img src="file:///C:/Users/jin47/AppData/Roaming/marktext/images/2023-04-26-21-55-49-image.png" title="" alt="" width="230"><img src="file:///C:/Users/jin47/AppData/Roaming/marktext/images/2023-04-26-21-56-12-image.png" title="" alt="" width="360">

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-26-21-56-38-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-26-21-56-52-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-26-21-57-17-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-26-21-57-32-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-26-21-58-06-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-26-22-22-15-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-26-22-22-30-image.png)

```python
# models.py

from django.db import models
from django.contrib.auth.models. import AbstractUser

class User(AbstractUser):
    pass
```

```python
# setting.py
AUTH_USER_MODEL = 'app_name.User'
```

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-26-22-25-54-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-26-22-26-07-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-26-22-26-23-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-26-22-27-06-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-26-22-28-37-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-26-22-28-51-image.png)

```python
# admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# originally this is right but user is different 
admin.site.register(User)

# write this
adin.site.register(User, UserAdmin)
```

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-26-22-31-06-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-26-22-31-22-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-26-22-31-38-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-26-22-34-11-image.png)

---

# django-allauth

- [allauth 설치 가이드](https://django-allauth.readthedocs.io/en/latest/index.html)

<img title="" src="file:///C:/Users/jin47/AppData/Roaming/marktext/images/2023-04-27-07-57-12-image.png" alt="" width="236"><img title="" src="file:///C:/Users/jin47/AppData/Roaming/marktext/images/2023-04-27-07-57-32-image.png" alt="" width="325">

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-07-58-30-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-07-58-59-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-07-59-19-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-08-00-02-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-08-02-08-image.png) ![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-08-02-39-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-08-03-07-image.png) ![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-08-03-28-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-08-05-42-image.png) ![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-08-06-03-image.png)  ![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-08-06-24-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-08-09-49-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-08-29-36-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-08-30-00-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-08-31-00-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-08-31-41-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-08-32-33-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-08-35-25-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-08-35-44-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-08-36-47-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-08-37-09-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-08-37-47-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-08-38-04-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-08-38-40-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-08-38-57-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-08-42-16-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-08-42-39-image.png)

**setting.py**

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-08-53-23-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-08-54-26-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-08-54-47-image.png)

<img title="" src="file:///C:/Users/jin47/AppData/Roaming/marktext/images/2023-04-27-08-57-19-image.png" alt="" width="280"><img title="" src="file:///C:/Users/jin47/AppData/Roaming/marktext/images/2023-04-27-08-57-35-image.png" alt="" width="326">

**setting.py**    ![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-08-58-31-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-08-59-18-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-08-59-36-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-09-00-55-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-09-01-14-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-09-02-08-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-09-02-50-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-09-03-58-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-09-14-06-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-09-13-37-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-09-14-40-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-09-15-15-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-09-15-37-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-09-16-14-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-09-16-48-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-09-19-30-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-09-20-43-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-09-21-04-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-09-21-19-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-09-21-36-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-09-22-05-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-09-22-22-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-09-22-43-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-09-22-59-image.png)

```python
# admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# write this
adin.site.register(User, UserAdmin)
UserAdmin.fieldsets += ("Custom fields", {"fields" : ("nickname",)})
```

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-12-54-45-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-12-55-08-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-12-55-25-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-12-56-11-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-12-55-59-image.png)

---

# Signup Form Custom

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-12-59-13-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-13-00-14-image.png)

**forms.py**

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-13-02-26-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-13-03-04-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-13-03-26-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-13-04-08-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-14-45-08-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-14-45-24-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-13-11-44-image.png)

<img src="file:///C:/Users/jin47/AppData/Roaming/marktext/images/2023-04-27-14-46-46-image.png" title="" alt="" width="355"><img src="file:///C:/Users/jin47/AppData/Roaming/marktext/images/2023-04-27-14-47-01-image.png" title="" alt="" width="254">

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-14-47-36-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-14-48-36-image.png) ![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-14-47-56-image.png)

---

# Velidation

**setting.py**            <img src="file:///C:/Users/jin47/AppData/Roaming/marktext/images/2023-04-27-14-55-20-image.png" title="" alt="" width="172">![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-14-56-21-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-14-59-25-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-14-58-27-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-14-58-53-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-15-00-00-image.png)<img src="file:///C:/Users/jin47/AppData/Roaming/marktext/images/2023-04-27-15-00-13-image.png" title="" alt="" width="431">

---

## Password velidator

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-15-04-41-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-15-05-16-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-15-01-32-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-15-03-25-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-15-03-57-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-15-06-15-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-15-06-33-image.png)

```python
def contains_uppercase_letter(value):
    for char in value:
        if char.isupper():
            return True
    return False

def contains_lowercase_letter(value):
    for char in value:
        if char.islower():
            return True
    return False

def contains_number(value):
    for char in value:
        if char.isdigit():
            return True
    return False
```

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-15-07-02-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-15-07-19-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-15-07-37-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-15-09-07-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-15-09-24-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-15-08-16-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-15-10-24-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-15-10-42-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-15-11-06-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-15-11-24-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-15-11-44-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-15-12-08-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-15-12-25-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-15-16-03-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-15-16-38-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-15-16-57-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-15-17-41-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-15-17-54-image.png)

---

<img title="" src="file:///C:/Users/jin47/AppData/Roaming/marktext/images/2023-04-27-15-21-01-image.png" alt="" width="258"><img title="" src="file:///C:/Users/jin47/AppData/Roaming/marktext/images/2023-04-27-15-21-18-image.png" alt="" width="361">![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-15-21-52-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-15-22-08-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-15-22-44-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-15-23-12-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-15-24-58-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-15-25-13-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-15-25-29-image.png)

---

# Email velidation

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-15-40-26-image.png)

## 1. ACCOUNT_EMAIL_VERIFICATION

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-15-41-43-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-15-42-01-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-15-42-17-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-15-42-32-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-15-42-55-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-15-43-13-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-15-43-30-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-15-43-48-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-15-44-02-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-15-46-06-image.png)<img src="file:///C:/Users/jin47/AppData/Roaming/marktext/images/2023-04-27-15-46-26-image.png" title="" alt="" width="236">

Sign up and

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-15-48-02-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-15-48-42-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-15-49-51-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-15-50-40-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-15-50-56-image.png)<img title="" src="file:///C:/Users/jin47/AppData/Roaming/marktext/images/2023-04-27-15-51-14-image.png" alt="" width="256"><img title="" src="file:///C:/Users/jin47/AppData/Roaming/marktext/images/2023-04-27-15-51-29-image.png" alt="" width="304">

<img src="file:///C:/Users/jin47/AppData/Roaming/marktext/images/2023-04-27-15-52-11-image.png" title="" alt="" width="599">

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-15-52-41-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-15-52-55-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-15-53-24-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-15-53-52-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-15-54-15-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-15-58-22-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-15-58-53-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-15-59-08-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-16-04-19-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-16-00-24-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-16-00-40-image.png)

<img src="file:///C:/Users/jin47/AppData/Roaming/marktext/images/2023-04-27-16-06-02-image.png" title="" alt="" width="668">

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-16-02-40-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-16-02-55-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-16-04-35-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-16-04-50-image.png)

---

# Password

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-16-24-10-image.png)![](assets/2023-04-27-22-17-09-image.png)<img src="file:///C:/Users/jin47/AppData/Roaming/marktext/images/2023-04-27-20-00-07-image.png" title="" alt="" width="371">![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-20-00-54-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-20-01-39-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-20-02-00-image.png)<img src="file:///C:/Users/jin47/AppData/Roaming/marktext/images/2023-04-27-20-02-16-image.png" title="" alt="" width="455"><img title="" src="file:///C:/Users/jin47/AppData/Roaming/marktext/images/2023-04-27-20-02-31-image.png" alt="" width="147">![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-20-02-58-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-27-20-03-18-image.png)<img src="file:///C:/Users/jin47/AppData/Roaming/marktext/images/2023-04-27-20-03-53-image.png" title="" alt="" width="561">

![](assets/2023-04-27-22-20-23-image.png)![](assets/2023-04-27-22-21-52-image.png)![](assets/2023-04-27-22-22-08-image.png)![](assets/2023-04-27-22-22-25-image.png)<img src="assets/2023-04-27-22-23-02-image.png" title="" alt="" width="663">![](assets/2023-04-27-22-25-22-image.png)![](assets/2023-04-27-22-25-35-image.png)![](assets/2023-04-27-22-26-09-image.png)![](assets/2023-04-27-22-26-25-image.png)

![](assets/2023-04-27-22-27-54-image.png)![](assets/2023-04-29-00-44-31-image.png)![](assets/2023-04-29-00-44-52-image.png)![](assets/2023-04-29-00-45-06-image.png)![](assets/2023-04-29-00-45-33-image.png)![](assets/2023-04-29-00-47-38-image.png)![](assets/2023-04-29-00-48-00-image.png)![](assets/2023-04-29-00-48-25-image.png)

```python
# views.py
from allauth,account.views import PasswordChangeView
from django.urls import reverse

class CustomPasswordChangeView(PasswordChangeView):
    def get_success_url(self):
        return reverse("index")
```

![](assets/2023-04-29-00-49-26-image.png)![](assets/2023-04-29-00-49-41-image.png)![](assets/2023-04-29-00-49-56-image.png)![](assets/2023-04-29-00-50-13-image.png)![](assets/2023-04-29-00-50-26-image.png)

![](assets/2023-04-29-00-50-50-image.png)![](assets/2023-04-29-00-51-02-image.png)![](assets/2023-04-29-09-22-36-image.png)![](assets/2023-04-29-09-22-54-image.png)![](assets/2023-04-29-09-23-41-image.png)![](assets/2023-04-29-09-24-03-image.png)

![](assets/2023-04-29-09-27-19-image.png)

자주 사용되는 allauth URL입니다. 참고하세요!

| URL 경로                    | URL 네임                                 | 설명                                                                                                                                                                              |
| ------------------------- | -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 'signup/'                 | 'account_signup'                       | 회원가입 페이지                                                                                                                                                                        |
| 'login/'                  | 'account_login'                        | 로그인 페이지                                                                                                                                                                         |
| 'logout/'                 | 'account_logout'                       | 로그아웃 페이지 (`ACCOUNT_LOGOUT_ON_GET = True` 사용시 바로 로그아웃 됩니다. `ACCOUNT_LOGOUT_ON_GET`은 settings.py 파일에서 설정합니다. 'allauth 유용한 세팅들 정리' [노트](https://www.codeit.kr/learn/4792)를 참고하세요!) |
| 'confrim-email//'         | 'account_confirm_email'                | 이메일 인증 페이지 (`ACCOUNT_CONFIRM_EMAIL_ON_GET = True` 사용시 바로 인증 완료 됩니다.)                                                                                                            |
| 'password/change/'        | 'account_change_password'              | 비밀번호 변경 페이지                                                                                                                                                                     |
| 'password/reset/'         | 'account_reset_password'               | 비밀번호 찾기 페이지 (비밀번호 재설정 링크를 받을 이메일을 입력하는 페이지)                                                                                                                                     |
| 'password/reset/done/'    | 'account_reset_password_done'          | 비밀번호 재설정 이메일 전송 완료 페이지                                                                                                                                                          |
| 'password/reset/key//     | 'account_reset_password_from_key'      | 비밀번호 재설정 페이지 (새 비밀번호를 설정하는 페이지)                                                                                                                                                 |
| 'password/reset/key/done/ | 'account_reset_password_from_key_done' | 비밀번호 재설정 완료 페이지                                                                                                                                                                 |

`<key>`는 이메일 인증/비밀번호 재설정에 사용되는 코드입니다. 전송되는 이메일에 자동으로 포함됩니다.

allauth의 전용 세팅도 있고, 일반 django의 세팅도 있는데, allauth 전용 세팅은 모두 ACCOUNT로 시작합니다. 모든 세팅은 프로젝트의 settings.py 파일에 추가해 주시면 됩니다.

| 세팅                                                    | 값                                         | 디폴트 값                       | 설명                                                                                                                                                         |
| ----------------------------------------------------- | ----------------------------------------- | --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ACCOUNT_AUTHENTICATION_METHOD                         | "username" \| "email" \| "username_email" | "username"                  | 로그인 방법을 설정합니다. "username": 유저네임 사용, "email": 이메일 사용, "username_email": 둘 다 사용 가능                                                                           |
| ACCOUNT_CONFIRM_EMAIL_ON_GET                          | True \| False                             | False                       | True: 이메일 인증 링크를 클릭하면 바로 인증이 됩니다, False: 이메일 인증 링크를 클릭하면 인증 confirmation 페이지로 갑니다.                                                                         |
| ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL     | URL (URL 경로, URL 네임 모두 가능)                | LOGIN_URL (아래 참고)           | 로그인이 안된 상태로 인증을 완료했을 때 리디렉트되는 URL.                                                                                                                         |
| ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL | URL (URL 경로, URL 네임 모두 가능)                | LOGIN_REDICRECT_URL (아래 참고) | 로그인이 된 상태로 인증을 완료했을 때 리디렉트되는 URL.                                                                                                                          |
| ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS                | 이메일 인증 링크 만료 기간 (단위: 일)                   | 3                           | 이메일 인증 링크 만료 기간                                                                                                                                            |
| ACCOUNT_EMAIL_REQUIRED                                | True \| False                             | False                       | 회원가입 시 이메일을 꼭 입력해야 하는지를 결정합니다. True: 이메일을 꼭 입력해야 합니다, False: 이메일 필드는 옵셔널 필드입니다.                                                                            |
| ACCOUNT_EMAIL_VERIFICATION                            | "mandatory" \| "optional" \| "none"       | "optional"                  | 이메일 인증 필요 여부를 설정합니다. "mandatory": 회원가입 시 인증 이메일이 발송되고, 인증을 완료해야만 로그인을 할 수 있습니다, "optional": 회원가입 시 인증 이메일이 발송되지만, 인증이 필수는 아닙니다, "none": 인증 이메일이 발송되지 않습니다. |
| ACCOUNT_LOGIN_ATTEMPTS_LIMIT                          | 최대 로그인 실패 횟수                              | 5                           | 최대 로그인 실패 횟수                                                                                                                                               |
| ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT                        | 로그인이 잠기는 기간 (단위: 초)                       | 300                         | 로그인 시도가 ACCOUNT_LOGIN_ATTEMPTS_LIMIT을 초과하면 설정하는 시간만큼 로그인이 잠깁니다.                                                                                            |
| ACCOUNT_LOGOUT_ON_GET                                 | True \| False                             | False                       | True: 로그아웃 링크를 클릭하면 바로 로그아웃이 됩니다, False: 로그아웃 링크를 클릭하면 로그아웃 confirmation 페이지로 갑니다.                                                                         |
| ACCOUNT_LOGOUT_REDIRECT_URL                           | URL (URL 경로, URL 네임 모두 가능)                | "/"                         | 로그아웃 시 리디렉트되는 URL                                                                                                                                          |
| ACCOUNT_PASSWORD_INPUT_RENDER_VALUE                   | True \| False                             | False                       | 폼 유효성 검사를 실패할 경우, 입력했던 비밀번호가 채워진 상태로 폼이 돌아오는지를 설정합니다.                                                                                                      |
| ACCOUNT_SESSION_REMEMBER                              | None \| True \| False                     | None                        | 브라우저를 닫으면 유저를 로그아웃 시킬지를 결정합니다. None: 유저가 체크박스를 통해 선택하게 합니다, True: 브라우저를 닫아도 로그인을 유지합니다, False: 브라우저를 닫으면 유저를 로그아웃 시킵니다.                                    |
| ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE                      | True \| False                             | False                       | 회원가입시 이메일을 두 번 입력해야 하는지를 설정합니다.                                                                                                                            |
| ACCOUNT_SIGNUP_FORM_CLASS                             | 폼 클래스 (e.g. 'myapp.forms.SignupForm')     | None                        | 회원가입 페이지에서 추가 정보를 받아야 할 때, 사용할 폼 클래스를 지정해 줍니다.                                                                                                             |
| ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE                   | True \| False                             | False                       | 회원가입 시 비밀번호를 두 번 입력해야 하는지를 설정합니다.                                                                                                                          |
| ACCOUNT_SIGNUP_REDIRECT_URL                           | URL (URL 경로, URL 네임 모두 가능)                | LOGIN_REDIRECT_URL (아래 참고)  | 회원가입 성공 시 리디렉트되는 URL                                                                                                                                       |
| ACCOUNT_USERNAME_REQUIRED                             | True \| False                             | True                        | 회원가입 시 유저네임을 입력해야 하는지를 결정합니다. True: 유저네임을 입력해야 합니다, False: 유저네임을 입력받지 않습니다.                                                                                |
| LOGIN_REDIRECT_URL                                    | URL (URL 경로, URL 네임 모두 가능)                | '/accounts/profile/'        | 성공적인 로그인 시 리디렉트되는 URL                                                                                                                                      |
| LOGIN_URL                                             | URL (URL 경로, URL 네임 모두 가능)                | '/accounts/login/'          | 웹사이트의 로그인 URL (이 [영상](https://www.codeit.kr/learn/4826)을 참고하세요)                                                                                            |
| PASSWORD_RESET_TIMEOUT                                | 비밀번호 재설정 링크 만료 기간 (단위: 초)                 | 259200 (3일)                 | 비밀번호 재설정 링크 만료 기간 (Django 3.1 이후 버전에서만 지원)                                                                                                                 |
| PASSWORD_RESET_TIMEOUT_DAYS                           | 비밀번호 재설정 링크 만료 기간 (단위: 일)                 | 3                           | 비밀번호 재설정 링크 만료 기간 (Django 3.0 이전 버전에서만 지원)                                                                                                                 |
| SESSION_COOKIE_AGE                                    | 세션 쿠키 만료 기간 (단위: 초)                       | 1209600 (2주)                | 세션 쿠키 만료 기간 (로그인을 얼마나 오랫동안 유지할 것인지)                                                                                                                        |

나머지 세팅들은 링크를 참고하세요!

[Configuration &mdash; django-allauth 0.43.0 documentation](https://django-allauth.readthedocs.io/en/latest/configuration.html)

# Allauth HTML

![](assets/2023-04-29-09-50-54-image.png)<img src="assets/2023-04-29-09-51-11-image.png" title="" alt="" width="338">

![](assets/2023-04-29-09-52-05-image.png)![](assets/2023-04-29-09-52-43-image.png)![](assets/2023-04-29-09-53-01-image.png)![](assets/2023-04-29-09-53-22-image.png)![](assets/2023-04-29-09-53-36-image.png)![](assets/2023-04-29-09-54-12-image.png)![](assets/2023-04-29-09-54-29-image.png)![](assets/2023-04-29-09-54-56-image.png)![](assets/2023-04-29-09-55-13-image.png)![](assets/2023-04-29-09-55-42-image.png)

![](assets/2023-04-29-09-58-17-image.png)

![](assets/2023-04-29-10-01-06-image.png)![](assets/2023-04-29-10-01-24-image.png)![](assets/2023-04-29-10-01-40-image.png)![](assets/2023-04-29-10-04-48-image.png)![](assets/2023-04-29-10-05-35-image.png)![](assets/2023-04-29-10-07-21-image.png)![](assets/2023-04-29-10-07-41-image.png)![](assets/2023-04-29-10-08-05-image.png)![](assets/2023-04-29-10-08-24-image.png)![](assets/2023-04-29-10-14-26-image.png)![](assets/2023-04-29-10-16-47-image.png)![](assets/2023-04-29-10-17-19-image.png)![](assets/2023-04-29-10-17-32-image.png)![](assets/2023-04-29-10-19-10-image.png)

```bash
pip install django-widget-tweaks
```

```python
# settings.py
INSTALLED_APPS [ 
    ...
    'widget_tweaks'
    ...
]
```

```html
# template 
{% widget_tweaks %}

{{ form.email |add_class:"asdf" |attr:"placeholder:email" 
    |add_error_class:"error" }}

{% for error in form.email.errors %}
    <div class="error-message">{{ error }}</div>
{% endfor %}


/* css */
.asdf input {
 ...
}
.asdf.error {
  ...
}

.error-message {
  ...
}
```

![](assets/2023-04-29-10-28-19-image.png)![](assets/2023-04-29-10-28-35-image.png)

![](assets/2023-04-29-10-30-58-image.png)<img src="assets/2023-04-29-10-31-23-image.png" title="" alt="" width="263">

![](assets/2023-04-29-10-52-16-image.png) ![](assets/2023-04-29-10-36-46-image.png)![](assets/2023-04-29-10-35-57-image.png)

![](assets/2023-04-29-10-53-32-image.png)

---

input 태그에는 여러 속성이 사용됩니다. 예를 들어 제공되는 singnup.html 템플릿에는 아래와 같은 input 태그가 있었는데요.

```html
<input type="email" name="email" placeholder="이메일" autocomplete="email" class="cp-input" required id="id_email">

<input type="text" name="nickname" maxlength="15" placeholder="닉네임 (Coplate에서 사용되는 이름입니다)" class="error cp-input" required id="id_nickname">

<input type="password" name="password1" placeholder="비밀번호" autocomplete="new-password" class="cp-input" required id="id_password1">

<input type="password" name="password2" placeholder="비밀번호 확인" class="cp-input" required id="id_password2">
```

### `type`

필드에 들어가는 데이터 유형을 뜻합니다. 모델 폼을 사용하면 모델 필드의 종류에 따라 `type` 이 설정됩니다. (예: `CharField` - `type="text"`, `URLField` - `"type=url"`, `IntegerField` - `type="number"`, `ImageField` - `type="file"`)

`type`에 따라 사용되는 HTML 폼 필드가 결정되고 입력되는 데이터에 대한 유효성 검사도 진행됩니다. 예를 들어 `"type=url"`인 경우 일반 텍스트 필드가 사용되는데, 여기에 유효한 URL을 넣지 않으면 폼을 submit(서버에 전달) 할 수 없습니다. 참고로 이런 유효성 검사는 서버 측에서 진행되는 유효성 검사와 다릅니다. 유효하지 않은 데이터는 아예 서버 쪽으로 전달되는 것을 막기 위해서 클라이언트, 즉 웹 브라우저 측에서도 어느 정도의 유효성 검사를 해 줍니다. 하지만 클라이언트 측에서 진행할 수 없는 유효성 검사도 있는데요. 예를 들어 어떤 값의 중복 여부를 확인하려면 데이터베이스에 있는 값들과 비교를 해야 하기 때문에 클라이언트 측에서 확인할 수 없습니다.

### `name`

폼 데이터가 서버로 전송될 때 사용되는 이름인데, django 폼을 사용하면 자동으로 설정되기 때문에 크게 신경 쓰지 않으셔도 됩니다.

### `placeholder`

HTML 폼 필드 안에 디스플레이되는 텍스트입니다. Django 폼을 사용하면 기본적으로 django 필드의 이름이 사용됩니다. (그래서 우리는 widget-tweaks 패키지를 사용해서 placeholder 속성을 바꿔주었죠?)

### `maxlength`

입력받는 값의 최대 길이를 제한합니다. 이것도 클라이언트 측에서 진행되는 유효성 검사의 일부라고 볼 수 있는데요. 모델 폼을 사용하면 `CharField`의 `max_length` 값에 따라 자동으로 설정됩니다.

### `autocomplete`

브라우저는 기본적으로 input 태그에 입력되는 값들을 기억합니다. autocomplete(자동완성) 기능은 HTML 폼 필드에 값을 입력할 때, 과거에 비슷한 필드에 입력했던 값을 제안해 주는 기능입니다. autocomplete 속성은 form 태그에도 있고, input 태그에도 있는데 autocomplete 속성의 디폴트 값은 "on"이고 input 태그의 autocomplete 속성이 더 우선순위가 높습니다. 그러니까 form 태그와 안에 있는 input 태그에 둘 다 autocomplete 속성이 정의돼 있으면 input 태그의 autocomplete 속성이 사용되는 거죠. (form 태그에는 autocomplete 속성이 있고 input 태그에는 없는 경우 form 태그의 autocomplete 속성이 사용됩니다.)

form 태그의 autocomplete 속성에는 "on"(자동완성 기능을 사용함), "off"(자동완성 기능을 사용하지 않음) 두 가지 옵션이 있고, input 태그의 autocomplete 속성에는 "on", "off" 외에도 많은 옵션이 있습니다. 예를 들어 위 코드를 보시면 `autocomplete="email"`, `autocomplete="new-password"`같이 다양한 값이 사용되는 걸 확인하실 수 있을 텐데요. 다양한 속성을 통해 브라우저한테 어떤 정보에 대한 자동완성을 원하는지 전달해 줄 수 있습니다. 예를 들어 `autocomplete="email"`을 사용하면 이메일 주소만 제안해 줍니다. 여러 autocomplete 옵션에 대한 설명은 이 [링크](https://developer.mozilla.org/ko/docs/Web/HTML/Attributes/autocomplete)를 참고하세요.

참고로 요즘은 로그인을 할 때 브라우저가 ID와 비밀번호를 기억했다가 자동으로 입력해 주죠?

![](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=4796&directory=pic8.png&name=pic8.png)

이건 자동완성 중에서도 조금 특별한 기능이고 로그인 필드에서는 autocomplete을 꺼도 이 기능이 항상 사용됩니다. 이 점 유의해 주세요.

### `class`

디자인 (CSS)를 위한 속성입니다. Django가 만들어 주는 input 태그에는 class 속성이 포함되지 않습니다.

### `required`

HTML 폼 필드를 비워놓을 수 없게 하는 속성입니다. 이것도 클라이언트 측에서 진행되는 유효성 검사의 일부라고 볼 수 있는데요. Django 모델/폼 필드를 필수로 정의해 주면 required 속성이 저절로 추가됩니다.

### `id`

일반적으로 id는 HTML 요소를 (CSS나 JavaScript로) 선택할 수 있게 해 줍니다. id 속성도 django 폼을 사용하면 자동으로 설정되기 때문에 크게 신경 쓰지 않으셔도 됩니다.

Django 폼을 렌더하는 작업은 항상 까다롭고 헷갈릴 수 있는데요. 먼저 `{{ form.field }}` 형태로 폼 필드를 렌더한 다음, 개발자 도구로 어떤 속성이 설정되는지를 파악하고 widget-tweaks를 사용해서 속성을 추가하거나 수정해 보세요!

---

### non-field error

![](assets/2023-04-29-11-16-58-image.png)![](assets/2023-04-29-11-17-11-image.png)![](assets/2023-04-29-11-17-28-image.png)![](assets/2023-04-29-11-17-59-image.png)

```html
<form method="post">
    {% csrf_token %}
    {% for error in form.non_field_errors %}
        <div class="form-error error-message">
            {{ error }}
        </div>
    {% endfor %}
    ...
</form>
```

---

## Message_overriding

![](assets/2023-04-29-11-36-14-image.png)<img src="assets/2023-04-29-11-36-54-image.png" title="" alt="" width="130">

<img title="" src="assets/2023-04-29-11-37-34-image.png" alt="" width="368">  <img title="" src="assets/2023-04-29-11-35-43-image.png" alt="" width="244">![](assets/2023-04-29-11-38-21-image.png)

![](assets/2023-04-29-11-39-25-image.png)![](assets/2023-04-29-11-39-47-image.png)

<img src="assets/2023-04-29-11-40-54-image.png" title="" alt="" width="242"><img src="assets/2023-04-29-11-41-38-image.png" title="" alt="" width="331"><img src="assets/2023-04-29-11-43-30-image.png" title="" alt="" width="144"><img title="" src="assets/2023-04-29-11-43-13-image.png" alt="" width="197"><img title="" src="assets/2023-04-29-11-42-57-image.png" alt="" width="237">![](assets/2023-04-29-11-44-44-image.png)![](assets/2023-04-29-11-45-28-image.png)![](assets/2023-04-29-11-45-43-image.png)

```html
{{ activate_url }}
```

![](assets/2023-04-29-11-47-00-image.png)

```python
# settings.py
ACCOUNT_EMAIL_SUBJECT_PREFIX = ""
```

![](assets/2023-04-29-11-48-51-image.png)![](assets/2023-04-29-11-49-09-image.png)![](assets/2023-04-29-11-49-26-image.png)![](assets/2023-04-29-11-49-39-image.png)![](assets/2023-04-29-11-49-51-image.png)![](assets/2023-04-29-11-50-08-image.png)

allauth의 템플릿 파일을 오버라이드하려면 allauth의 템플릿 파일과 똑같은 이름을 가진 파일을 app_name/templates/account/ 폴더 안에 넣어주시면 됩니다. 그리고 settings.py 파일의 `INSTALLED_APPS` 목록에서 `app_name`은 `allauth`보다 위에 와야 합니다.

# HTML 템플릿

커스텀 템플릿을 app_name/templates/account/ 폴더 안에 넣어주시면 됩니다.

(예: coplate/templates/account/signup.html)

| 페이지                                                  | 템플릿 이름                            | 필드                                                                                                                                                                        |
| ---------------------------------------------------- | --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 회원가입 ('account_signup')                              | signup.html                       | - 유저네임: {{ form.username }}<br>- 이메일: {{ form.email }}<br>- 비밀번호: {{ form.password1 }}<br>- 비밀번호 확인: {{ form.password2 }}<br>- 추가 필드(extra_field): {{ form.extra_field }} |
| 로그인 ('account_login')                                | login.html                        | - 로그인 (유저네임/이메일/둘 다 허용): {{ form.login }}<br>- 비밀번호: {{ form.password }}                                                                                                  |
| 비밀번호 변경 ('account_change_password')                  | password_change.html              | - 현재 비밀번호: {{ form.oldpassword }}<br>- 새 비밀번호: {{ form.password1 }}<br>- 새 비밀번호 확인: {{ form.password2 }}                                                                  |
| 비밀번호 찾기 ('account_reset_password')                   | password_reset.html               | - 이메일: {{ form.email }}                                                                                                                                                   |
| 비밀번호 재설정 이메일 발송 완료 ('account_reset_password_done')   | password_reset_done.html          |                                                                                                                                                                           |
| 비밀번호 재설정 ('account_reset_password_from_key')         | password_reset_from_key.html      | - 새 비밀번호: {{ form.password1 }}<br>- 새 비밀번호 확인: {{ form.password2 }}                                                                                                       |
| 비밀번호 재설정 완료 ('account_reset_password_from_key_done') | password_reset_from_key_done.html |                                                                                                                                                                           |

위 테이블에 있는 필드를 활용해서 템플릿을 만드시면 됩니다.

예: signup.html

```html
{% extends "coplate_base/base.html" %}

{% load static %}
{% load widget_tweaks %}

{% block title %}회원가입 | Coplate{% endblock title %}

{% block content %}
<div class="account-background">
  <main class="account">
    <div class="title">
      <a href="{% url 'index' %}">
        <img class="logo" src="{% static 'coplate/assets/coplate-logo.svg' %}" alt="Coplate Logo">
      </a>
    </div>

    <form method="post">
      {% csrf_token %}
      <div>
        {{ form.email|add_class:"cp-input"|attr:"placeholder:이메일"|add_error_class:"error" }}
        {% for error in form.email.errors %}
          <div class="error-message">{{ error }}</div>
        {% endfor %}
      </div>
      <div>
        {{ form.nickname|add_class:"cp-input"|attr:"placeholder:닉네임 (Coplate에서 사용되는 이름입니다)"|add_error_class:"error" }}
        {% for error in form.nickname.errors %}
          <div class="error-message">{{ error }}</div>
        {% endfor %}
      </div>
      <div>
        {{ form.password1|add_class:"cp-input"|attr:"placeholder:비밀번호"|add_error_class:"error" }}
        {% for error in form.password1.errors %}
          <div class="error-message">{{ error }}</div>
        {% endfor %}
      </div>
      <div>
        {{ form.password2|add_class:"cp-input"|attr:"placeholder:비밀번호 확인"|add_error_class:"error" }}
        {% for error in form.password2.errors %}
          <div class="error-message">{{ error }}</div>
        {% endfor %}
      </div>
      <button class="cp-button" type="submit">회원가입</button>
    </form>

    <div class="info">
      이미 회원이신가요?<a class="link" href="{% url 'account_login' %}">로그인</a>
    </div>
  </main>
</div>
{% endblock content %}
```

# 이메일 템플릿

커스텀 템플릿을 app_name/templates/account/email/ 폴더 안에 넣어주시면 됩니다.

(예: coplate/templates/account/email/email_confirmation_signup_subject.txt)

| 설명                                                                          | 템플릿 이름                                | 템플릿 변수                                |
| --------------------------------------------------------------------------- | ------------------------------------- | ------------------------------------- |
| 인증 이메일 제목<br>(회원가입시 자동으로 발송되는 이메일)                                          | email_confirmation_signup_subject.txt |                                       |
| 인증 이메일 내용<br>(회원가입시 자동으로 발송되는 이메일)                                          | email_confirmation_signup_message.txt | 이메일 인증 링크: {{ activate_url }}         |
| 인증 이메일 제목<br>(수동으로 발송되는 이메일: [나중에 사용됩니다](https://www.codeit.kr/learn/4828)) | email_confirmation_subject.txt        |                                       |
| 인증 이메일 내용<br>(수동으로 발송되는 이메일)                                                | email_confirmation_message.txt        | 이메일 인증 링크: {{ activate_url }}         |
| 비밀번호 재설정 이메일 제목                                                             | password_reset_key_subject.txt        |                                       |
| 비밀번호 재설정 이메일 내용                                                             | password_reset_key_message.txt        | 비밀번호 재설정 링크: {{ password_reset_url }} |

필요할 경우 위 테이블에 있는 템플릿 변수를 활용해서 이메일 내용을 작성하시면 됩니다.

예: password_reset_key_message.txt

```
안녕하세요 {{ user }} 회원님,

아래 링크를 통해 계정의 비밀번호를 재설정하실 수 있습니다.

{{ password_reset_url }}

감사합니다.

Coplate
```

그리고 이메일 제목은 템플릿을 오버라이딩해도 제목 앞에 웹사이트 도메인이 붙는데, 이걸 제거하려면 `ACCOUNT_EMAIL_SUBJECT_PREFIX`를 설정해 주시면 됩니다.

```python
ACCOUNT_EMAIL_SUBJECT_PREFIX = ''
```

`ACCOUNT_EMAIL_SUBJECT_PREFIX`의 디폴트 값은 웹사이트 도메인 이름입니다.

# 메시지 템플릿

우리는 메시지를 사용하지 않기 때문에 빈 메시지 템플릿을 사용했습니다.

메시지 템플릿은 app_name/templates/account/messages/ 폴더 안에 넣어주시면 됩니다.

만약 메시지 내용을 실제로 오버라이드하고, 웹사이트 내에서 사용하고 싶으시다면 메시지를 디스플레이해 줘야 하는데요. 메시지를 디스플레이하는 방법은 [여기](https://docs.djangoproject.com/en/2.2/ref/contrib/messages/#displaying-messages)서 확인하실 수 있습니다.

---

[django-allauth](https://django-allauth.readthedocs.io/en/latest/index.html)는 유저 기능을 만들기 위한 패키지입니다.

allauth는 Django 프레임워크에 포함되지 않기 때문에 따로 설치를 해줘야 합니다. (설치 [가이드](https://django-allauth.readthedocs.io/en/latest/installation.html), 설치 [영상](https://www.codeit.kr/learn/4773))

allauth 패키지 안에는 유저 기능 구현에 필요한 URL 패턴, 뷰, 폼, 템플릿 등이 있고, 유저 모델은 django.contrib.auth의 유저 모델을 사용하는데요. allauth를 설치하면 안에 있는 코드를 가지고 기본적인 유저 시스템을 만들어 줍니다. 우리는 이 유저 시스템을 우리의 니즈에 맞게 바꿔주면 되는데요, 여러 부분들을 바꿔줄 수 있습니다.

# allauth URL: URL 패턴 정의

allauth의 URL은 [여기](https://www.codeit.kr/learn/4791) 정리돼 있는데요, 처음에 allauth URL을 프로젝트에 추가할 때, 앞에 붙는 패턴을 정해줄 수 있습니다.

project/urls.py

```python
urlpatterns = [
    ...
    path('accounts/', include('allauth.urls')),
    ...
]
```

이렇게 정의해 주면 모든 url 앞에 accounts/가 붙고 (예: localhost:8000/accounts/login/),

project/urls.py

```python
urlpatterns = [
    ...
    path('', include('allauth.urls')),
    ...
]
```

이렇게 정의해 주면 모든 url 앞에 아무것도 안 붙습니다 (예: localhost:8000/login/).

# allauth 주요 로직: 세팅(Configuration)

allauth의 주요 로직은 세팅(configuration)을 통해 바꿀 수 있습니다. [여기](https://www.codeit.kr/learn/4792)서 자주 사용되는 세팅을 찾으실 수 있습니다. 리디렉션 URL, 폼에서 사용되는 필드, 링크를 클릭했을 때의 동작 등 여러 가지를 바꿀 수 있는데요. settings.py에 간단한 코드를 써주는 거만으로도 로직을 원하는 대로 바꿀 수 있다는 게 allauth의 큰 장점입니다.

# allauth 폼: 커스텀 폼

기본 유저 인증 관련 페이지들에서는 다양한 폼이 사용됩니다. 로그인 폼, 회원가입 폼, 비밀번호 변경 폼 등 다양한 폼이 있죠? 회원가입을 제외한 나머지 페이지는 거의 항상 똑같은 필드를 가지고 있기 때문에 폼을 바꿔줄 필요가 없습니다. 예를 들어 로그인은 항상 로그인 필드와 비밀번호 필드가 있고, 비밀번호 변경은 현재 비밀번호, 새 비밀번호, 새 비밀번호 확인 필드가 있죠? 하지만 회원가입은 서비스에 따라 필요한 정보가 다 다르기 때문에 폼을 커스터마이즈해야 하는 경우가 많습니다. 유저네임 필드 여부, 비밀번호 필드 여부 같은 흔한 설정은 configuration을 통해 할 수 있지만, 커스텀 정보를 입력받으려면 커스텀 폼을 사용해야 합니다.

forms.py 파일에 추가 필드에 대한 폼을 만들고, `signup(self, request, user)` 메소드를 정의해 주면 됩니다.

app/forms.py

```python
class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['extra_field1', 'extra_field2', ...]

        def signup(self, request, user):
            user.extra_field1 = self.cleaned_data['extra_field1']
            user.extra_field2 = self.cleaned_data['extra_field2']
        ...
            user.save()
```

(참고로 `ModelForm` 대신 일반 `Form`을 써도 됩니다.)

그리고 `ACCOUNT_SIGNUP_FORM_CLASS`를 설정해 주면 됩니다.

project/settings.py

```python
ACCOUNT_SIGNUP_FORM_CLASS = 'app.forms.SignupForm' 
```

# 디자인: 템플릿 오버라이딩

아마 allauth가 제공하는 기본 템플릿을 그대로 사용하고 싶지는 않으실 겁니다. 템플릿을 오버라이딩 하려면 allauth가 제공하는 템플릿과 똑같은 이름을 가진 파일을 account 폴더 안에 넣어주면 되는데요. 자세한 내용은 [링크](https://www.codeit.kr/learn/4799)를 참고하세요.

# 뷰 오버라이딩?

뷰는 어떤 웹 페이지의 주요 로직을 담당하는 부분입니다. allauth에서 기본적으로 제공하는 뷰를 오버라이딩하면, 로직을 원하는 대로 바꿔줄 수 있지만, 그 과정은 굉장히 복잡하고 대부분의 로직은 configuration을 통해 바꿀 수 있기 때문에 뷰는 잘 오버라이딩 하지 않습니다. 유일한 예외는 비밀번호 변경 로직을 다루는 `PasswordChangeView`인데, 비밀번호 변경 후 리디렉트되는 URL을 configuration으로 설정할 수 없기 때문에 뷰를 오버라이딩해 줬습니다.

app/views.py

```python
class CustomPasswordChangeView(PasswordChangeView):
    def get_success_url(self):
        return reverse('index')
```

위 코드는 리디렉트 URL을 `'index'`, 즉 홈페이지로 설정합니다. 그리고 오버라이딩한 뷰를 사용하기 위해서 URL 패턴을 바꿔주면 되니다.

project/urls.py

```python
urlpatterns = [
    ...
    path('password/change/', CustomPasswordChangeView.as_view(), name='account_password_change'),
    path('', include('allauth.urls')),
]
```
