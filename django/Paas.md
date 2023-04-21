# Paas

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-19-00-07-18-image.png)

## 1. off debug

```python
# setting.py

DEBUG = False
```

## 2.  setting Host

write this code

```python
# setting.py

ALLOWED_HOSTS = ['.pythonanywhere.com']
```

## 2. collect static file

write this code

```python
# setting.py

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-19-00-15-17-image.png)

```terminal
# terminal

python manage.py collectstatic
```

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-19-00-18-34-image.png)       =>             ![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-19-00-19-22-image.png)

## 4. make project file to zip file

## 5. python anywhere sign up and upload

https://www.pythonanywhere.com/

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-19-00-24-50-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-19-00-26-04-image.png)

project.zip file upload

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-19-00-26-49-image.png)

then it will open console

write this

```bash
unzip yourfilename.zip
virtualenv --python=python3.7 venv
cd venv
. venv/script/active
pip install django==3.23
```

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-19-01-11-09-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-19-01-11-45-image.png)

push next 

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-19-01-12-40-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-19-01-13-31-image.png)

select your python version, and push next

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-19-01-15-32-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-19-01-16-00-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-19-01-17-22-image.png)

click

line 19 ~ line 47 comment out

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-19-01-19-35-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-19-01-19-53-image.png)

line 76 - line 89 uncomment

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-19-01-21-53-image.png)

line 81 

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-19-01-23-07-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-19-01-23-34-image.png)

line 85

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-19-01-24-04-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-19-01-24-21-image.png)

click save

![](assets/2023-04-21-00-30-27-image.png)

and click web

![](assets/2023-04-21-00-30-59-image.png)

find Virtualenv

![](assets/2023-04-21-00-33-42-image.png)

![](assets/2023-04-21-00-34-19-image.png)

![](assets/2023-04-21-00-34-50-image.png)

![](assets/2023-04-21-00-35-22-image.png)

![](assets/2023-04-21-00-35-47-image.png)

go to up

![](assets/2023-04-21-00-36-54-image.png)
