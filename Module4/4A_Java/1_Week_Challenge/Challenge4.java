package challenge;

public class Challenge4 {
    public static void main(String[] args) {
        System.out.println("Prime numbers:");

        for (int num = 2; num <= 100; num++) {
            if (isPrime(num)) {
                System.out.print(num + " ");
            }
        }
    }

    public static boolean isPrime(int number) {

        if (number <= 3) {
            return true; // 2 and 3 are prime numbers
        }
        if (number % 2 == 0 || number % 3 == 0) {
            return false; // Numbers divisible by 2 or 3 are not prime
        }

        for (int i = 5; i * i <= number; i += 6) {
            if (number % i == 0 || number % (i + 2) == 0) {
                return false;
            }
        }

        return true;
    }
}
