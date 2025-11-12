import java.util.Arrays;
import java.util.Scanner;
public class sorted{
    static int numlist = 0;
    public static void main(String[] args){
        int[] list = list_maker();
        list = sorter(list);
        System.out.println("this is your sorted list:");
        System.out.println(Arrays.toString(list));
    }

    public static int[] list_maker(){
        System.out.println("how many integers will be in the list?");
        Scanner input = new Scanner(System.in);
        numlist = input.nextInt();
        int[] list = new int[numlist];
        for (int i = 0; i<numlist; i++){
            System.out.println("please enter an integer");
            list[i] = input.nextInt();
        }
        input.close();
        return list;
    }

    public static int[] sorter(int[] list){
        for ( int i = 0; i<numlist; i++) {
            for (int d = i; d<numlist; d++){
                if (list[d]<list[i]) {
                    int smallestIndex = d;
                    int temp = list[i];
                    list[i] = list[smallestIndex];
                    list[smallestIndex] = temp;  
                }
            }
            
        }
        return list;
    }
}