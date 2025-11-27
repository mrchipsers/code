import java.util.Arrays;
public class BubbleSort{
    public static void main(String[] args){
        int[] list = {2,4,5,6,4,5,3};
        boolean repeat = true;
        while (repeat){
            System.out.println(Arrays.toString(list));
            repeat = bubbleSwitch(list);
        }
        System.out.println(Arrays.toString(list));
    }

    public static boolean bubbleSwitch(int[] list){
        boolean sort = false;
        for (int i = 0; i<(list.length-1); i++)
            if (list[i]>list[i+1]){
                sort = true;
                int temp = list[i];
                list[i] = list[i+1];
                list[i+1] = temp;
            }
        return sort;
    }
}