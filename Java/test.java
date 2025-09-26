public class test{
    static int timer_default = 50;
    static int timer = timer_default;
    public static void main(String[] args){
        System.out.println("this is a test for timers");
        text("here I am modifying the wait time"); timer = 700;
        text("now there is no wait time");
    }
    public static void text(String text){
        System.out.println("start the clock for "+timer+" milliseconds");
        try {
            Thread.sleep(timer);
        } catch (InterruptedException e) {
            System.out.println("thread interrupt");
        }
        System.out.println("time is up");
        timer = timer_default;
    }
}