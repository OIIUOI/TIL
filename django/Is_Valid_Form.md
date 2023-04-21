# Is valid Form?

## How to valid by Model Field

In field title, unique option make valid data

![](assets/2023-04-21-02-13-51-image.png)

![](assets/2023-04-21-02-14-18-image.png)

![](assets/2023-04-21-02-14-54-image.png)

## How to valid by Validator

![](assets/2023-04-21-02-19-02-image.png)

make new file validator.py

![](assets/2023-04-21-02-24-44-image.png)

![](assets/2023-04-21-02-25-07-image.png)

![](assets/2023-04-21-02-25-59-image.png)

![](assets/2023-04-21-02-23-26-image.png)

![](assets/2023-04-21-02-26-41-image.png)

![](assets/2023-04-21-02-26-55-image.png)

![](assets/2023-04-21-02-27-27-image.png)

![](assets/2023-04-21-02-27-40-image.png)

![](assets/2023-04-21-02-27-56-image.png)

![](assets/2023-04-21-02-29-36-image.png)

![](assets/2023-04-21-02-22-34-image.png)

![](assets/2023-04-21-02-31-44-image.png)

![](assets/2023-04-21-02-31-59-image.png)

![](assets/2023-04-21-02-33-03-image.png)

## How to valid in form

example >>

![](assets/2023-04-21-02-37-44-image.png)

![](assets/2023-04-21-02-39-43-image.png)

![](assets/2023-04-21-02-40-01-image.png)

![](assets/2023-04-21-02-40-36-image.png)

![](assets/2023-04-21-02-40-51-image.png)

![](assets/2023-04-21-02-41-12-image.png)

![](assets/2023-04-21-02-41-24-image.png)

![](assets/2023-04-21-02-41-47-image.png)

![](assets/2023-04-21-02-42-02-image.png)

![](assets/2023-04-21-02-42-27-image.png)

![](assets/2023-04-21-02-44-26-image.png)

![](assets/2023-04-21-02-44-56-image.png)

![](assets/2023-04-21-02-45-28-image.png)

![](assets/2023-04-21-02-46-08-image.png)

![](assets/2023-04-21-02-46-24-image.png)

![](assets/2023-04-21-02-46-43-image.png)

![](assets/2023-04-21-02-47-17-image.png)

![](assets/2023-04-21-02-47-29-image.png)

![](assets/2023-04-21-02-49-23-image.png)

![](assets/2023-04-21-02-48-21-image.png)

![](assets/2023-04-21-02-48-41-image.png)

![](assets/2023-04-21-02-48-57-image.png)

![](assets/2023-04-21-02-53-49-image.png)



# 유효성 검증을 뒤늦게 추가했다면?



![](assets/2023-04-21-05-32-01-image.png)

make new file **validate_data.py**

we'll make function for check and modify data

```python
# validate_data.py

from .models import {YourModel}

def validate_post():
    # 1. bring all data
    models = {YourModel}.objects.all()

    # 2. check that exist '&' in your model data
    for model in models:
        if '&' in model.{yourfield}:
            # 3. if exist '&' in data, delete '&'
            post.{yourfield} = post.{yourfield}.replace('&', '')

            # 4. save the data
            post.save()

    # if modified day is earlier than created day
    if model.dt_modified < model.dt_created:
        model.save()
        # dt_modified will be present
```



In **terminal**

```bash
python manage.py shell


from {app_name}.validate_data import validate_post


validate_post()

exit()
```
