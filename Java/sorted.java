import java.util.Arrays;
import java.util.Scanner;
public class sorted{
    public static void main(String[] args){
        int[] list = list_maker();
        int numlist = list.length;
        list = sorter(list, numlist);
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

    public static int[] sorter(int[] list, int numlist){
        for ( int i = 0; i<numlist; i++) {
            int smallest_index = i;
            for (int d = i; d<numlist; d++){
                if (list[d]<list[smallest_index]) {
                    smallest_index = d;  
                }
            }
            int temp = list[i];
            list[i] = list[smallest_index];
            list[smallest_index] = temp;
        }
        return list;
    }
}