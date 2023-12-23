package Tasks;

import java.util.Scanner;

public class Task18 {
    public static void main(String[] args) {
        try {
            Scanner userInput = new Scanner((System.in));
            System.out.println("How old are you?");
            int dob = userInput.nextInt();
        } catch (Exception ageException){
            System.out.println("Input field only accepts numbers");
            System.out.println(ageException);
        }
    }

}
