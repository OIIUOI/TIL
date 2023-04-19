## Raise

### **그냥  raise**

```
a = int(input("1~5 까지 숫자 입력 : "))

# 범위를 벗어나면 error 발생!
if a < 1 or a > 5:
    raise

# 범위 안에 있으면 정상 출력
print(f"입력한 a : {a} 입니다.")
```

이렇게 1~~5까지 숫자를 받아야하는 프로그램을 만들었다고 생각한다면  
1~~5 사이의 숫자가 아니라 다른 숫자를 넣게 되면 raise 를 통해서 에러를 발생하도록 할 수 있습니다.

![](https://blog.kakaocdn.net/dn/bz2fCz/btq8lEJeMC2/2oC7bbPSfOEKaERmOzk9Uk/img.png)

![](https://blog.kakaocdn.net/dn/pclqN/btq8lDQ7HPL/SjLlh1fHadHwIH2OqjKUVk/img.png)

이런식으로 raise 를 이용해서 일부러 에러를 발생시킬 수 있습니다.

### **raise + 예외처리 이름**

raise 뒤에 이미 파이썬에서 에러로 사용하고 있는 키워드들을 넣을 수 있습니다.  
ValueError, SyntaxError, NameError 등등의 에러 종류가 있으며 이중 알맞는 키워드를 입력할 수 있습니다.   
에러 종류에 대한 포스팅은 다음 포스팅에서 다루도록 하겠습니다.

```
a = int(input("1~5 까지 숫자 입력 : "))

# 범위를 벗어나면 error 발생!
if a < 1 or a > 5:
    raise ValueError

# 범위 안에 있으면 정상 출력
print(f"입력한 a : {a} 입니다.")
```

raise ValueError 이런식으로 raise 뒤에 에러 종류를 입력하면 됩니다.

![](https://blog.kakaocdn.net/dn/buEInR/btq8ojX8A1p/HGaiXGlvY6zaFwXL0lofVk/img.png)

결과를 보면 이렇게 해당 에러 종류가 잘 나오는 것을 볼 수 있습니다

### **raise + 메시지**

1-2에서 처럼 이미 정해진 에러 코드를 출력하도록 할수도있지만, 우리가 원하는 메시지를 출력하도록 할 수 있습니다.

**raise Exception("메시지")**

이런식으로 메시지를 작성하면 됩니다. 바로 예제를 볼까요?

```
a = int(input("1~5 까지 숫자 입력 : "))

# 범위를 벗어나면 error 발생!
if a < 1 or a > 5:
    raise Exception("에러에러에러!!")

# 범위 안에 있으면 정상 출력
print(f"입력한 a : {a} 입니다.")
```

![](https://blog.kakaocdn.net/dn/bagJEB/btq8mVwFZWL/crnN2HAuddTgg8m9JuMGTK/img.png)

결과를 보면 이렇게 해당 에러 종류가 잘 나오는 것을 볼 수 있습니다

## **파이썬 예외처리 try + raise + except**

---

우리가 raise를 통해서 에러를 발생시킬수 있는데, 이 에러도 우리가 이전 시간에 배웠던 예외처리 try + except  를 통해서 에러를 처리할 수 있습니다.

```
try:
    a = int(input("1~5 까지 숫자 입력 : "))

    # 범위를 벗어나면 error 발생!
    if a < 1 or a > 5:
        raise

    # 범위 안에 있으면 정상 출력
    print(f"입력한 a : {a} 입니다.")
except:
    print("1~5 사이 입력하라고 했잖아요.")
```

![](https://blog.kakaocdn.net/dn/cC4Nrb/btq8lw5kYnQ/mRP6dLQLZ9ze8ixFvEvzz0/img.png)

동일한 코드를 **try + except 구문으로 감싸게 하고 try 안에서 raise 를 통해서 에러를 발생**시킬 수 있습니다.  
하지만 try + except 로 예외처리를 하고 있으니, 에러로 인해서 프로그램이 중간에 비정상 종료되는 것이 아니라,  
except 구문으로 가게되어서 예외처리 되고 있음을 볼 수 있습니다.
