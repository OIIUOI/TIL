이번 레슨은 꼭 듣지 않아도 되는 선택 레슨입니다. `Meta` 클래스에 어떤 옵션들을 사용할 수 있는지 살펴보고, 필요할 때 다시 읽어 보시기 바랍니다.

# `Meta`  클래스의 옵션들

## `model`

`model`은 `ModelSerializer` 클래스가 어떤 모델로 시리얼라이저를 생성할지 지정해 주는 필수 옵션입니다. 아래 코드와 같이 `Meta` 클래스 내부에 모델 이름을 작성해 주는 식으로 사용합니다.

```python
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie

```

## `fields`

`ModelSerializer`에서 어떤 필드를 사용할지 선언하는 옵션입니다. 아래와 같이 필요한 필드들의 이름을 `fields`에 작성하면 됩니다. 필드의 타입은 모델 필드의 타입을 보고 자동으로 유추합니다.

```python
# Movie 모델
class Movie(models.Model):
    name = models.CharField(max_length=30)
    opening_date = models.DateField()
    running_time = models.IntegerField()
    overview = models.TextField()

```

```python
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'name', 'opening_date', 'running_time', 'overview']

```

  

`fields`를 `__all__`로 해주면 모델에 존재하는 모든 필드를 사용할 수 있습니다.

```python
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

```

`fields`는 조건부 필수 옵션으로, `exclude`를 사용하지 않으면 필수로 입력해야 합니다.

## `exclude`

`fields`와 정반대인 옵션입니다. 모델을 기준으로 어떤 필드를 제외할지 나타냅니다. 모델에 총 5개의 필드가 있는데 시리얼라이저에서는 4개의 필드만 사용하고 싶다면 `exclude`로 하나의 필드를 제외할 수 있습니다.

아래의 두 `MovieSerializer`는 동일한 기능을 합니다.

```python
# id, name, opening_date, running_time 총 4개의 필드를 fields 옵션을 사용해 직렬화 시키는 방법
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'name', 'opening_date', 'running_time']

# id, name, opening_date, running_time 총 4개의 필드를 exclude 옵션을 사용해 직렬화 시키는 방법
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        exclude = ['overview']

```

`exclude`는 조건부 필수 옵션으로, 위에서 설명한 `fields`를 사용하지 않으면 필수로 입력해야 합니다.

## `read_only_fields`

이전 레슨에서 모델 시리얼라이저는 `id` 필드와 같이 데이터베이스에서 기본으로 생성되는 필드에 `read_only` 옵션을 자동으로 추가해 준다고 했었죠? 하지만, 만약 그 외 필드(자동 생성되지 않는 필드)에 선택적으로 `read_only`를 추가하려면 `read_only_fields` 옵션을 사용하면 됩니다.

```python
# read_only_fields를 사용한다면 필드명 작성을 통해 read_only 옵션을 추가할 수 있음.
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'name', 'opening_date', 'running_time', 'overview']
        read_only_fields = ['name']

```

## `extra_kwargs`

다양한 필드에 여러 옵션을 추가해야 할 경우 `extra_kwargs`를 사용합니다. `extra_kwargs`를 사용하면 필드를 직접 정의하지 않아도 된다는 `ModelSerializer`의 장점을 극대화할 수 있습니다.

만약 영화 모델의 줄거리(`overview`)를 생성 시에만 사용하고 싶다면, 아래 코드와 같이 `extra_kwargs`를 사용하여 `write_only` 옵션을 추가할 수 있습니다.

```python
# extra_kwargs를 사용한다면 간단하게 특정한 필드에 옵션을 추가할 수 있음.
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'name', 'opening_date', 'running_time', 'overview']
        extra_kwargs = {
            'overview': {'write_only': True},
        }

```

  

참고로 꼭 `read_only_fields`나 `extra_kwargs` 같은 옵션을 사용하지 않고 필드를 직접 정의해도 됩니다.

```python
class MovieSerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only=True)
    overview = serializers.CharField(write_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'name', 'opening_date', 'running_time', 'overview']

```
