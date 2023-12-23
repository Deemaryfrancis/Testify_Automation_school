package Tasks;

public class Task4 {
    public static void main(String[] args) {
        // Find the area of a circle with radius on 12.7m. 
        //Print out your result with the unit of measurement which is meters

        // area= pie π × r2
        // pie (π) = 3.14
        // radius (r) = 12.7

        float radius = 12.7f;

        double pie = 3.14;

        double areaOfCircle = pie * (radius*radius);

        String unit = "metres";

        System.out.println(areaOfCircle + unit);
    }
}
