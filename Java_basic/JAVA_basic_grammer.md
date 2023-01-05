# JAVA

computer

virtual Machine

java source code

code -> compile -> .class file (this is java app) -> run   

---

## Grammer

| Grammer             | mean                                  |
|:-------------------:|:-------------------------------------:|
| `\n`                | enter in print                        |
| `\" \"`             | escape                                |
| `"string".length()` | string's length                       |
| &&                  | and                                   |
|                     |                                       |
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

```java
import java.util.Scanner;

public class Scanner2Demo {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while(sc.hasNextInt()) {
            System.out.println(sc.nextInt()*1000); 
        }
        sc.close();
    }
}
```

- `.hasNextInt()`
  
  - is int? or not? => return true or false

- file input

```java
import java.util.Scanner;
import java.io.*;

public class Scanner3Demo {

    public static void main(String[] args) {
        try {
            File file = new File("out.txt");
            Scanner sc = new Scanner(file);
            while(sc.hasNextInt()) {
                System.out.println(sc.nextInt()*1000); 
            }
            sc.close();
        } catch(FileNotFoundException e){
            e.printStackTrace();
        }

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
