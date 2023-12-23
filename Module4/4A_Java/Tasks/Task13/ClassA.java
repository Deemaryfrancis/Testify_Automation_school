package Tasks.Task13;

public class ClassA {
    String name;
    int price;
    boolean isAvailable;

    public ClassA(String Cname) {
        name = Cname;
    }
    public ClassA(String Cname, int Cprice) {
        price = Cprice;
    }
    public ClassA(String Cname, int Cprice, boolean CisAvailable) {
        isAvailable = CisAvailable;
    }
    public void printCar(){
        System.out.println();
    }
}
