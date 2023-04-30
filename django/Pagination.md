# Pagination

We will use this Command

in **Terminal**

```bash
python manage.py shell

from django.core.paginator import Paginator

from {app_name}.models import {YourModel}

your_models = {YourModel}.objects.all()
# out : 54

pages = Paginator(your_models, 6)

pages.page_range
# out : range(1, 10) 

page = pages.page(1)

page.objects_list
# out : <QuerySet [~~~~~]>

page.has_next()
# out : True


page.has_previous()
# out : False


page.next_page_number()
# out : 2
```

## 1. Paginator in Views

```python
# views.py

from django.core.paginator import Paginator


def post_list(req):
    posts = Post.objects.all()
    paginator = Paginator(posts, 6)
    cur_page_number = req.GET.get('page')
    if cur_page_number is None:
        cur_page_number = 1
    page = paginator.page(cur_page_number)
    return render(req, posts/post_list.html, {'page' : page})
```

## 2. Paginator in Template

before

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-21-19-55-10-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-21-19-55-31-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-21-19-56-02-image.png)

```python
{% if post %}
   =>
{% if page.object_list %}
```

---

### object_list

![](assets/2023-04-21-20-20-09-image.png)

![](assets/2023-04-21-20-20-27-image.png)

---

![](assets/2023-04-21-20-21-47-image.png)

![](assets/2023-04-21-20-22-14-image.png)

```python
{% for post in posts %}
   =>
{% for post in page.object_list %}
```

![](assets/2023-04-21-20-23-46-image.png)

```python
<div class="paginator">
    {% if page.has_previous %}
        <a href="?page={{ page.previous_page_number}}"
        class="prev">prev</a>
    {% endif %}
</div>
```

![](assets/2023-04-21-20-25-39-image.png)

![](assets/2023-04-21-20-28-26-image.png)

![](assets/2023-04-21-20-28-39-image.png)

![](assets/2023-04-21-20-28-58-image.png)

![](assets/2023-04-21-20-29-20-image.png)

![](assets/2023-04-21-20-29-37-image.png)

![](assets/2023-04-21-20-29-54-image.png)

![](assets/2023-04-21-20-31-06-image.png)

![](assets/2023-04-21-20-31-26-image.png)

![](assets/2023-04-21-20-31-41-image.png)

```python
<div class="paginator">
    {% if page.has_previous %}

        #############################
        <a href="?page=1"
        class="first">first</a>
        #############################

        <a href="?page={{ page.previous_page_number}}"
        class="prev">prev</a>

    {% endif %}
</div>
```

![](assets/2023-04-21-20-32-00-image.png)

![](assets/2023-04-21-20-33-14-image.png)

![](assets/2023-04-21-20-36-14-image.png)

![](assets/2023-04-21-20-37-04-image.png)![](assets/2023-04-21-20-37-28-image.png)

![](assets/2023-04-21-20-38-04-image.png)

![](assets/2023-04-21-20-38-32-image.png)

```python
<div class="paginator">
    {% if page.has_previous %}
        <a href="?page=1"
        class="first">first</a>
        <a href="?page={{ page.previous_page_number}}"
        class="prev">prev</a>

        #############################
        <div>
            <p>{{ page.number}} of {{ page.paginator.num_pages}}</p>
        </div>
        #############################
    {% endif %}
</div>
```

![](assets/2023-04-21-20-45-12-image.png)

![](assets/2023-04-22-02-45-47-image.png)

![](assets/2023-04-22-02-46-06-image.png)

![](assets/2023-04-22-02-46-29-image.png)

![](assets/2023-04-22-02-46-53-image.png)

![](assets/2023-04-22-02-47-12-image.png)

```python
<div class="paginator">
    {% if page.has_previous %}
        <a href="?page=1"
        class="first">first</a>
        <a href="?page={{ page.previous_page_number}}"
        class="prev">prev</a>

        <div>
            <p>{{ page.number}} of {{ page.paginator.num_pages}}</p>
        </div>

        #############################
        {% if page.has_next %}
            <a href="?page={{page.next_page_number}}"
            class="next">next</a>
        #############################
    {% endif %}
</div>
```

![](assets/2023-04-22-03-17-01-image.png)

![](assets/2023-04-22-03-17-29-image.png)

```python
<div class="paginator">
    {% if page.has_previous %}
        <a href="?page=1"
        class="first">first</a>
        <a href="?page={{ page.previous_page_number}}"
        class="prev">prev</a>

        <div>
            <p>{{ page.number}} of {{ page.paginator.num_pages}}</p>
        </div>

        {% if page.has_next %}
            <a href="?page={{page.next_page_number}}"
            class="next">next</a>
        #############################
            <a href="?page={{page.paginator.num_pages}}"
            class="last">last</a>
        #############################
    {% endif %}
</div>
```

# Final_code

```html
{% if is_paginated %}
    {% if page_obj.has_previous %}
        <a href="?page=1">처음</a></li>
        <a href="?page={{ page_obj.previous_page_number }}">이전</a>
    {% endif %}
    {% for num in page_obj.paginator.page_range %}
        {% if page_obj.number == num %}
            {{ num }}
        {% elif num > page_obj.number|add:'-3' and num < page_obj.number|add:'3' %}
            <a href="?page={{ num }}">{{ num }}</a>
        {% endif %}
    {% endfor %}
    {% if page_obj.has_next %}
        <a href="?page={{ page_obj.next_page_number }}">다음</a>
        <a href="?page={{ page_obj.paginator.num_pages }}">마지막</a>
    {% endif %}
{% endif %}
```


