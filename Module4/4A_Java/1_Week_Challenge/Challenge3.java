package challenge;

public class Challenge3 {
    public static void main(String[] args) {
        int[] arr = {-40, 4, 2, 31, 4, 9};
        int[] result = maxProduct(arr);

        if (result != null) {
            System.out.println("Two numbers with maximum product: " + result[0] + " and " + result[1]);
        } else {
            System.out.println("Not enough elements to form a pair.");
        }
    }

    public static int[] maxProduct(int[] arr) {
        if (arr.length < 2) {
            return null;  // Not enough elements to form a pair
        }

        int max1 = Integer.MIN_VALUE, max2 = Integer.MIN_VALUE;

        for (int num : arr) {
            if (num > max1) {
                max2 = max1;
                max1 = num;
            } else if (num > max2) {
                max2 = num;
            }
        }

        return new int[]{max1, max2};
    }
}


