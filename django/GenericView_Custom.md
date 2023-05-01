# CreateView Custom

## urls.py

![](assets/2023-04-29-22-08-12-image.png)

## views.py

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-29-20-38-16-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-29-20-38-28-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-29-20-39-06-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-29-20-39-19-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-29-20-39-35-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-29-20-39-49-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-29-20-40-50-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-29-20-41-01-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-29-20-42-03-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-29-20-43-39-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-29-20-43-58-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-29-20-47-14-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-29-20-47-34-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-29-20-47-46-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-29-20-44-35-image.png)<img title="" src="file:///C:/Users/jin47/AppData/Roaming/marktext/images/2023-04-29-20-44-56-image.png" alt="" width="343"><img title="" src="file:///C:/Users/jin47/AppData/Roaming/marktext/images/2023-04-29-20-45-12-image.png" alt="" width="299">![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-29-20-46-02-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-29-20-46-18-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-29-20-46-37-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-29-20-48-13-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-29-20-48-30-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-29-20-49-04-image.png)<img title="" src="file:///C:/Users/jin47/AppData/Roaming/marktext/images/2023-04-29-20-50-28-image.png" alt="" width="310"><img src="file:///C:/Users/jin47/AppData/Roaming/marktext/images/2023-04-29-20-50-42-image.png" title="" alt="" width="340">![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-29-20-51-46-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-29-20-52-11-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-29-20-53-07-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-29-20-53-21-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-29-20-53-31-image.png)![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-29-20-53-57-image.png)

## decorator / mixin

##### Process to deal with request

<img src="assets/2023-04-30-09-52-30-image.png" title="" alt="" width="547">

![](assets/2023-04-30-09-53-32-image.png)![](assets/2023-04-30-09-53-55-image.png)![](assets/2023-04-30-09-54-12-image.png)![](assets/2023-04-30-09-54-40-image.png)![](assets/2023-04-30-09-55-21-image.png)![](assets/2023-04-30-09-55-36-image.png)![](assets/2023-04-30-09-55-54-image.png)![](assets/2023-04-30-09-56-11-image.png)![](assets/2023-04-30-09-56-40-image.png)![](assets/2023-04-30-09-57-04-image.png)![](assets/2023-04-30-09-57-19-image.png)![](assets/2023-04-30-09-57-34-image.png)![](assets/2023-04-30-09-57-56-image.png)

![](assets/2023-04-30-10-00-09-image.png)

![](assets/2023-04-30-10-00-46-image.png)![](assets/2023-04-30-10-01-02-image.png)![](assets/2023-04-30-10-01-32-image.png)<img src="assets/2023-04-30-10-02-05-image.png" title="" alt="" width="291"><img src="assets/2023-04-30-10-02-23-image.png" title="" alt="" width="352">![](assets/2023-04-30-10-02-55-image.png)

### django-braces

#### Access Mixxin

![](assets/2023-04-30-10-03-19-image.png)![](assets/2023-04-30-10-03-48-image.png)

```bash
pip install django-braces
```

![](assets/2023-04-30-10-05-27-image.png)![](assets/2023-04-30-10-06-07-image.png)

```python
# views.py

from braces.views import LoginRequiredMixin

class ReviewCreteView(LoginRequiredMixin, CreateView):
    ...
```

![](assets/2023-04-30-10-08-53-image.png)![](assets/2023-04-30-10-10-21-image.png)

![](assets/2023-04-30-10-10-49-image.png)![](assets/2023-04-30-10-12-31-image.png)

![](assets/2023-04-30-10-16-14-image.png)![](assets/2023-04-30-10-16-43-image.png)

```python
# settings.py

LOGIN_URL = "account_login"
```

![](assets/2023-04-30-10-21-17-image.png)![](assets/2023-04-30-10-21-44-image.png)![](assets/2023-04-30-10-22-05-image.png)

![](assets/2023-04-30-10-22-32-image.png)![](assets/2023-04-30-10-23-06-image.png)![](assets/2023-04-30-10-25-36-image.png)![](assets/2023-04-30-10-26-20-image.png)![](assets/2023-04-30-10-26-45-image.png)

![](assets/2023-04-30-10-28-45-image.png)![](assets/2023-04-30-10-31-32-image.png)![](assets/2023-04-30-10-31-56-image.png)<img title="" src="assets/2023-04-30-10-32-16-image.png" alt="" width="398"><img title="" src="assets/2023-04-30-10-32-52-image.png" alt="" width="306"><img src="assets/2023-04-30-10-33-12-image.png" title="" alt="" width="615">

---

#### UserPassesTextMixin

##### verify email certification

![](assets/2023-04-30-10-58-32-image.png)![](assets/2023-04-30-10-56-24-image.png)![](assets/2023-04-30-10-56-58-image.png)<img src="assets/2023-04-30-10-57-22-image.png" title="" alt="" width="206">![](assets/2023-04-30-11-01-18-image.png)

```python
# views.py

from braces.views import UserPassesTestMixin

class ReviewCreteView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    ...
```

![](assets/2023-04-30-11-03-50-image.png)![](assets/2023-04-30-11-04-08-image.png)![](assets/2023-04-30-11-04-23-image.png)

![](assets/2023-04-30-11-04-56-image.png)![](assets/2023-04-30-11-05-09-image.png)

```python
# views.py

from braces.views import UserPassesTestMixin

class ReviewCreteView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    ...
    def test_func(self, user):
        
```

![](assets/2023-04-30-11-07-06-image.png)![](assets/2023-04-30-11-07-23-image.png)![](assets/2023-04-30-11-08-20-image.png)![](assets/2023-04-30-11-09-39-image.png)

```python
# views.py

from braces.views import UserPassesTestMixin
from allauth.account.models import EmailAddress

class ReviewCreteView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    ...
    def test_func(self, user):
       if EmailAddress.objects.filter(user=user, verified=True).exists():
```

<img title="" src="assets/2023-04-30-11-12-34-image.png" alt="" width="96"><img src="assets/2023-04-30-11-12-50-image.png" title="" alt="" width="547">![](assets/2023-04-30-11-13-27-image.png)![](assets/2023-04-30-11-15-30-image.png)![](assets/2023-04-30-11-17-30-image.png)![](assets/2023-04-30-11-17-49-image.png)

```python
# views.py

from braces.views import UserPassesTestMixin
from allauth.account.models import EmailAddress

class ReviewCreteView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    ...
    def test_func(self, user):
       if EmailAddress.objects.filter(user=user, verified=True).exists():
            return True
       else:
            return False
# Email--exists() return the boolen, so..

    def test_func(self, user):
       return EmailAddress.objects.filter(user=user, verified=True).exits
```

### Control process, if User can't pass the Mixin

**Make process going login page or sending certicate email**

![](assets/2023-04-30-13-36-00-image.png)![](assets/2023-04-30-13-36-56-image.png)

![](assets/2023-04-30-13-37-49-image.png)![](assets/2023-04-30-13-39-15-image.png)![](assets/2023-04-30-13-39-32-image.png)![](assets/2023-04-30-13-39-52-image.png)

**redirect_unauthenticated_users**

![](assets/2023-04-30-13-46-34-image.png)

**raise_exception**

![](assets/2023-04-30-14-22-02-image.png)

<img title="" src="assets/2023-04-30-14-24-56-image.png" alt="" width="383"><img title="" src="assets/2023-04-30-14-25-12-image.png" alt="" width="251">

**urls.py**

![](assets/2023-04-30-14-26-45-image.png)![](assets/2023-04-30-14-43-15-image.png)![](assets/2023-04-30-14-44-34-image.png)![](assets/2023-04-30-14-45-11-image.png)![](assets/2023-04-30-14-47-47-image.png)![](assets/2023-04-30-14-50-19-image.png)![](assets/2023-04-30-14-50-46-image.png)![](assets/2023-04-30-14-52-32-image.png)![](assets/2023-04-30-14-49-05-image.png)

```python
# functions.py

from django.shortcuts import redirect
from allauth.account.utils import send_email_confirmation

def confirmation_required_redirect(self, request):
    send_email_confirmation(request, request.user)
    return redirect("account_email_conirmation_required")
```

![](assets/2023-04-30-14-55-41-image.png)![](assets/2023-04-30-14-56-11-image.png)![](assets/2023-04-30-14-56-27-image.png)![](assets/2023-04-30-14-56-51-image.png)![](assets/2023-04-30-14-57-08-image.png)![](assets/2023-04-30-14-57-28-image.png)![](assets/2023-04-30-14-58-52-image.png)![](assets/2023-04-30-15-00-36-image.png)

## Final code

```python
# views.py

from .functions import confirmation_reuired_redirect
from braces.views import LoginRequiredMixin, UserPassesTestMixin
from allauth.account.models import EmailAddress

class ReviewCreteView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
  model = Review
  form_class = ReviewForm
  template_name = "coplate/review_form.html"

  redirect_unauthenticated_users = True
  raise_exception = confirmation_required_redirect

  def form_valid(self, form):
     form.nstance.author = self.request.user
     return super().form_valid(form)
  def get_success_url(self)L
     return reverse("review-detail", kwargs={"review_id":self.object.id})
  def test_func(self, user):
     return EmailAddress.objects.filter(user=user,verified=True).exists()
```

![](assets/2023-04-30-15-11-24-image.png)![](assets/2023-04-30-15-11-40-image.png)![](assets/2023-04-30-15-12-26-image.png)![](assets/2023-04-30-15-11-57-image.png)![](assets/2023-04-30-15-16-03-image.png)![](assets/2023-04-30-15-13-34-image.png)![](assets/2023-04-30-15-17-42-image.png)![](assets/2023-04-30-15-18-08-image.png)![](assets/2023-04-30-15-18-22-image.png)![](assets/2023-04-30-15-18-39-image.png)![](assets/2023-04-30-15-21-46-image.png)![](assets/2023-04-30-15-28-54-image.png)

---

# UpdateView_Custom

**urls.py**

![](assets/2023-04-29-22-09-01-image.png)

**views.py**

![](assets/2023-04-29-21-16-12-image.png)![](assets/2023-04-29-21-16-26-image.png)

```python
# views.py

from django.views.generic import UpdateView

class ReviewUdateView(UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = "coplate.review_form.html"
    pk_url_kwarg = "review_id"

    def get_success_url(self)
        return reverse("review-detail", 
            kwargs={"review_id":self.object.id})
```

<img title="" src="assets/2023-04-29-21-21-08-image.png" alt="" width="365"><img title="" src="assets/2023-04-29-21-21-21-image.png" alt="" width="285">![](assets/2023-04-29-21-25-03-image.png)![](assets/2023-04-29-21-25-19-image.png)![](assets/2023-04-29-21-25-42-image.png)![](assets/2023-04-29-21-24-26-image.png)![](assets/2023-04-29-21-26-19-image.png)![](assets/2023-04-29-21-26-31-image.png)![](assets/2023-04-29-21-27-55-image.png)![](assets/2023-04-29-21-28-07-image.png)

**template**

![](assets/2023-04-29-21-40-20-image.png)![](assets/2023-04-29-21-41-45-image.png)![](assets/2023-04-29-21-42-17-image.png)![](assets/2023-04-29-21-43-34-image.png)![](assets/2023-04-29-21-43-56-image.png)![](assets/2023-04-29-21-50-24-image.png)

![](assets/2023-04-29-21-53-59-image.png)<img title="" src="assets/2023-04-29-21-54-30-image.png" alt="" width="356"><img title="" src="assets/2023-04-29-21-54-50-image.png" alt="" width="291">![](assets/2023-04-29-21-56-00-image.png)<img title="" src="assets/2023-04-29-21-56-19-image.png" alt="" width="240">![](assets/2023-04-29-21-57-14-image.png)![](assets/2023-04-29-21-57-34-image.png)![](assets/2023-04-29-21-59-05-image.png)

![](assets/2023-04-29-22-01-21-image.png)

![](assets/2023-04-29-22-00-59-image.png)![](assets/2023-04-29-22-02-00-image.png)![](assets/2023-04-29-22-02-22-image.png)![](assets/2023-04-29-22-03-11-image.png)![](assets/2023-04-29-22-03-37-image.png)![](assets/2023-04-29-22-04-01-image.png)![](assets/2023-04-29-22-04-40-image.png)

## Mixin

![](assets/2023-04-30-15-42-22-image.png)![](assets/2023-04-30-15-43-47-image.png)![](assets/2023-04-30-15-42-54-image.png)![](assets/2023-04-30-15-49-47-image.png)

![](assets/2023-04-30-15-51-42-image.png)![](assets/2023-04-30-15-52-03-image.png)![](assets/2023-04-30-15-55-52-image.png)![](assets/2023-04-30-15-57-48-image.png)<img title="" src="assets/2023-04-30-15-58-13-image.png" alt="" width="239"><img title="" src="assets/2023-04-30-15-58-27-image.png" alt="" width="400">![](assets/2023-04-30-15-59-19-image.png)![](assets/2023-04-30-16-01-41-image.png)

```python
# views.py

from django.views.generic import UpdateView
from braces.views import LoginRequiredMixin, UserPassesTestMixin

class ReviewUdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = "coplate.review_form.html"
    pk_url_kwarg = "review_id"

    raise_exception = True    

    def get_success_url(self)
        return reverse("review-detail", 
            kwargs={"review_id":self.object.id})

    def test_func(self, user):
        review = self.get_object()
        return review.author == uwer
```

![](assets/2023-04-30-16-05-02-image.png)

![](assets/2023-04-30-16-08-43-image.png)<img title="" src="assets/2023-04-30-16-42-02-image.png" alt="" width="245"><img title="" src="assets/2023-04-30-16-42-36-image.png" alt="" width="404">![](assets/2023-04-30-16-44-01-image.png)![](assets/2023-04-30-16-44-17-image.png)<img title="" src="assets/2023-04-30-16-45-26-image.png" alt="" width="647">![](assets/2023-04-30-16-46-12-image.png)<img title="" src="assets/2023-04-30-16-47-57-image.png" alt="" width="321"><img title="" src="assets/2023-04-30-16-48-15-image.png" alt="" width="324">![](assets/2023-04-30-16-48-50-image.png)![](assets/2023-04-30-16-52-19-image.png)

---

# deleteView Custom

**urls.py**

![](assets/2023-04-29-22-10-16-image.png)

**views.py**

![](assets/2023-04-29-22-11-45-image.png)

**template**

```html
{% extends "base.html" %}

{% block content %}

<form method="post">
    {% csrf_token %}
    <span> really want delete review? </span>
    <button type="submit">delete</button>
    <a href="{% url 'review-detail' review.id %}">cancel</a>
</form>

{% endblock %}
```

![](assets/2023-04-30-09-44-36-image.png)![](assets/2023-04-30-09-44-52-image.png)

## Mixin

<img title="" src="assets/2023-04-30-16-53-49-image.png" alt="" width="127"><img title="" src="assets/2023-04-30-16-54-00-image.png" alt="" width="513">

```python
# views.py

from django.views.generic import deleteView
from braces.views import LoginRequiredMixin, UserPassesTestMixin

class ReviewUdateView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Review
    form_class = ReviewForm
    template_name = "coplate.review_confirm_delete.html"
    pk_url_kwarg = "review_id"

    raise_exception = True    

    def get_success_url(self)
        return reverse("review-detail", 
            kwargs={"review_id":self.object.id})

    def test_func(self, user):
        review = self.get_object()
        return review.author == uwer
```

# DetailView

![](assets/2023-04-30-23-44-42-image.png)

**urls.py**

```python
urlpatterns = [
    ...
    path("user/<int:user_id>/", views.ProfileView.as_view(), 
    name="profile"),
    ...
]
```

**views.py**

![](assets/2023-04-30-23-47-39-image.png)![](assets/2023-04-30-23-44-19-image.png)![](assets/2023-04-30-23-48-33-image.png)![](assets/2023-04-30-23-48-50-image.png)![](assets/2023-04-30-23-49-06-image.png)![](assets/2023-04-30-23-49-20-image.png)

```python
from django.views.generic import DetailView

class ProfileView(DetailView):
    model = User
    template_name = "coplate/profile.html"
    pk_url_kwarg = "user_id"
    context_object_name = "profile_user"
```

![](assets/2023-04-30-23-50-09-image.png)![](assets/2023-04-30-23-50-58-image.png)![](assets/2023-04-30-23-51-22-image.png)

![](assets/2023-04-30-23-54-41-image.png)<img title="" src="assets/2023-04-30-23-55-12-image.png" alt="" width="291"><img title="" src="assets/2023-04-30-23-55-31-image.png" alt="" width="349">![](file://C:\Users\jin47\OneDrive\바탕 화면\TIL\django\assets\2023-04-30-23-51-22-image.png?msec=1682866282399)

![2023-04-30-23-56-37-image.png](C:\Users\jin47\OneDrive\바탕%20화면\TIL\django\assets\2023-04-30-23-56-37-image.png)<img title="" src="assets/2023-05-01-00-02-59-image.png" alt="" width="309">  <img title="" src="assets/2023-05-01-00-03-27-image.png" alt="" width="253"><img title="" src="assets/2023-05-01-00-04-11-image.png" alt="" width="330"><img title="" src="assets/2023-05-01-00-05-17-image.png" alt="" width="317">![](assets/2023-05-01-00-06-37-image.png)

```python
from django.views.generic import DetailView

class ProfileView(DetailView):
    model = User
    template_name = "coplate/profile.html"
    pk_url_kwarg = "user_id"
    context_object_name = "profile_user"

    def get_conext_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.kwargs.get("user_id")
        context["user_reviews"] = (
            Review.objects.filter(author__id).order_by("-dt_created")[:4]
        )
        return context
```

<img title="" src="assets/2023-05-01-00-09-27-image.png" alt="" width="238"><img title="" src="assets/2023-05-01-00-09-41-image.png" alt="" width="404">



# ListView Custom

특정 유저가 가지고 있는 리뷰만 전달하고 싶을 때
(=listView가 전달하는 object를 바꾸고 싶으면)
get_queryset이란 메소드를 오버라이드 해주면 된다

```python
# views.py
class UserReviewListView(ListView):
    model = Review
    template_name = "coplate/user_review_list.html"
    context_object_name = "user_reviews"
    paginate_by = 4

    # 원래는 리뷰 전체 모델오브젝트를 다 가져오는데
    # 그걸 메소드를 오버라이딩 해서 특정 유저가 작성한 리뷰만 리턴하도록 함
    def get_queryset(self):
        user_id = self.kwargs.get("user_id")
        return Review.objects.filter(author__id=user_id).order_by("dt_created")
```

리스트뷰에 컨텍스트로 리뷰만 전달되고 리뷰의 작성자가 전달되지 않아
작성자도 전달하려고 함 => get_context_data 메소드 오버라이드

```python
# views.py
from django.shortcuts import get_object_or_404

class UserReviewListView(ListView):
    model = Review
    template_name = "coplate/user_review_list.html"
    context_object_name = "user_reviews"
    paginate_by = 4

    # 원래는 리뷰 전체 모델오브젝트를 다 가져오는데
    # 그걸 메소드를 오버라이딩 해서 특정 유저가 작성한 리뷰만 리턴하도록 함
    def get_queryset(self):
        user_id = self.kwargs.get("user_id")
        return Review.objects.filter(author__id=user_id).order_by("dt_created")
        # 메소드를 정의하고 기존의 컨텍스트를 가져와서 그대로 전달
    def context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 찾는 유저가 없으면 404 에러를 냄
        # get_object_or_404(오브젝트를 찾을 모델, 찾을때 조건)
        # 함수가 조회한 유저를 등록함
        context["profile_user"]=
        get_object_or_404(User, id=self.kwargs.get("user_id"))
        return context
```

**template** 리뷰 쓴 총개수를 알고 싶을 때 쓴다

```html
{{ paginator.count }}
```

# UpdateView Custom

**urls.py**

```python
url_pattern = [
    ...
    path("set-profile/",
        views.ProfileSetView.as_view(),
        name="profile-set"),
]
```

**views.py** 프로필정보 설정페이지는 생성 되어있는 유저오브젝트에 프로필에 관련된 필드를 설정해주는 역할이기 때문에 updateview

보통 updateview는 어떤 오브젝트를 업데이트 할 지 알고
이 오브젝트 아이디가 url에 전달되고 
pk_url_kwarg를 이용해서 설정해 주는데
유저 아이디가 url로 전달되지 않음, 업데이트할 유저는 현재 들어와 있는 유저이기 때문
업데이트를 해야 할 오브젝트를 updateview에 알려줄 수 있는 것이
get_object 메소드 임

업데이트 하고 나서 리디렉트 할 url 적어줘야 함

```python
# views.py
from .forms import ProfileForm

class ProfileSetView(UpdateView):
    model = User
    form_class = ProfileForm
    template_name = "coplate/profile_set_form.html"    

    # 여기서 현재 유저를 리턴해주면 됨
    def get_object(self, queryset=None):
        # 현재 유저를 돌려줌
        return self.request.user

    def get_success_url(self):
        return reverse("index")
```

ListView는 여러 오브젝트를 다루니까 get_queryset 메소드 오버라이드
UpdateView는 한 오브젝트를 다루니까 get_object 메소드 오버라이드
=> 따라서 하나의 오브젝트를 다루는 detailview, createview, deleteview 모두 get_object 메소드를 오버라이드 할 수 있다

```python
# forms.py
class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "nickname", "profile_pic", "intro",
        ]
        widgets = {
            "intro": forms.Textarea,
        }
```
