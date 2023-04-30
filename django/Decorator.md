# Decorator

![](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=4834&directory=pic1.png&name=pic1.png)

접근 제어에 대해 처음으로 배울 때 함수형 뷰에는 decorator를 쓰고, 클래스형 뷰에는 mixin을 쓴다고 했습니다. 우리는 클래스형 뷰를 사용하기 때문에 이번 챕터에서는 AccessMixin을 활용해 봤는데요. 이번 레슨에서는 decorator에 대해 간단히 설명드릴게요. Decorator를 어떻게 사용하는지 참고만 하시면 좋을 것 같습니다.

Decorator도 mixin과 비슷하게 '유저가 뷰에 접근할 수 있는지'를 확인하는 로직을 뷰에 추가해 줍니다. 하지만 사용법은 mixin과 조금 다른데요. 우선 접근 관련 decorator는 django.contrib.auth 앱에서 찾올 수 있습니다. (django-braces는 django 관련 mixin만 제공합니다.)

`LoginRequiredMixin`과 비슷한 역할을 하는 `login_required` decorator가 있는데, 아래와 같이 임포트할 수 있습니다.

```python
from django.contrib.auth.decorators import login_required
```

그리고 decorator를 뷰 위에 달아주면 됩니다.

```python
# views.py
from django.contrib.auth.decorators import login_required

@login_required
def my_view(request):
    ...
```

그러면 로그인이 안 돼있는데 `my_view`를 접근하려고 하면 로그인 페이지(settings 파일의 `LOGIN_URL`에 해당하는 URL)로 리디렉트됩니다.

참고로 decorator는 뷰를 정의할 때가 아닌 URL 패턴을 정의할 때 사용할 수도 있는데요.

```python
# views.py
def my_view(request):
    ...

class YourView(View):
    ...

# urls.py
from django.contrib.auth.decorators import login_required

from .views import my_view, YourView

urlpatterns = [
    path('my/url/', login_required(my_view), name='my_url'),
    path('your/url/', login_required(YourView.as_view()), name='your_url'),
]
```

뷰를 decorator로 감싸주면 됩니다. (`YourView`는 클래스형 뷰지만 `.as_view()` 메소드를 적용해 주면 decorator를 사용할 수 있습니다.) 위와 같은 방식도 많이 사용됩니다. 뷰를 직접 정의하는 것이 아니라 뷰를 임포트해서 URL 패턴에 사용한다면 유용할 수 있겠죠?

`UserPassesTestMixin`과 비슷한 `user_passes_test` decorator도 있는데요. `user_passes_test`는 뷰에 접근하지 못하는 유저를 처리하는 로직을 커스터마이즈할 수 없다는 단점이 있습니다. `user_passes_test`는 뷰에 접근하지 못하는 유저를 어떤 URL로 리디렉트하는 로직밖에 구현할 수 없습니다. (자세한 사용법은 [링크](https://docs.djangoproject.com/en/2.2/topics/auth/default/#limiting-access-to-logged-in-users-that-pass-a-test)를 참고하세요!) 다른 로직이 필요하다면 로직을 함수형 뷰 안에 직접 넣거나 클래스형 뷰를 사용해야겠죠?
