public class Cat {
    private String name;
    private String gender;
    private int age;
    private boolean adoptable;

    public void meow(){
        System.out.println("meow");
    }

    public void catDetails(){
        System.out.println("these are the details of the cat. Name "+this.name+", Age "+this.age+", Gender "+this.gender+", Adoptable "+this.adoptable);
    }

    public String getName(){
        return  this.name;
    }

    public String getGender(){
        return  this.gender;
    }

    public int getAge(){
        return  this.age;
    }

    public boolean getAdoptable(){
        return  this.adoptable;
    }

    public void setName(String name){
        this.name=name;
    }

    public void setGender(String gender){
        this.gender=gender;
    }

    public void setAge(int age){
        this.age=age;
    }

    public void setAdoptable(boolean adoptable){
        this.adoptable=adoptable;
    }

    public Cat(){
        this.name="cat";
        this.age=1;
        this.adoptable=true;
        this.gender="M";
    }
}
