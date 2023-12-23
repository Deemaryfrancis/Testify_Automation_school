package Tasks;

public class Task5 {
    public static void main(String[] args) {
//        Write a code to: If the number is divisible by 3, print Fizz instead of the number.
//        If the number is divisible by 5, print Buzz instead of the number.
//        If the number is divisible by 3 and 5 both, print FizzBuzz instead of the number.

        int num = 123;

        if (num % 5 == 0 && num % 3 == 0) {
            System.out.println("FizzBuzz");
        } else if (num % 3 == 0) {
            System.out.println("Fizz");
        } else if (num % 5 == 0) {
            System.out.println("Buzz");
        } else {
            System.out.println(num);
        }
    }
}