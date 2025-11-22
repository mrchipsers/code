import java.util.Arrays;
import java.util.Scanner;
public class sorted{
    public static void main(String[] args){
        //int[] list = list_maker();
        int[] list = {2,4,3,5,6,4,7,4,5};
        list = sorter(list);
        System.out.println("this is your sorted list:");
        System.out.println(Arrays.toString(list));
    }

    public static int[] list_maker(){
        System.out.println("how many integers will be in the list?");
        Scanner input = new Scanner(System.in);
        int numlist = input.nextInt();
        int[] list = new int[numlist];
        for (int i = 0; i<numlist; i++){
            System.out.println("please enter an integer");
            list[i] = input.nextInt();
        }
        input.close();
        return list;
    }

    public static int[] sorter(int[] list){
        int n = list.length;
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                if (list[j] < list[i]) {
                    int temp = list[i];
                    list[i] = list[j];
                    list[j] = temp;
                }
            }
        }
        return list;
    }
}