
public class Main {
    public static void main(String[] args) {
        Cat mittens = new Cat();
        mittens.catDetails(); 

        mittens.setAdoptable(true);
        mittens.setName("Mittens");
        mittens.setAge(12);
        mittens.setGender("M");

        mittens.meow();
        mittens.catDetails(); 
    }    
}
