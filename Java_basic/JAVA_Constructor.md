# JAVA

---

We have to set a parameter of class for using class's method use class member

```java
class Calculator2 {
    int left, right;

    public void setOprands(int left, int right) {
        this.left = left;
        this.right = right;
    }

    public void sum() {
        System.out.println(this.left + this.right + base);
    }
}

public class CalculatorDemo2 {

    public static void main(String[] args) {

        Calculator2 c1 = new Calculator2();
        c1.setOprands(10, 20);
        c1.sum();
    }
}
```

We always use method set parameter, it's incovienient

So, if we call class with parameter, it is more simple

---

## Constructor

> method of setting a Class's parameter
> 
> it must have same name class's name

```java
class Calculator {
    int left, right;

    public Calculator(int left, int right) {
        this.left = left;
        this.right = right;
    }

    public void sum() {
        System.out.println(this.left + this.right);
    }

    public void avg() {
        System.out.println((this.left + this.right) / 2);
    }
}

public class CalculatorDemo1 {

    public static void main(String[] args) {

        Calculator c1 = new Calculator(10, 20);
        c1.sum();
        c1.avg();

        Calculator c2 = new Calculator(20, 40);
        c2.sum();
        c2.avg();
    }

}
```

in this code `new Calculator(10,20) ` is Constructor, not class

### Characteristics of the Constructor

- No return
  
  - Constructor is method to make instant, if it has return value it's not we need
  
  - Name of Constrcutor is same with class's name
