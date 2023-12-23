package Tasks.Task14;

public class ClassB {
    public static void main(String[] args) {
        ClassA squareShape = new ClassA();
        squareShape.setShapeLength(20);
        int squareShapeLength = squareShape.getShapeLength();
        System.out.println("length of the square is: " + squareShapeLength + "cm");

        squareShape.setShapeBreadth(20);
        int squareShapeBreadth = squareShape.getShapeBreadth();
        System.out.println("breadth of the square is: " + squareShapeBreadth + "cm");

        int squareShapeArea = squareShapeLength * squareShapeBreadth;
        System.out.println("The area of a sqaure of length " +squareShapeLength +"cm and breadth " + squareShapeBreadth +"cm" + " is: " + squareShapeArea + "cm2");

    }
}
