import java.util.ArrayList;
import java.util.Scanner;
public class sorter{
    public static void main(String[] args){
        int starting_index = 0;
        int smallest_index = 0;
        int d = 0;
        int c = 0;
        System.out.println("how many integers will be in the list?");
        Scanner input = new Scanner(System.in);
        int numlist = input.nextInt();
        ArrayList<Integer> list = new ArrayList<>(numlist);
        while (c<numlist){
            System.out.println("please enter and integer");
            list.add(input.nextInt());
            c++;
        }
        input.close();
        while (starting_index<list.size()) {
            while (d<list.size()){
                if (list.get(d)<list.get(smallest_index)) {
                    smallest_index = d;  
                }
                d++;
                }
            int temp = list.get(starting_index);
            list.set(starting_index, list.get(smallest_index));
            list.set(smallest_index, temp);
            starting_index++;
            d = starting_index;
            smallest_index = starting_index;
        }
        System.out.println("this is your sorted list:");
        System.out.println(list.toString());
    }
}