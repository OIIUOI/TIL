# ClassView

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-22-04-33-51-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-22-04-29-36-image.png)

```python
# url.py


urlpatterns = [
    path('', views.PostCreateView.as_view(), name="create")
]
```

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-22-04-36-55-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-22-04-35-39-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-22-04-36-04-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-22-04-37-59-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-22-04-38-16-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-22-04-37-37-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-22-04-38-52-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-22-04-40-30-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-22-04-40-42-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-22-04-41-16-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-22-04-41-49-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-22-04-42-12-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-22-04-41-32-image.png)

---

## Generic View

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-22-04-43-07-image.png)

### CreateView

```python
from django.views.generic import CreateView

classs PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "posts/post_form.html"
```

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-22-07-05-29-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-22-07-05-43-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-22-07-05-58-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-22-07-06-56-image.png)

![](assets/2023-04-23-19-23-19-image.png)

![](assets/2023-04-23-19-23-35-image.png)

![](assets/2023-04-23-19-24-20-image.png)

![](assets/2023-04-23-19-24-49-image.png)

![](assets/2023-04-23-19-25-18-image.png)

![](assets/2023-04-23-19-25-50-image.png)

![](assets/2023-04-23-19-26-11-image.png)

![](assets/2023-04-23-19-26-40-image.png)

```python
from django.views.generic import CreateView
########################################
from django.urls import reverse
########################################

classs PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "posts/post_form.html"

    ########################################
    def get_success_url(self):
        return reverse('post-detail', 
               kwargs={'post_id':self.object.id})
    ########################################
```

```python
def get_success_url(self):
        # self.object는 이 CreateView에서 새로 생성한 데이터 모델을 말합니다.
        return reverse('<이동할 URL>', kwargs={'<URL에 전달할 키워드>': <전달할 값>})
```

###### Reverse

![](assets/2023-04-23-19-27-55-image.png)

![](assets/2023-04-23-19-28-33-image.png)

###### Kwargs

![](assets/2023-04-23-19-29-16-image.png)

![](assets/2023-04-23-19-29-32-image.png)

###### self.object

![](assets/2023-04-23-19-30-04-image.png)

![](assets/2023-04-23-19-30-22-image.png)

![](assets/2023-04-23-19-31-44-image.png)

![](assets/2023-04-23-19-31-58-image.png)

---

### ListView

![](assets/2023-04-23-19-40-00-image.png)

![](assets/2023-04-23-19-40-17-image.png)

![](assets/2023-04-23-19-40-40-image.png)

![](assets/2023-04-23-19-42-27-image.png)

![](assets/2023-04-23-19-42-49-image.png)

![](assets/2023-04-23-19-43-12-image.png)

![](assets/2023-04-23-19-44-05-image.png)

![](assets/2023-04-23-19-44-47-image.png)

![](assets/2023-04-23-19-45-13-image.png)

![](assets/2023-04-23-19-45-29-image.png)

![](assets/2023-04-23-19-45-44-image.png)

![](assets/2023-04-23-19-46-18-image.png)

```python
from django.views.generic import ListView

class PostListView(ListView):
    model = Post
    template_name="posts/post_list.html"
    context_object_name="posts"
    ordering = ['-dt_created']
    paginate_by = 6
    page_kwarg = 'page'
```

#### how to write Html with ListView

![](assets/2023-04-23-19-48-18-image.png)

![](assets/2023-04-23-19-48-35-image.png)

<img src="assets/2023-04-23-19-48-59-image.png" title="" alt="" width="231">

<img src="assets/2023-04-23-19-49-07-image.png" title="" alt="" width="249">

![](assets/2023-04-23-19-49-20-image.png)

![](assets/2023-04-23-19-49-37-image.png)

![](assets/2023-04-23-19-49-54-image.png)

![](assets/2023-04-23-19-51-35-image.png)

![](assets/2023-04-23-19-52-05-image.png)

![](assets/2023-04-23-19-53-12-image.png)

![](assets/2023-04-23-19-52-38-image.png)

![](assets/2023-04-23-19-52-53-image.png)

![](assets/2023-04-23-19-53-34-image.png)

![](assets/2023-04-23-19-53-49-image.png)

---

### DetailView

![](assets/2023-04-23-20-03-59-image.png)

![](assets/2023-04-23-20-04-15-image.png)

![](assets/2023-04-23-20-04-45-image.png)

![](assets/2023-04-23-20-05-39-image.png)

![](assets/2023-04-23-20-06-00-image.png)

![](assets/2023-04-23-20-06-35-image.png)

![](assets/2023-04-23-20-06-50-image.png)

![](assets/2023-04-23-20-07-34-image.png)

![](assets/2023-04-23-20-07-53-image.png)

```python
from django.views.generic import DetailView

class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post_detail.html"
    pk_url_kwarg = "post_id"
    context_object_name = "post"
```

---

### UpdateView

```python
from django.views.generic import UpdateView

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_form.html'
    pk_url_kwarg = 'post_id'

    def get_success_url(self):
        return reverse('post-detail', kwargs={'post_id': self.object.id})
```

---

### DeleteView

```python
from django.views.generic import DeleteView

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/post_confirm_delete.html'
    pk_url_kwarg = 'post_id'
    context_object_name = 'post'

    def get_success_url(self):
        return reverse('post-list')
```

![](C:\Users\jin47\OneDrive\바탕%20화면\TIL\django\Classview\assets\2023-04-23-19-23-19-image.png)

![](C:\Users\jin47\OneDrive\바탕%20화면\TIL\django\Classview\assets\2023-04-23-20-18-19-image.png)

![](C:\Users\jin47\OneDrive\바탕%20화면\TIL\django\Classview\assets\2023-04-23-20-18-37-image.png)

![](assets/2023-04-23-20-19-01-image.png)

---

## Context in GenericView

![](assets/2023-04-23-20-26-32-image.png)

![](assets/2023-04-23-20-26-47-image.png)

![](assets/2023-04-23-20-28-09-image.png)

![](assets/2023-04-23-21-13-09-image.png)

![](assets/2023-04-23-21-06-13-image.png)

![](assets/2023-04-23-21-06-54-image.png)

![](assets/2023-04-23-21-13-56-image.png)

![](assets/2023-04-23-21-14-10-image.png)

![](assets/2023-04-23-21-14-24-image.png)

![](assets/2023-04-23-21-14-37-image.png)

![](assets/2023-04-23-21-14-56-image.png)

![](assets/2023-04-23-21-15-24-image.png)

![](assets/2023-04-23-21-16-20-image.png)

![](assets/2023-04-23-21-16-45-image.png)

![](assets/2023-04-23-21-17-21-image.png)

![](assets/2023-04-23-21-17-36-image.png)

![](assets/2023-04-23-21-17-50-image.png)

![](assets/2023-04-23-21-19-44-image.png)

![](C:\Users\jin47\OneDrive\바탕%20화면\TIL\django\assets\2023-04-23-21-20-02-image.png)

![](assets/2023-04-23-21-23-49-image.png)

![](assets/2023-04-23-21-24-26-image.png)

![](assets/2023-04-23-21-24-40-image.png)

![](assets/2023-04-23-21-24-59-image.png)

![](assets/2023-04-23-21-25-12-image.png)

![](assets/2023-04-23-21-28-56-image.png)

![](assets/2023-04-23-22-29-57-image.png)

![](assets/2023-04-23-22-32-33-image.png)

![](assets/2023-04-23-21-29-35-image.png)

![](assets/2023-04-23-21-29-51-image.png)

![](assets/2023-04-23-21-30-09-image.png)

![](assets/2023-04-23-21-30-24-image.png)

![](assets/2023-04-23-21-31-03-image.png)

![](assets/2023-04-23-21-31-45-image.png)

![](assets/2023-04-23-21-32-07-image.png)

![](assets/2023-04-23-21-32-37-image.png)

![](assets/2023-04-23-21-33-00-image.png)

![](assets/2023-04-23-21-38-09-image.png)

![](assets/2023-04-23-21-36-27-image.png)

![](assets/2023-04-23-21-36-45-image.png)

![](assets/2023-04-23-21-37-01-image.png)

![](assets/2023-04-23-21-38-29-image.png)

![](assets/2023-04-23-21-38-47-image.png)

![](assets/2023-04-23-21-39-06-image.png)

![](assets/2023-04-23-21-39-21-image.png)

---

## Make simple GenericView

### Simple ListView

![](assets/2023-04-23-21-54-53-image.png)

![](assets/2023-04-23-21-55-11-image.png)

![](assets/2023-04-23-21-55-39-image.png)

![](assets/2023-04-23-21-55-51-image.png)

![](assets/2023-04-23-21-56-20-image.png)

![](assets/2023-04-23-21-56-42-image.png)

![](assets/2023-04-23-21-57-32-image.png)

<img title="" src="assets/2023-04-23-22-04-45-image.png" alt="" width="319">  <img title="" src="assets/2023-04-23-22-08-18-image.png" alt="" width="111"><img title="" src="assets/2023-04-23-22-04-59-image.png" alt="" width="440">

<img title="" src="assets/2023-04-23-22-11-26-image.png" alt="" width="230"><img title="" src="assets/2023-04-23-22-11-45-image.png" alt="" width="408">

![](assets/2023-04-23-22-12-49-image.png)

![](assets/2023-04-23-22-15-16-image.png)

![](assets/2023-04-23-22-28-23-image.png)

![](assets/2023-04-23-22-28-45-image.png)

![](assets/2023-04-23-22-36-44-image.png)

![](assets/2023-04-23-22-37-10-image.png)

![](assets/2023-04-23-22-42-37-image.png)

<img src="assets/2023-04-23-22-43-00-image.png" title="" alt="" width="462">

![](assets/2023-04-23-22-43-54-image.png)

![](assets/2023-04-23-22-44-20-image.png)

![](assets/2023-04-23-22-44-41-image.png)

![](assets/2023-04-23-22-45-01-image.png)

![](assets/2023-04-23-22-45-20-image.png)

![](assets/2023-04-23-22-45-52-image.png)

![](assets/2023-04-23-22-46-22-image.png)

![](assets/2023-04-23-22-47-29-image.png)

![](assets/2023-04-23-22-46-37-image.png)

![](assets/2023-04-23-22-47-51-image.png)

![](assets/2023-04-23-22-48-05-image.png)

![](assets/2023-04-23-22-48-22-image.png)

![](assets/2023-04-23-22-49-51-image.png)

![](assets/2023-04-23-22-50-12-image.png)

![](assets/2023-04-23-22-50-57-image.png)

![](assets/2023-04-23-22-51-34-image.png)

![](assets/2023-04-23-22-51-57-image.png)

| object_list                               |
| ----------------------------------------- |
| ![](assets/2023-04-23-23-02-26-image.png) |

![](assets/2023-04-23-23-03-26-image.png)

<img src="assets/2023-04-23-23-03-52-image.png" title="" alt="" width="449">

<img src="assets/2023-04-23-23-04-19-image.png" title="" alt="" width="480">

![](assets/2023-04-23-23-04-51-image.png)

![](assets/2023-04-23-23-05-07-image.png)

![](assets/2023-04-23-23-06-23-image.png)

![](assets/2023-04-23-23-07-07-image.png)

---

### Simple DetailView

![](assets/2023-04-23-23-12-03-image.png)

**template_name**

![](assets/2023-04-24-01-42-52-image.png)

**pk_url_kwarg**

![](assets/2023-04-24-01-45-30-image.png)<img title="" src="assets/2023-04-24-01-50-56-image.png" alt="" width="153">

![](assets/2023-04-24-01-46-06-image.png)

![](assets/2023-04-24-01-52-23-image.png)

**context_object_name**

![](assets/2023-04-24-01-54-49-image.png)

![](assets/2023-04-24-01-55-09-image.png)

![](assets/2023-04-24-01-55-36-image.png)

![](assets/2023-04-24-01-56-03-image.png)

![](assets/2023-04-24-01-56-25-image.png)

---

### CreateView

![](assets/2023-04-24-01-57-37-image.png)

**model**

It doesn't have default value

**form_class** 

It doesn't have default value

<img title="" src="assets/2023-04-24-01-58-51-image.png" alt="" width="287"><img title="" src="assets/2023-04-24-01-59-41-image.png" alt="" width="315">

**template_name**

![](assets/2023-04-24-02-01-14-image.png)

![](assets/2023-04-24-02-01-57-image.png)

<img title="" src="assets/2023-04-24-02-02-29-image.png" alt="" width="164"><img title="" src="assets/2023-04-24-02-03-06-image.png" alt="" width="403">

**get_success_url**

![](assets/2023-04-24-02-04-40-image.png)

![](assets/2023-04-24-02-05-22-image.png)

![](assets/2023-04-24-02-05-53-image.png)

![](assets/2023-04-24-02-06-27-image.png)

---

### UpdateView

![](assets/2023-04-24-02-07-38-image.png)

**form_class**

it doesn't have default value

![](assets/2023-04-24-02-09-44-image.png)

<img title="" src="assets/2023-04-24-02-10-42-image.png" alt="" width="267"><img title="" src="assets/2023-04-24-02-11-09-image.png" alt="" width="314">

**template_name**

![](assets/2023-04-24-02-13-25-image.png)

**pk_url_kwarg**

![](assets/2023-04-24-02-14-06-image.png)

![](assets/2023-04-24-02-16-42-image.png)

**get_success_url**

![](assets/2023-04-24-02-17-57-image.png)

![](assets/2023-04-24-02-18-20-image.png)

---

### DeleteView

![](assets/2023-04-24-02-19-13-image.png)

**template_name**

![](assets/2023-04-24-02-20-05-image.png)

**pk_url_kwarg**

default = pk

![](assets/2023-04-24-02-21-16-image.png)

![](assets/2023-04-24-02-21-39-image.png)

**context_object_name**

![](assets/2023-04-24-02-23-15-image.png)

![](assets/2023-04-24-02-23-27-image.png)

![](assets/2023-04-24-02-23-44-image.png)

![](assets/2023-04-24-02-24-00-image.png)

![](assets/2023-04-24-02-24-26-image.png)

![](assets/2023-04-24-02-24-42-image.png)

![](assets/2023-04-24-02-24-58-image.png)

![](assets/2023-04-24-02-25-19-image.png)

![](assets/2023-04-24-02-25-35-image.png)

![](assets/2023-04-24-02-26-28-image.png)

---

## RedirectView

![](assets/2023-04-24-02-30-00-image.png)

![](assets/2023-04-24-02-31-12-image.png)
