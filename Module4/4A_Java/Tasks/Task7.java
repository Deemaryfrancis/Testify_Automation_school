package Tasks;

public class Task7 {
    public static void main(String[] args) {

        // 2-dimensional array with 4 rows and 3 columns. 
        // Fill only the first column with any fruits of ur choice

        String[][] fruitShelf =  new String[4][3];
        fruitShelf [0][0] = "Paw-Paw";
        fruitShelf [1][0] = "Orange";
        fruitShelf [2][0] = "Banana";
        fruitShelf [3][0] = "Apple";

        System.out.println(java.util.Arrays.deepToString(fruitShelf));
    }
}