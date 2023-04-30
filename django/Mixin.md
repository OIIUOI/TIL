# Mixin이란?

Mixin은 파이썬의 일반적인 개념인데, 기존의 클래스에 어떤 기능을 더해줄 때 쓰입니다. 우리의 경우 mixin을 활용해서 뷰 클래스에 접근 제어 기능을 더해줬습니다.

우리는 django-braces(링크 추가)라는 패키지를 사용했는데요. django-braces는 사실 django에서 사용할 수 있는 다양한 mixin을 제공합니다. 우리는 그중에서 `LoginRequiredMixin`과 `UserPassesTestMixin`을 사용해 봤습니다.

# `LoginRequiredMixin`

`LoginRequiredMixin`은 로그인이 돼있는 유저만 뷰에 접근할 수 있게 해 줍니다. 로그인 여부를 확인하는 로직이 뷰 로직보다 먼저 실행돼야 하기 때문에 제네릭 뷰 왼쪽에 씁니다.

```python
class MyView(LoginRequiredMixin, CreateView):
    ...
```

로그인이 안 돼있으면 로그인 페이지(settings 파일의 `LOGIN_URL`에 해당하는 URL)로 리디렉트되고, 로그인을 한 후에는 원래 가려고 하던 페이지로 또다시 리디렉트됩니다.

# `UserPassesTestMixin`

(로그인 여부가 아닌) 어떤 특정 조건을 충족하는지 확인하고 싶을 때는 `UserPassesTestMixin`을 씁니다. `UserPassesTestMixin`은 우리가 정의하는 커스텀 테스트 (`test_func`)를 통과하는 유저만 뷰에 접근할 수 있게 해 줍니다.

`UserPassesTestMixin`을 따로 쓸 수도 있지만, 보통 유저가 로그인이 돼있는지를 먼저 확인하기 때문에 (그래야 그 유저에 대한 여러 가지 조건을 확인할 수 있겠죠?) `LoginRequiredMixin`과 같이 씁니다. `LoginRequiredMixin` 오른쪽, 제네릭 뷰 왼쪽에 써 주시면 됩니다.

```python
class MyView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    ...
```

## `test_func`

`test_func`는 뷰에 접근할 수 있으면 `True`, 없으면 `False`를 리턴합니다.

```python
class MyView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    def test_func(self, user):
        if <condition>:
            return True
        else:
            return False
```

이걸 더 간단히 써 줄 수도 있고요.

```python
class MyView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    def test_func(self, user):
        return <condition>
```

## 뷰에 접근하지 못하는 유저들 처리하기

뷰에 접근하지 못하는 유저가 처리되는 방식을 제어하기 위해서는 두 가지 속성을 사용합니다.

1. `redirect_unauthenticated_users`

뷰에 접근하지 못하는 유저들 중, 로그인 돼있는 유저와 로그인이 안 돼있는 유저를 다르게 처리할 것인지를 정하는 속성입니다. 이걸 `True`로 하면, 로그인이 안 돼있는 유저는 로그인 페이지로 리디렉트되고, 로그인 돼있는 유저는 `raise_exception` 속성의 값에 따라 처리 방식이 정해집니다. 반대로 이걸 `False`로 하면, 로그인 돼있는 유저 안 돼있는 유저 모두 `raise_exception` 속성의 값에 따라 처리됩니다.

2. `raise_exception`

`raise_exception`에 가장 흔히 사용되는 값은 `True`와 커스텀 함수인데요. `raise_exception`을 `True`로 설정해 주면 유저가 뷰에 접근할 수 없을 경우 403 Forbidden(권한 없음, 금지됨) 오류가 나고, 커스텀 함수로 설정해 주면 그 함수가 그대로 실행됩니다.

```python
def some_func(self, request):
    # 필요한 로직 수행
    return redirect('some_url')

class ReviewCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    ...   
    raise_exception = some_func
```

커스텀 함수는 `self`와 `request`를 파라미터로 받아야 합니다.
