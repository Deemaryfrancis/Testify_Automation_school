package Tasks;

import java.util.Scanner;

public class Task10 {
    public static void main(String[] args) {
        // Create a method that verify that visitors on the slack channel are coming for testify Trainings.
        // If they write" Testify" then print out a  welcome message
        // if not, the user should be shown rejection message.
        // after creating this method,then invoke the created method in your main method

        Task10 methodVariable = new Task10();
        methodVariable.verifyMe();
    }

    public void verifyMe() {
        Scanner scanner = new Scanner(System.in);
        String Input = "";
        System.out.println("Please enter your passcode:");
        Input = scanner.nextLine();

        if (Input.equalsIgnoreCase("Testify")) {
            System.out.println("Welcome to the Testify weekly training!");

        } else {
            System.out.println("Sorry, you cannot join this meeting!");
        }
    }
}
