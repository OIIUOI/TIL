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
AUTH_USER)MODEL = 'app_name.User'
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



![](assets/2023-04-29-00-50-50-image.png)![](assets/2023-04-29-00-51-02-image.png)
