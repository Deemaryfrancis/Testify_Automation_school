package Tasks.Task15;

public class ClassB extends ClassA{

    public static void main(String[] args) {
        ClassA classA = new ClassA();
        classA.qaTester();
        classA.productManager();
        classA.uxDesigner();

        ClassB classB = new ClassB();
        classB.qaIntern();
        classB.designIntern();

    }

    public void qaIntern() {
        System.out.println("QA Intern");
    }

    public void designIntern() {
        System.out.println("Design Intern");
    }
}
