public class Cat {
    public String name;
    public String gender;
    public int age;
    public boolean adoptable;

    public void meow(){
        System.out.println("meow");
    }

    public void catDetails(){
        System.out.println("these are the details of the cat. Name "+this.name+", Age "+this.age+", Gender "+this.gender+", Adoptable "+this.adoptable);
    }
}
