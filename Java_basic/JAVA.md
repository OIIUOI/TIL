# JAVA

computer

virtual Machine

java source code

code -> compile -> .class file (this is java app) -> run   

---

## Data type

| kind | Grammer                | mean             | range      | often |
|:----:|:----------------------:|:----------------:|:----------:|:-----:|
| int  | `int`x = 30            | integer          | int < long | *     |
| int  | `long` l = 30`L`       | big integer      | wide       | *     |
| int  | `short` s = 30         | small integer    | narrow     |       |
| int  | `byte` b = 30          | small then short | narrow     |       |
| dec  | `double` dd = 30.0     | decimal          | wide       | *     |
| dec  | `float` f = 30.0`f`    | decimal          | narrow     |       |
| str  | `char`  c = `'`a`'`    | one string       | narrow     |       |
| str  | `String` s = `"`str`"` | all string       | wide       | *     |

![](assets/2022-12-21-19-10-43-image.png)

<img src="assets/2022-12-21-19-24-08-image.png" title="" alt="" width="398">

- Just `int` , `double`

### Casting

> data type change

```java
int e = (int) 1.1;
System.out.println(e);
// 1

double b = (double) 1;
System.out.println(b);
// 1.0


String text = "1.56"
double num = Double.parseDouble(text)
System.out.println(num)
```

- `int range` is smaller than `long range`
  
  - if you want to change type `long` to  `int`
    
    ```java
    int i = (int) 30L;
    ```
  
  - but change type `int` to `long`
    
    ```java
    long l = 30;
    ```
  
  - you don't have need to change, because `long range` is bigger than `int range`
    
    this principal is same in double and float
    
    ```java
    double dd = 30.0;
    float ff = 30.0f;
    
    dd = ff; 
    ff = (float) dd;
    ```

- `string` to `int`
  
  ```java
  String str = "1000";
  
  int i = Integer.parseInt(str); // 1000
  long l = Long.parseLong(str); // 1000
  ```

- `int` to `string`
  
  ```java
  int i = 1000;
  String str = String.valueOf(i) // 1000
  
  System.out.println(i.getClass()); // class java.lang.String
  ```

### Array

- Array declaration -1

```java
public class DefineDemo {
    public static void main(String[] args) {
        String[] classGroup = { "최진혁", "최유빈", "한이람", "이고잉" };
    }
}
```

- Array declaration -2

```java
package org.opentutorials.javatutorials.array;
 
public class LengthDemo {
 
    public static void main(String[] args) {
        String[] classGroup = new String[4];
        classGroup[0] = "최진혁";
        System.out.println(classGroup.length);
        classGroup[1] = "최유빈";
        System.out.println(classGroup.length);
        classGroup[2] = "한이람";
        System.out.println(classGroup.length);
        classGroup[3] = "이고잉";
        System.out.println(classGroup.length);
 
    }
 
}
```

- for statement in array

```java
public class ArrayLoopDemo {
    public static void main(String[] args) {
        String[] members = { "최진혁", "최유빈", "한이람" };
        for (int i = 0; i < members.length; i++) {
            String member = members[i];
            System.out.println(member + "이 상담을 받았습니다");
        }
    }
}
```

```java
public class ForeachDemo {
    public static void main(String[] args) {

        String[] members = { "최진혁", "최유빈", "한이람" };
        for (String e : members) {
            System.out.println(e + "이 상담을 받았습니다");
        }
    }
}
```

---

## Grammer

| Grammer             | mean                                  |
|:-------------------:|:-------------------------------------:|
| `\n`                | enter in print                        |
| `\" \"`             | escape                                |
| `"string".length()` | string's length                       |
| &&                  | and                                   |
|                     | \|                                    |
| !                   | not (!true == false / !false == true) |

---

## Variable

java must called data type to variable 

```java
int a = 1;
double b = 1.1;
String c = "hello World";
```

---

## Const

if you don't want chage value

```java
final int x
```

---

## Input

```java
public class prac {
  public static void main(String[] args) {
    String id = args[0]
    String bright = args[1]
    System.out.println(id)
    System.out.println(bright)
  }
}
```

```java
public class prac {
  public static void main(String[] args) {
    String id = JOptionPane.showInputDialog("input here");
    System.out.println(id.getClass());
  }
}
```

---

## library

### Math

- max(a, b)
  
  - which one bigger a and b?

- min(a, b)
  
  - which one smaller a and b?

- abs(-20)
  
  - absolute value

### Random

```java
import java.util.Random;

public class Main {
    public static void main(String[] args) {
        Random random = new Random();
        random.nextInt(10);
        // ↑ 0 ~ 9
        random.nextInt(4) + 5;
        // ↑ 5 ~ 9
    }
}
```

### Scanner

```java
import java.util.Scanner

public class Main {
    public static void main(Sting[] args) {

        Scanner scanner = new Scanner(System.in);

        String str = scanner.next();
        int i = scanner.nextInt();
        long l = scanner.nextLong();
    }
}
```

---

## if Statement

```java
public class Main {
    public static void main(String[] args) {

        int i = 10;

        if (i < 5) {
            System.out.println("it's true")
        } else if (i < 3) {
            System.out.println("it's false")
        } else {
            System.out.println("???")
        }
    }
}
```

---

## Infix Operator

```java
package org.opentutorials.javatutorials.operator;

public class PrePostDemo {
    public static void main(String[] args) {
        int i = 3;
        i++;
        System.out.println(i); // 4 출력
        ++i;
        System.out.println(i); // 5 출력
        System.out.println(++i); // 6 출력
        System.out.println(i++); // 6 출력
        System.out.println(i); // 7 출력
    }
}
```

---

## The Ternary Operator ( Condition Operator )

```java
public class Main {
    public static void main(String[] args) {

        boolean bool = true; 
        String str;

        str = bool ? "abc" : "def";

        System.out.prinln(str); // abc
    }
}


// that mean


public class Main {
    public static void main(String[] args) {

        boolean bool = true; 
        String str;

        if (bool) {
            str = "abc";
        } else {
            str = "def";
        }

        System.out.prinln(str); // abc
    }
}
```

---

## Switch Statement

```java
String str = "asdf"


switch (str) {
    case "asdf":
        system.out.println("O");
        break;
    case "zxcv":
        system.out.println("X");
        break;
    default:
        system.out.println("?")
}
```

if your code don't have break code in case

all of code will execute

---

## For Statement

### For

```java
for (int i = 0; i< 10; i++) {
    System.out.println(i)
}
```

### While

```java
int i = 0
while (i < 10) {
    System.out.println(i);
    i ++;
}
```

### Do While

```java
int i = 0;
do {
    System.out.println(i);
    i++;
} while (i < 10);
```

### Break & Continue

- `break`
  
  - if you want to stop iteration, use this
    
    ```java
    for (int i = 0; i < 10; i++) {
      if (i == 4) {
        break;
      }
      System.out.println(i);
    }
    ```
  
  - 

- `continue`
  
  - if you want to skip iteration, use this
    
    ```java
    for (int i = 0; i < 10; i++) {
      if (i == 4) {
        continue;
      }
      System.out.println(i);
    }
    ```
