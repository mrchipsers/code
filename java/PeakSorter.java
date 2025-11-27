import java.util.Arrays;

public class PeakSorter {
    public static void main(String[] args) {
        int[] arr = { 1, 2, 3, 4, 5, 6, 7 };
        int peakElement= sorter(arr, 3);
        System.out.println(Arrays.toString(arr));
        System.out.println(peakElement);
    }
    public static int sorter(int[] list, int peak){
        for (int i = 0; i<peak; i++){
            for (int j = i; j<list.length; j++){
                if (list[j]<list[i]) {
                    int temp = list[i];
                    list[i] = list[j];
                    list[j] = temp;  
                }
            }
        }

        for (int i = peak; i<list.length; i++){
            for (int j = i; j<list.length; j++){
                if (list[j]>list[i]) {
                    int temp = list[i];
                    list[i] = list[j];
                    list[j] = temp;  
                }
            }
        }
        int peakElement = list[peak];
        return peakElement;
    }
}
