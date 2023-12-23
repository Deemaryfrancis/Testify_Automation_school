package Tasks;

public class Task3 {
    public static void main(String[] args) {
        // Print out age in a string using different methods of concatenation

        int age = 30;
        String adjective = "My age is ";

        String conjuction = adjective + age;

        System.out.println(conjuction);
        
        System.out.println(adjective.concat(age+" "));
    }
}
