package challenge;

public class Challenge8 {
    public static void main(String[] args) {
        int[] inputArray = randomArray(1000000, 1, 9); // Generate 1 million random integers between 1 and 9
        int[] sortedArray = countingSort(inputArray, 1, 9);

        // Print the sorted array (for demonstration purposes, not suitable for large arrays)
        for (int num : sortedArray) {
            System.out.print(num + " ");
        }
    }
    public static int[] countingSort(int[] arr, int min, int max) {
        int[] countArray = new int[max - min + 1];

        // Count the occurrences of each element
        for (int num : arr) {
            countArray[num - min]++;
        }

        int k = 0;

        // Reconstruct the sorted array from the countArray
        for (int i = min; i <= max; i++) {
            while (countArray[i - min] > 0) {
                arr[k++] = i;
                countArray[i - min]--;
            }
        }

        return arr;
    }
    public static int[] randomArray(int length, int min, int max) {
        int[] arr = new int[length];
        for (int i = 0; i < length; i++) {
            arr[i] = (int) (Math.random() * (max - min + 1) + min);
        }
        return arr;
    }
}