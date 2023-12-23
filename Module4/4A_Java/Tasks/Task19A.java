package Tasks;

public class Task19A {

    final int ballSize;

    public Task19A(){
        ballSize = 7;
    }

   final public  void play(){
       String ballColour = "blue";
       String ballTexture = "hard";
       System.out.println("I want to play with the "+ballTexture + " " +ballColour +" ball that weighs " + ballSize + " kg");
    }
}
