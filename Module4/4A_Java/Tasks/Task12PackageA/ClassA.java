package Tasks.Task12PackageA;

import Tasks.Task12PackageB.ClassB;

public class ClassA {
    public static void main(String[] args) {
        ClassA task12 = new ClassA();
        task12.classA();

    }

    public void classA() {
        System.out.println("Class A");
        ClassB task = new ClassB();

    }
}
