package challenge;

import java.util.*;

public class Challenge5 {
    public static void main(String[] args) {
        String[] words = {"akak", "akka", "bbaa", "baba", "baab"};
        Map<String, List<String>> anagramBucket = createAnagramBucket(words);

        // Print the anagram bucket
        for (List<String> bucket : anagramBucket.values()) {
            System.out.println(bucket);
        }
    }

    public static Map<String, List<String>> createAnagramBucket(String[] words) {
        Map<String, List<String>> anagramBucket = new HashMap<>();

        for (String word : words) {
            // Sort the characters in the word
            char[] charArray = word.toCharArray();
            Arrays.sort(charArray);
            String sortedWord = new String(charArray);

            // Check if a bucket for the sorted word exists in the map
            if (!anagramBucket.containsKey(sortedWord)) {
                anagramBucket.put(sortedWord, new ArrayList<>());
            }

            // Add the original word to the corresponding bucket
            anagramBucket.get(sortedWord).add(word);
        }

        return anagramBucket;
    }
}

