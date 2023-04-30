# `null` vs `blank`

`null`: `null`은 데이터베이스와 관련된 옵션입니다. `null`을 `True`로 설정해 주면, 필드에 해당하는 데이터베이스 컬럼에 NULL(데이터베이스에서 존재하지 않는 값을 의미함) 값을 허용하고, 필드에 대한 값이 없으면 데이터베이스에 NULL을 저장합니다. `null`의 디폴트 값은 `False`입니다.

`blank`: `blank`는 폼과 유효성 검사에 관련된 내용입니다. `blank`를 `True`로 설정해 주면 폼(어드민 페이지의 폼 포함)에서 필드에 대한 값을 입력해 주지 않아도 됩니다. 즉, 옵셔널(필수가 아닌) 필드가 됩니다.

여기까지는 이해하기가 쉬운데요, 문제는 모델 필드의 종류에 따라 `null`과 `blank`의 쓰임새가 달라집니다. 결론부터 정리해 드리자면:

1. 문자열 기반 필드를 옵셔널 필드로 만들고 싶다면 (필드에 "빈 값"을 허용하고 싶다면) `blank=True`를 사용합니다.

```python
# name 필드는 옵셔널 필드 (폼에서 작성하지 않아도 됨)

class Person(models.Model):
    name = models.CharField(max_length=20, blank=True)
```

하지만 `unique=True`(중복 금지) 옵션도 같이 사용하고 싶다면 `unique=True`, `null=True`, `blank=True` 모두 사용해야 합니다.

```python
# name 필드는 옵셔널 필드 (폼에서 작성하지 않아도 됨), 하지만 중복 금지

class Person(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True, unique=True)
```

2. 문자열 기반이 아닌 필드를 옵셔널 필드로 만들고 싶다면 `null=True`, `blank=True`를 사용합니다.

```python
# age 필드는 옵셔널 필드 (폼에서 작성하지 않아도 됨)

class Person(models.Model):
    age = models.IntegerField(blank=True, null=True)
```

`unique=True`(중복 금지) 옵션도 같이 사용하고 싶다면 `unique=True`, `null=True`, `blank=True` 모두 사용하시면 됩니다.

```python
# age 필드는 옵셔널 필드 (폼에서 작성하지 않아도 됨), 하지만 중복 금지

class Person(models.Model):
    age = models.IntegerField(blank=True, null=True, unique=True)
```

# 문자열 기반 필드

문자열 기반 필드는 문자열 데이터가 저장되는 필드를 말합니다. 가장 먼저 생각나는 필드는 `CharField`가 있겠지만 문자열이 이메일 주소인지 확인해 주는 `EmailField`, 문자열이 URL 주소인지 확인해 주는 `URLField`, 길이 제한이 없는 `TextField` 모두 문자열 기반 필드입니다. 그리고, 사실 `ImageField`도 문자열 기반 필드인데요. 결국 `ImageField`는 이미지의 URL을 저장하기 때문입니다. 우리가 이번 토픽에서 사용해왔던 대부분의 필드는 문자열 기반 필드입니다.

Django에서는 기본적으로 문자열 기반 필드에 대한 값이 없으면 데이터베이스에 빈 문자열(empty string) `""`을 저장합니다. 데이터베이스에 NULL 대신 `""`를 저장하기 때문에 필드를 옵셔널 필드로 만들어도 `null=True`가 필요 없는 거죠.

```python
# name 필드는 옵셔널 필드 (폼에서 작성하지 않아도 됨)

class Person(models.Model):
    name = models.CharField(max_length=20, blank=True)
```

위에서 봤던 예시에서 `name` 필드를 옵셔널 필드로 만들어 주었죠? 폼에서 `name`을 입력받지 않으면, 데이터베이스에 `""`가 저장됩니다.

그런데 옵셔널 필드에 `unique=True` 옵션도 사용하게 되면 문제가 생깁니다. 필드 값이 없는 오브젝트가 여러 개 있을 수 있는데, 빈 값을 모두 `""`로 저장하면 `""`가 중복되기 때문이죠. 그래서 데이터베이스에서 중복 오류가 납니다. 이럴 때는 `""` 대신 NULL을 사용해야 합니다. **NULL은 어떤 주어진 값으로 생각하지 않기 때문에 중복이 돼도 상관없습니다.**

```python
ID           name (blank=True, null=False, unique=True)
1            "우재"
2            ""
3            ""
4            "종훈"

# 중복 불가 오류

ID           name (blank=True, null=True, unique=True)
1            "우재"
2            NULL
3            NULL
4            "종훈"

# OK
```

# 문자열 기반이 아닌 필드

문자열 기반이 아닌 필드는 정수를 저장하는 `IntegerField`, 날짜와 시간을 저장하는 `DateTimeField` 같은 것들이 있습니다. 문자열이 아닌 데이터 타입에는 `""`같은 "빈 값"을 대표하는 값이 없기 때문에 필드에 대한 값이 없으면 데이터베이스에는 NULL을 저장하는 방법밖에 없습니다. 그래서 문자열 기반이 아닌 필드를 옵셔널 필드로 만들어 주고 싶다면 `blank=True`, `null=True`를 둘 다 사용해야 합니다.

```python
# age 필드는 옵셔널 필드 (폼에서 작성하지 않아도 됨)

class Person(models.Model):
    age = models.IntegerField(blank=True, null=True)
```

`age` 필드를 입력받지 않으면 데이터베이스에 NULL이 저장됩니다.
