package challenge;

import java.util.Arrays;

public class Challenge6 {
    public static void main(String[] args) {
        String sentence = "Despite commuting at the peak hour, she was able to keep to time";
        String[] words = sentence.split(" ");

        for (int i = 0; i < words.length; i++) {
            for (int j = i + 1; j < words.length; j++) {
                if (areAnagrams(words[i], words[j])) {
                    System.out.println(words[i] + " and " + words[j] + " are anagrams.");
                }
            }
        }
    }

    public static boolean areAnagrams(String str1, String str2) {
        // Remove spaces and convert to lowercase
        str1 = str1.replaceAll("\\s+", "").toLowerCase();
        str2 = str2.replaceAll("\\s+", "").toLowerCase();

        // Check if the lengths are different
        if (str1.length() != str2.length()) {
            return false;
        }

        // Convert the strings to character arrays and sort them
        char[] charArray1 = str1.toCharArray();
        char[] charArray2 = str2.toCharArray();
        Arrays.sort(charArray1);
        Arrays.sort(charArray2);

        // Compare the sorted character arrays
        return Arrays.equals(charArray1, charArray2);
    }
}