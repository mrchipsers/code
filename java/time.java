public class time{
    public static void main(String[] args){
        double f= 32.56;
        double x= f%(f/f);
        f-=x;
        x=(x*60)/100;
        f+=x;
        System.out.println(f);
    }
}