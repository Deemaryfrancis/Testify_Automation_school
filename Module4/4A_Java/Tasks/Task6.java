package Tasks;

public class Task6 {
    public static void main(String[] args) {

        // Write a code to reverse the string DEMOCRACY and get the word COME out of it.

        String firstWord = "DEMOCRACY";
        String reversedWord = "";

        // function to reversefirstWord
        for (int i = 0; i < firstWord.length(); i++) {
            reversedWord = firstWord.charAt(i) + reversedWord;
        }

        // print the word COME at a particular index
        System.out.println(reversedWord.substring(4, 8));
    }
}
