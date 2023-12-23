package Tasks;

import java.util.Scanner;

public class Task8 {
    public static void main(String[] args) {

        // Build a Simple interest calculator.
        // Write a program to ask the user for the necessary field you need in calculating the simple interest
        // and then communicate the simple interest back to the user in a good sentence

        Scanner amountInput = new Scanner(System.in);

        System.out.println("Welcome, please enter your desired principal amount");
        double principal = amountInput.nextDouble();

        System.out.print("Enter your interest rate (%): ");
        double rate = amountInput.nextDouble();

        System.out.print("For how long do you want this to run (in years): ");
        double time = amountInput.nextDouble();

        double simpleInterest = (principal * rate * time) / 100;

        System.out.println("Your Simple Interest for a period of " + time+" years" +" at " + rate+"% " + " is " + simpleInterest);

        amountInput.close();

    }
}
