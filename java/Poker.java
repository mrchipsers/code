import java.util.Arrays;
import java.util.Random;
public class Poker {
    public static void main(String[] args){
        String[] deck = buildDeck();
        shuffleDeck(deck);
        System.out.println(Arrays.toString(deck));
    }

    public static String[] buildDeck(){
        String[] deck = new String[52];
        String[] suit = {"S", "H", "C", "D"};
        int index = 0;
        for (int i = 0; i<suit.length; i++){
            for (int j = 1; j<14; j++){
                if (j == 11){
                    deck[index]="J"+suit[i];
                } else if (j==12){
                    deck[index]="Q"+suit[i];
                }else if (j==13){
                    deck[index]="K"+suit[i];
                }else{
                    deck[index]=j+suit[i];
                }
                index++;
            }
        }
        return deck;
    }

    public static void shuffleDeck(String[] cardArray){
        Random random = new Random();
        for (int i = 0; i<52; i++){
            int index = random.nextInt(52);
            String temp = cardArray[i];
            cardArray[i] = cardArray[index];
            cardArray[index] = temp;
        }
    }

    public static String[] deal(String[] deck, int amount){
        String[] hand = new String[amount];
        int start = 0;
        for (int j = 0; j<52;j++){
                if (!deck[j].equals("0")){
                    start=j;
                }
            }
        for (int i = 0;i<amount;i++){
                hand[i]=deck[start+i];
                deck[start+i]="0";
            }
        return hand;
    }

    
}
