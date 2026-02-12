
public class Main {
    public static void main(String[] args) {
        Cat mittens = new Cat();
        mittens.adoptable=true;
        mittens.name="Mittens";
        mittens.age=12;
        mittens.gender="M";

        mittens.meow();
        mittens.catDetails();
    }    
}
