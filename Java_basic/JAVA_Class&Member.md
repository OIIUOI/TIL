# JAVA

---

## Class

- method define
  
  ```java
  public class CalculatorDemo2 {
      // method define
      public static void sum(int left, int right) {
          System.out.println(left + right);
      }
  
      // main 
      public static void main(String[] args) {
          sum(10, 20);
          sum(20, 40);
      }
  
  }
  ```

- class define & use class in main
  
  ```java
  class Calculator{
      int left, right;
  
      public void setOprands(int left, int right){
          this.left = left;
          this.right = right;
      }
  
      public void sum(){
          System.out.println(this.left+this.right);
      }
  
      public void avg(){
          System.out.println((this.left+this.right)/2);
      }
  }
  
  public class CalculatorDemo4 {
  
      public static void main(String[] args) {
  
          Calculator c1 = new Calculator();
          c1.setOprands(10, 20);
          c1.sum();       
          c1.avg();       
  
          Calculator c2 = new Calculator();
          c2.setOprands(20, 40);
          c2.sum();       
          c2.avg();
      }
  }
  ```
  
  - if you want to use class, we can't use class direct,
    
    `new` is method make class to instant
    
    and variable's type is instant's class, cause we make datatype by class
  
  - `this.left = left;``this.right = right`
    
    you can write like this
    
    ```java
    class Calculator {
    
      public void sum(int left, int right) {
        System.out.println(left + right);
      }
    
      public void avg(int left, int right) {
        System.out.println((left + right) / 2);
      }
    }
    
    public class prac {
    
      public static void main(String[] args) {
    
        Calculator c1 = new Calculator();
        c1.sum(10, 20);
        c1.avg(10, 20);
    
        Calculator c2 = new Calculator();
        c2.sum(10, 20);
        c2.avg(10, 20);
      }
    }
    ```
    
    I don't know why do like this setting the value meaning
    
    but I guess that is instant
    
    and prevent overlapping code, maybe?
    
    **NOPE, instant method**
    
    **OOP's mean**
    
    > programing pradime
    > 
    > Create logic by object maden state(variable) and behave(method)

---

## Class member and Instant member

Member is variable included class and method

Instant member's meaning is having different values for each instant

Class member's meaning is having same value every instant

```java
class Calculator{
    static double PI = 3.14;
    int left, right;

    public void setOprands(int left, int right){
        this.left = left;
        this.right = right;
    }

    public void sum(){
        System.out.println(this.left+this.right);
    }

    public void avg(){
        System.out.println((this.left+this.right)/2);
    }
}
```

static is fixed (we can use `final`)

`PI` is class member, every instant have same value

`left`, `right` is instant member can be change

If you have class member, you can access to value by class, not instant

```java
Calculator c2 = new Calculator();
System.out.println(c2.PI);

System.out.println(Calculator.PI);
```

and it can do like this

```java
class Calculator2 {
    static double PI = 3.14;
    // 클래스 변수인 base가 추가되었다.
    static int base = 0;
    int left, right;

    public void setOprands(int left, int right) {
        this.left = left;
        this.right = right;
    }

    public void sum() {
        // 더하기에 base의 값을 포함시킨다.
        System.out.println(this.left + this.right + base);
    }

    public void avg() {
        // 평균치에 base의 값을 포함시킨다.
        System.out.println((this.left + this.right + base) / 2);
    }
}

public class CalculatorDemo2 {

    public static void main(String[] args) {

        Calculator2 c1 = new Calculator2();
        c1.setOprands(10, 20);
        // 30 출력
        c1.sum();

        Calculator2 c2 = new Calculator2();
        c2.setOprands(20, 40);
        // 60 출력
        c2.sum();

        // 클래스 변수 base의 값을 10으로 지정했다.
        Calculator2.base = 10;

        // 40 출력
        c1.sum();

        // 70 출력
        c2.sum();
    }
}
```

- Reason of Class Member
  
  - case of fixed value regardless of instant
  
  - case of accessing value by class directly
  
  - case of sharing value's change every instant

---

## Class method

if you don't need to have instant member, and you want to use method

don't make instant, just use method with accessing class directly

you can see `static`, it's mean of **Class method**

```java
class Calculator3{

    public static void sum(int left, int right){
        System.out.println(left+right);
    }

    public static void avg(int left, int right){
        System.out.println((left+right)/2);
    }
}

public class CalculatorDemo3 {

    public static void main(String[] args) {
        Calculator3.sum(10, 20);
        Calculator3.avg(10, 20);

        Calculator3.sum(20, 40);
        Calculator3.avg(20, 40);
    }
}
```

---

## Relationship of Instant member & Class member

- Instant member = Non-Static Field

- Class member = Satic Field

```java
class C1{
    static int static_variable = 1;
    int instance_variable = 2;
    static void static_static(){
        System.out.println(static_variable);
    }
    static void static_instance(){
        // 클래스 메소드에서는 인스턴스 변수에 접근 할 수 없다. 
        //System.out.println(instance_variable);
    }
    void instance_static(){
        // 인스턴스 메소드에서는 클래스 변수에 접근 할 수 있다.
        System.out.println(static_variable);
    }
    void instance_instance(){        
        System.out.println(instance_variable);
    }
}
public class ClassMemberDemo {  
    public static void main(String[] args) {
        C1 c = new C1();
        // 인스턴스를 이용해서 정적 메소드에 접근 -> 성공
        // 인스턴스 메소드가 정적 변수에 접근 -> 성공
        c.static_static();
        // 인스턴스를 이용해서 정적 메소드에 접근 -> 성공
        // 정적 메소드가 인스턴스 변수에 접근 -> 실패
        c.static_instance();
        // 인스턴스를 이용해서 인스턴스 메소드에 접근 -> 성공
        // 인스턴스 메소드가 클래스 변수에 접근 -> 성공
        c.instance_static();
        // 인스턴스를 이용해서 인스턴스 메소드에 접근 -> 성공 
        // 인스턴스 메소드가 인스턴스 변수에 접근 -> 성공
        c.instance_instance();
        // 클래스를 이용해서 클래스 메소드에 접근 -> 성공
        // 클래스 메소드가 클래스 변수에 접근 -> 성공
        C1.static_static();
        // 클래스를 이용해서 클래스 메소드에 접근 -> 성공
        // 클래스 메소드가 인스턴스 변수에 접근 -> 실패
        C1.static_instance();
        // 클래스를 이용해서 인스턴스 메소드에 접근 -> 실패
        //C1.instance_static();
        // 클래스를 이용해서 인스턴스 메소드에 접근 -> 실패
        //C1.instance_instance();
    }
}
```
