package Tasks.Task16B;

public class Creche extends School{
    public static void main(String[] args) {
        School apex = new School() {
            @Override
            public void kitchen() {
                System.out.println("lunch room");
            }

            @Override
            public void playGround() {
                System.out.println("games room");
            }
        };
        apex.kitchen();
        apex.playGround();
    }

    @Override
    public void kitchen(){
        System.out.println(" this is the kitchen");
    }
    @Override
    public void playGround(){
        System.out.println("this is the playground");
    }
}
