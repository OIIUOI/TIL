# JAVA

---

## Method

```java
public class MethodDemo1 {
// Method define
    public static void numbering() {
        int i = 0;
        while (i < 10) {
            System.out.println(i);
            i++;
        }
    }

// Method call
    public static void main(String[] args) {
        numbering();
    }
}
```

- Parameter & Argument

```java
public class MethodDemo4 {
    public static void numbering(int limit) { // <- parameter
        int i = 0;
        while (i < limit) {
            System.out.println(i);
            i++;
        }
    }

    public static void main(String[] args) { // <- argument
        numbering(5);
    }
}
```

- More than two Parameter

```java
public class MethodDemo5 {

    public static void numbering(int init, int limit) {
        int i = init;
        while (i < limit) {
            System.out.println(i);
            i++;
        }
    }

    public static void main(String[] args) {
        numbering(1, 5);
    }

}
```

- return
  
  - void => no return

```java
public class MethodDemo6 {
    public static String numbering(int init, int limit) {
        int i = init;
        String output = "";
        while (i < limit) {
            output += i;
            i++;
        }.
        return output;
    }

    public static void main(String[] args) {
        // 메소드 numbering이 리턴한 값이 변수 result에 담긴다.
        String result = numbering(1, 5);
        // 변수 result의 값을 화면에 출력한다.
        System.out.println(result);
    }
}
```

- More than two Return

```java
public class ReturnDemo4 {

    public static String[] getMembers() {
        String[] members = { "최진혁", "최유빈", "한이람" };
        return members;
    }

    public static void main(String[] args) {
        String[] members = getMembers();
    }

}
```

---
