package com.rummy;
import java.util.Arrays;
import java.util.Random;
import java.util.Scanner;
public class Rummy{
    static Scanner input = new Scanner(System.in);
    public static void main(String[] args) {
        String[] deck = buildDeck();
        System.out.println(Arrays.toString(deck));
        //shuffleDeck(deck);
        
        //String[] hand = dealHand(deck);
        //sortHand(hand);
        
        //print(hand);
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
        String[] suit = {"S", "H", "C", "D"};
        int index = 0;
        for (int i = 0; i<suit.length; i++){
            for (int j = 1; j<11; j++){
                deck[index]=j+suit[i];
                index++;
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

    public static String[] sortHand(String[] hand){
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
        return hand;
    }

    public static boolean isSet(String[] meld){
        for (int a = 0; a<meld.length; a++){
            for (int b = 0; b<meld.length; b++){
                if (a==b){
                    continue;
                }
                for (int c = 0; c<meld.length; c++){
                    if (c==b || c==a){
                        continue;
                    }
                    if (cardNum(meld[a])==cardNum(meld[b]) && cardNum(meld[b])==cardNum(meld[c])){
                        return true;
                    }
                }
            }
        }
        return false;
    }

    public static boolean isRun(String[] meld){
        for (int a = 0; a<meld.length; a++){
            for (int b = 0; b<meld.length; b++){
                for (int c = 0; c<meld.length; c++){
                    if (cardNum(meld[a])==cardNum(meld[b])-1 && cardNum(meld[b])==cardNum(meld[c])-1 && cardSuit(meld[a])==cardSuit(meld[b]) && cardSuit(meld[b])==cardSuit(meld[c]) && cardSuit(meld[c])==cardSuit(meld[a])){
                        return true;
                    }
                }
            }
        }
        return false;
    }

    public static int index(String[] cardArray, String card){
        for (int i = 0; i<cardArray.length; i++){
            if (cardArray[i].equals(card)){
                return i;
            }
        }
        return -1;
    }

    public static String[] chooseMeld(String[] hand){
        System.out.print("your hand: ");
        print(hand);
        System.out.println("How many card will you play? ");
        int cards = input.nextInt();
        String[] meld = new String[cards];
        for (int i = 0; i<cards;){
            System.out.println("play your card: ");
            meld[i]=input.nextLine();
            int index = index(hand, meld[i]);
            if(index!=-1){
                hand[index]="0";
                i++;
            }else{
                System.out.println("please enter a valid card");
            }
        }
        return meld;
    }

    public static int meldScore(String[] meld){
        int sum = 0;
        for (int i = 0; i<meld.length; i++){
            sum+=cardNum(meld[i]);
        }
        return sum;
    }

    public static int assessMeld(String[] cardArray){
        if (isRun(cardArray) || isSet(cardArray)){
            return meldScore(cardArray);
        }
        return 0;
    }

    public static int playMeld(String[] cardArray){
        int score = 0;
        while (true){
            System.out.println("Do you have any cards to play? (Yes/no)");
            String confirm = input.nextLine();
            if (confirm.toLowerCase() != "yes"){
                break;
            }
            String[] meld = chooseMeld(cardArray);
            score = assessMeld(meld);
        }
        return score;
    }

    public static boolean playedAllCards(String[] cardArray){
        for (int i = 0; i<cardArray.length; i++){
            if (cardArray[i]!="0"){
                return false;
            }
        }
        return true;
    }


}