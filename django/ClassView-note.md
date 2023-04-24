# Generic View 정리하기

Django에서 제공하는 제네릭 뷰는 역할에 따라 크게 네 가지로 나누어져 있습니다. 우리는 각각 로직에 맞는 기능을 편하게 구현할 수 있게 하는 클래스 변수와 메소드를 이용해서 정해진 틀에 따라 구현을 해야 하는데 처음에는 이런 부분들이 조금 생소하게 느껴질 수 있지만 필요할 때마다 하나씩 사용하다 보면 금방 익숙해지실 거에요.

| 종류            | 뷰                                                                         | 설명                                                                                                                                |
| ------------- | ------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| Base Views    | TemplateView<br>RedirectView                                              | 템플릿을 랜더해서 결과로 돌려주거나 다른 URL로 리디렉션 하는등의 기본적인 기능을 하는 뷰                                                                               |
| Display Views | ListView<br>DetailView                                                    | 데이터를 보여주는 기능을 하는 뷰                                                                                                                |
| Edit Views    | FormView<br>CreateView<br>UpdateView<br>DeleteView                        | 데이터 생성, 수정, 삭제등의 기능을 하는 뷰                                                                                                         |
| Date Views    | YearArchiveView<br>MonthArchiveView<br>DayArchiveView<br>TodayArchiveView | 날짜를 중심으로 데이터를 조회하는 기능을 하는 뷰<br>[Date Views 문서보기](https://docs.djangoproject.com/en/2.2/ref/class-based-views/generic-date-based/) |

아래는 우리가 강의에서 함께 구현해 보았던 제네릭 뷰의 각 속성들을 정리해놓은 것 입니다. 내가 구현하려하는 뷰가 CRUD 로직에 해당하는 뷰라면 제네릭뷰 사용을 꼭 고려해 보세요.

# Base Views

[Base Views 문서 바로가기](https://docs.djangoproject.com/en/2.2/ref/class-based-views/base/)

## RedirectView

RedirectView는 들어온 요청을 새로운 URL로 이동시키는 기능을 합니다.

| 속성           | 설명                  | 기본값   |
| ------------ | ------------------- | ----- |
| url          | 이동할 URL을 지정하는 속성    | None  |
| pattern_name | URL 패턴의 이름을 지정하는 속성 | None  |
| query_string | 쿼리 스트링을 전달할 지 여부    | False |

## TemplateView

TemplateView는 주어진 템플릿을 렌더링해서 보여주는 기능을 합니다.

| 속성            | 설명               | 기본값  |
| ------------- | ---------------- | ---- |
| template_name | 렌더할 템플릿을 지정하는 속성 | None |

# Display Views

[Display Views 문서 바로가기](https://docs.djangoproject.com/en/2.2/ref/class-based-views/generic-display/)

## DetailView

DetailView는 하나의 데이터를 보여주는 기능을 합니다. 우리가 같이해봤던 '상세 보기'를 생각하면 됩니다.

| 속성                  | 설명                                                         | 기본값            |
| ------------------- | ---------------------------------------------------------- | -------------- |
| model               | 사용할 모델 지정                                                  | None           |
| pk_url_kwarg        | 보여주기 위한 단일 데이터를 조회할 때 사용할 키워드 인수 지정 (urls.py에서 지정한 키워드 인수) | 'pk'           |
| template_name       | 렌더할 템플릿을 지정하는 속성                                           | None           |
| context_object_name | 템플릿으로 전달할 모델의 context 키워드 지정                               | '<model_name>' |

## ListView

ListView는 여러 데이터를 보여주는 기능을 합니다. 우리가 같이해봤던 '목록 보기'를 생각하면 됩니다.

| 속성                  | 설명                               | 기본값                 |
| ------------------- | -------------------------------- | ------------------- |
| model               | 사용할 모델 지정                        | None                |
| ordering            | 데이터 정렬 속성 지정(order_by와 동일한 값 사용) | None                |
| paginate_by         | 페이지에 표시 할 데이터의 수                 | None                |
| page_kwarg          | 쿼리스트링으로부터 가져올 현재 페이지에 대한 키워드     | ‘page’              |
| template_name       | 렌더할 템플릿을 지정하는 속성                 | None                |
| context_object_name | 템플릿으로 전달할 모델의 context 키워드 지정     | '<model_name>_list' |

# Editing Views

[Editing Views 문서 바로가기](https://docs.djangoproject.com/en/2.2/ref/class-based-views/generic-editing/)

## FormView

FormView는 Form을 렌더링해서 보여주는 기능을 하는 뷰입니다.

| 속성            | 설명                        | 기본값  |
| ------------- | ------------------------- | ---- |
| form_class    | 입력을 위한 Form Class를 지정합니다. | None |
| success_url   | 처리가 성공했을 때 리디렉션 할 URL을 지정 | None |
| template_name | 렌더할 템플릿을 지정하는 속성          | None |

## CreateView

Createview는 새로운 데이터를 생성을 위한 뷰입니다.

| 속성            | 설명                                                        | 기본값  |
| ------------- | --------------------------------------------------------- | ---- |
| model         | 사용할 모델 지정                                                 | None |
| form_class    | 입력을 위한 Form Class를 지정합니다.                                 | None |
| fields        | 데이터 입력에 사용할 필드를 명시적으로 지정합니다.                              | None |
| template_name | 렌더할 템플릿을 지정하는 속성                                          | None |
| pk_url_kwarg  | 보여주기 위한 단일 데이터를 조회할 때 사용할 키워드 인수 지정 urls.py에서 지정한 키워드 인수) | 'pk' |
| success_url   | 처리가 성공했을 때 리디렉션 할 URL을 지정                                 | None |

## UpdateView

UpdateView는 기존 데이터 개체의 수정을 위한 뷰입니다.

| 속성                  | 설명                                                         | 기본값          |
| ------------------- | ---------------------------------------------------------- | ------------ |
| model               | 사용할 모델 지정                                                  | None         |
| form_class          | 입력을 위한 Form Class를 지정합니다.                                  | None         |
| field               | 데이터 입력에 사용할 필드를 명시적으로 지정합니다.                               | None         |
| template_name       | 렌더할 템플릿을 지정하는 속성                                           | None         |
| pk_url_kwarg        | 보여주기 위한 단일 데이터를 조회할 때 사용할 키워드 인수 지정 (urls.py에서 지정한 키워드 인수) | ‘pk’         |
| success_url         | 처리가 성공했을 때 리디렉션 할 URL을 지정                                  | None         |
| context_object_name | 템플릿으로 전달할 모델의 context 키워드 지정                               | <model_name> |

## DeleteView

DeleteView는 기존 데이터를 삭제하는 기능을 위한 뷰입니다.

| 속성                  | 설명                                                         | 기본값          |
| ------------------- | ---------------------------------------------------------- | ------------ |
| model               | 사용할 모델 지정                                                  | None         |
| template_name       | 렌더할 템플릿을 지정하는 속성                                           | None         |
| pk_url_kwarg        | 보여주기 위한 단일 데이터를 조회할 때 사용할 키워드 인수 지정 (urls.py에서 지정한 키워드 인수) | ‘pk’         |
| success_url         | 처리가 성공했을 때 리디렉션 할 URL을 지정                                  | None         |
| context_object_name | 템플릿으로 전달할 모델의 context 키워드 지정                               | <model_name> |

# Context 정리하기

Context는 View에서 Template으로 전달되어 렌더링시 사용할 수 있는 사전형 데이터 변수입니다. 앞에서 함수형 뷰를 사용할 때 render 함수의 세 번째 파라미터로 넘겨서 사용했었죠.

```python
def function_view(request):
    return render(request, template_name, context)
```

Django의 Generic 뷰는 이러한 Context를 각각의 기능에 맞게 자동으로 Template에 전달합니다. 헷갈릴 수 있는 부분이니까 우리가 사용했던 CRUD를 중심으로 정리해보겠습니다.

## 모델(Model) 데이터

기본적으로 모델(Model) 데이터는 Template에 context로 전달됩니다. 하나의 데이터를 다루는 View는 하나의 데이터를 'object'라는 키워드로 전달하고 여러개의 데이터를 다루는 View는 'object_list'라는 키워드로 전달합니다. 그리고 같은 데이터를 'model' 클래스 변수에 명시한 Model을 보고 소문자로 변형해 함께 전달합니다. 아래 예시를 보면서 이해해봅시다.

```python
from django.views.generic import DetailView
from .models import Post

class PostDetailView(DetailView):
    model = Post
    ...
```

DetailView는 하나의 데이터를 다루는 로직을 수행합니다. 그래서 위처럼 model 클래스 변수를 지정하면 자동으로 ‘object’라는 키워드로 데이터베이스에서 조회한 하나의 Post 데이터를 Template에 전달합니다. 그러면 Template에서는 템플릿 변수를 사용해서 {{object.title}} 같은 형태로 접근할 수 있는거죠. 그리고 이 object와 똑같은 데이터를 모델명을 소문자로 쓴 형태인 `post`로도 Template에 함께 전달합니다. 그러니까 같은 데이터가 `object`와 `post` 두 개의 키워드로 전달되는거죠. 이렇게 되면 우리는 Template에서 조금 더 직관적인 {{post.title}} 같은 형태로 사용할 수 있습니다.

```python
from django.views.generic import ListView
from .models import Post

class PostListView(ListView):
    model = Post
    ...
```

자, 이번에는 ListView를 예로 들어볼게요. ListView는 여러 데이터를 다루는 로직을 수행하죠? 그래서 model 클래스 변수를 지정하면 자동으로 데이터베이스에서 조회한 Post 데이터 목록을 `object_list`라는 키워드로 Template에 전달합니다. 그리고 이때 똑같은 데이터를 model 키워드 변수에 명시된 모델을 참고하여 소문자로 쓴 형태인 `<model_name>_list` 즉 `post_list` 키워드로도 context를 전달합니다. 그러니까 Template에서는 `object_list`와 `post_list` 두 개의 키워드로 Post 데이터 목록에 접근할 수 있는겁니다.

## context_obejct_name

자, 그러면 context_object_name 클래스 변수는 무엇을 지정해주는 걸까요? 위에서 설명한 context 중 바로 모델명을 보고 유추하는 `<model_name>` 또는 `<model_name>_list` 같은 이름들을 바꿔주는 것 입니다. Django가 알아서 모델명을 보고 유추해서 넘겨주는 context 이름을 커스터마이징 할 수 있는거죠. 이것도 예시를 보면서 이해해봅시다.

```python
from django.views.generic import ListView
from .models import Post

class PostListView(ListView):
    model = Post
     ...
```

이렇게 적으면 Post 데이터 목록이 `object_list`와 `post_list`라는 두 개의 키워드로 전달되겠죠? 그런데 이때 context_object_name을 아래와 같이 명시해주면

```python
from django.views.generic import ListView
from .models import Post

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    ...
```

`post_list` 가 `posts`로 변경되어 전달됩니다. 그러니까 Post 데이터목록이 `object_list`와 `posts` 두 개의 키워드로 전달되게 되는거죠. 이렇게 generic 뷰가 자동으로 모델을 보고 생성하는 context 키워드를 변경해 주는 것이 바로 context_object_name 입니다.

# 그 외 Context 목록

위에서 설명한 context 말고도 우리가 함께 사용해보았던 context도 있습니다. 당연히 이러한 context를 모두 외울 필요는 없고 '아, 그런것도 있었는데?' 정도의 경험을 갖는 것이 중요합니다. 실제 어떻게 구현해야하는지 형태가 무엇인지는 필요할 때 Django 공식 문서를 보고 찾아서 구현하면 됩니다.

## CreateView

| 키워드  | 설명                               |
| ---- | -------------------------------- |
| form | form_class 클래스 변수에 명시한 폼이 전달됩니다. |

## ListView

| 키워드          | 설명                               |
| ------------ | -------------------------------- |
| paginator    | Paginator 객체가 전달됩니다.             |
| page_obj     | 현재 Page 객체가 전달됩니다.               |
| is_paginated | 페이지네이션 적용 여부가 boolean 형으로 전달됩니다. |

## UpdateView

| 키워드  | 설명                               |
| ---- | -------------------------------- |
| form | form_class 클래스 변수에 명시한 폼이 전달됩니다. |

이번 레슨은 어땠나요?
