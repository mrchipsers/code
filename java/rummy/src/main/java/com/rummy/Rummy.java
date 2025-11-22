package com.rummy;
import java.util.Arrays;
import java.util.Random;
public class Rummy{
    public static void main(String[] args) {
        String[] deck = buildDeck();
        System.out.println(Arrays.toString(deck));
        shuffleDeck(deck);
        
        String[] hand = dealHand(deck);
        sortHand(hand);
        
        print(hand);
        //System.out.println((int)"123".charAt(0));
        //System.out.println((int)"123".charAt(1));
        //System.out.println((int)"123".charAt(2));
        
    }

    public static void print(String[] input){
        for (int i = 0; i<input.length; i++){
            System.out.print(input[i]);
            if (i!=input.length-1){
                System.out.print(",");
            }else{
                System.out.println();
            }
        }
    }

    public static String[] buildDeck(){
        String[] deck = new String[40];
        
        for (int i = 0; i<4; i++){
            for (int j = 1; j<11; j++){
                if (i==0){
                    deck[j-1]=j+"S";
                }else if (i==1){
                    deck[9+j]=j+"D";
                }else if (i==2){
                    deck[19+j]=j+"H";
                }else{
                    deck[29+j]=j+"C";
                }
            }
        }
        return deck;
    }

    public static void shuffleDeck(String[] cardArray){
        Random random = new Random();
        for (int i = 0; i<40; i++){
            int index = random.nextInt(40);
            String temp = cardArray[i];
            cardArray[i] = cardArray[index];
            cardArray[index] = temp;
        }
    }

    public static String dealCard(String[] cardArray){
        for (int i = 0; i<cardArray.length; i++){
            if (cardArray[i]!="0"){
                String card = cardArray[i];
                cardArray[i]="0";
                return card;
            }
        }
        return "nothing left";
    }

    public static String[] dealHand(String[] cardArray){
        String[] hand = new String[10];
        for (int i = 0; i<10; i++){
            hand[i]=dealCard(cardArray);
        }
        return hand;
    }

    public static void redraw(String[] hand, String[] deck, int position){
        hand[position]=dealCard(deck);
    }

    public static char cardSuit(String card){
        if (card.charAt(1)=='0'){
            return card.charAt(2);
        }else{
            return card.charAt(1);
        }
    }

    public static int cardNum(String card){
        if (card.charAt(0)=='1' && card.charAt(1)=='0') {
            return 10;
        } else{
            return (int) card.charAt(0)-'0';
        }
    }

    public static void sortHand(String[] hand){
        boolean repeat=true;
        while (repeat){
            repeat=false;
            for (int i = 0; i<(hand.length-1); i++){
                if (cardNum(hand[i])>cardNum(hand[i+1])){
                    repeat = true;
                    String temp = hand[i];
                    hand[i] = hand[i+1];
                    hand[i+1] = temp;
                } else if (cardNum(hand[i])==cardNum(hand[i+1]) && cardSuit(hand[i])>cardSuit(hand[i+1])){
                    repeat = true;
                    String temp = hand[i];
                    hand[i] = hand[i+1];
                    hand[i+1] = temp;
                }
            }
        }

    }
}