package Tasks.Task19C;

public class ClassB extends ClassA{

    String name = "Anderson";

    public static void main(String[] args) {
        ClassB object = new ClassB();
        object.newName();
    }

    public void newName(){
        System.out.println("ClassA value is: "+super.name +" \nClassB value is: "+ name);
    }
}
