# Humanize

[django.contrib.humanize | Django documentation | Django](https://docs.djangoproject.com/en/3.2/ref/contrib/humanize/)



```python
# setting.py

INSTALLED_APPS = [
 ...,
 'django.contrib.humanize',
]
```

```html
{% load humanize %}

{{price | intcomma}}
```


