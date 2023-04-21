# Seeding

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-21-04-47-44-image.png)





![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-21-04-50-42-image.png)

```bash
python manage.py dumpdata {app_name} > {filenameyouwant}.json
```

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-21-04-51-44-image.png)

```bash
python manage.py dumpdata 
    {app_name} --indent=2 > {filenameyouwant}.json

# one line
```

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-21-04-56-56-image.png)

makefile





![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-21-04-57-43-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-21-04-57-27-image.png)

```bash
python manage.py loaddata {filenameyouwant}.json
```



# More data

```bash
pip install django-seed==0.2.2
```

![](assets/2023-04-21-05-02-06-image.png)

```bash
python manage.py seed {app_name} --number=50
```




