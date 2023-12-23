package challenge;

public class Challenge2 {
    public static void main(String[] args) {
        String sentence = "I am getting better at software testing";
        String reverse = "";

        // function to reverse sentence
        for (int i = 0; i < sentence.length(); i++) {
            reverse = sentence.charAt(i) + reverse;
        }
        System.out.println(reverse);
    }
}
