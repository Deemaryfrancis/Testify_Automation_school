package challenge;

public class Challenge7 {
    public static void main(String[] args) {
        String word = "TestifyAutomation";
        String reverse = "";

        // function to reverse sentence
        for (int i = 0; i < word.length(); i++) {
            reverse = word.charAt(i) + reverse;
        }
        System.out.println(reverse);
    }
}
