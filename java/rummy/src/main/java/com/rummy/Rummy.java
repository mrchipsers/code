package com.rummy;
import java.util.Random;
import java.util.Scanner;
public class Rummy{
    static Scanner input = new Scanner(System.in);
    public static void main(String[] args) {
        runGame();
    }

    public static void print(Deck input){
        for (int i = 0; i<input.length(); i++){
            System.out.println(input.getCard(i).print());
        }
    }

    public static void redraw(Card[] hand, Deck deck, int position){
        hand[position]=Deck.dealCard(deck);
    }

    public static boolean isSet(Card[] meld){
        int count = 0;
        for (int a = 0; a<meld.length; a++){
            for (int b = 0; b<meld.length; b++){
                if (Card.cardNum(meld[a])==Card.cardNum(meld[b])){
                    count++;
                } 
            }
            if (count>2){
                return true;
            }else{
                count=0;
            }
        }
        return false;
    }

    public static boolean isRun(Deck meld) {
        if (meld.getDeck().length < 3) {
            return false;
        }
        Deck.sortHand(meld);
        for (int i = 1; i < meld.getDeck().length; i++) {
            if (Card.cardSuit(meld[i]) != Card.cardSuit(meld[0]) || Card.cardNum(meld[i]) != Card.cardNum(meld[0]) + i) {
                return false;
            }
        }
        return true;
    }

    // public static boolean isRun3(Card[] meld){
    //     for (int a = 0; a<meld.length; a++){
    //         for (int b = 0; b<meld.length; b++){
    //             for (int c = 0; c<meld.length; c++){
    //                 if (Card.cardNum(meld[a])==Card.cardNum(meld[b])-1 && Card.cardNum(meld[b])==Card.cardNum(meld[c])-1 && Card.cardSuit(meld[a])==Card.cardSuit(meld[b]) && Card.cardSuit(meld[b])==Card.cardSuit(meld[c]) && Card.cardSuit(meld[c])==Card.cardSuit(meld[a])){
    //                     return true;
    //                 }
    //             }
    //         }
    //     }
    //     return false;
    // }

    public static int index(Card[] cardArray, Card card){
        for (int i = 0; i<cardArray.length; i++){
            if (cardArray[i].equals(card)){
                return i;
            }
        }
        return -1;
    }

    public static Card selectCard(){
        System.out.println("Enter card number: ");
        int number=input.nextInt();
        System.out.println("Enter card suit: ");
        char suit=input.nextLine().charAt(0);
        return new Card(number, suit);
    }

    public static Card[] chooseMeld(Card[] hand){
        System.out.print("your hand: ");
        print(hand);
        System.out.println("How many cards will you play? ");
        int cards = input.nextInt();
        input.nextLine();
        Card[] meld = new Card[cards];
        for (int i = 0; i<cards;){
            System.out.println("play your card: ");
            meld[i]=selectCard();
            int index = index(hand, meld[i]);
            if(index!=-1){
                hand[index]=null;
                i++;
            }else{
                System.out.println("please enter a valid card");
            }
            print(hand);
        }
        return meld;
    }

    public static int meldScore(Card[] meld){
        int sum = 0;
        for (int i = 0; i<meld.length; i++){
            sum+=Card.cardNum(meld[i]);
        }
        return sum;
    }

    public static int assessMeld(Card[] cardArray){
        if (isRun(cardArray) || isSet(cardArray)){
            return meldScore(cardArray);
        }
        return 0;
    }

    public static int playMeld(Card[] cardArray){
        int score = 0;
        while (true){
            System.out.println("Do you have any cards to play? (yes/No)");
            String confirm = input.nextLine();
            if (!confirm.toLowerCase().equals("yes")){
                break;
            }
            Card[] meld = chooseMeld(cardArray);
            score += assessMeld(meld);
        }
        System.out.println("your score for this round: "+score);
        return score;
    }

    public static boolean playedAllCards(Card[] cardArray){
        for (int i = 0; i<cardArray.length; i++){
            if (cardArray[i]!=null){
                return false;
            }
        }
        return true;
    }

    public static void shuffleDeck(Deck cardArray){
        Random random = new Random();
        for (int i = 0; i<40; i++){
            int index = random.nextInt(40);
            Card temp = cardArray.getCard(i);
            cardArray.setCard(i, cardArray.getCard(index));
            cardArray.setCard(index, temp);
        }
    }

    public static Deck dealHand(Deck cardArray){
        Deck hand = new Deck();
        for (int i = 0; i<10; i++){
            hand[i]=hand.dealCard(cardArray);
        }
        return hand;
    }

    public static Card dealCard(Deck cardArray){
        for (int i = 0; i<cardArray.getDeck().length; i++){
            if (cardArray.getCard(i)!=null){
                Card card = cardArray.getCard(i);
                cardArray.setCard(i, null);
                return card;
            }
        }
        return null;
    }

    public static Deck sortHand(Deck hand){
        boolean repeat=true;
        while (repeat){
            repeat=false;
            for (int i = 0; i<(hand.getDeck().length-1); i++){
                if (Card.cardNum(hand[i])>Card.cardNum(hand[i+1]) || Card.cardNum(hand[i])==Card.cardNum(hand[i+1]) && Card.cardSuit(hand[i])>Card.cardSuit(hand[i+1])){
                    repeat = true;
                    Card temp = hand.getCard(i);
                    hand.setCard(i, hand.getCard(+1));
                    hand.setCard(i+1, temp);
                }
            }
        }
        return hand;
    }

    public static int runRound(){
        Deck deck = new Deck();
        shuffleDeck(deck);
        System.out.println("Your hand is: ");
        Deck hand = sortHand(dealHand(deck));
        print(hand);
        System.out.println("Would you like to swap any of your cards? (yes/No)");
        String confirm = input.nextLine();
        if (confirm.toLowerCase().equals("yes")){
            for (int i = 0; i<5;){
                System.out.println("What card would you like to swap? ");
                int card = index(hand, selectCard());
                if (card!=-1){
                    redraw(hand, deck, card);
                    print(sortHand(hand));
                    i++;
                }else{
                    System.out.println("Please enter a valid card. ");
                    continue;
                }
                System.out.println("Are there any more cards to swap? (yes/No)");
                if (!input.nextLine().toLowerCase().equals("yes")){
                    break;
                }
            }
        }
        int score = playMeld(hand);
        if (playedAllCards(hand)){
            score+=25;
            System.out.println("Congratulations, you received bonus 25 points for playing all your cards!!!");
        }
        System.out.println("This is your final score: "+score);
        return score;
    }

    public static void runGame(){
        int score = 0;
        while (true){
            score += runRound();
            System.out.println("Would you like to play again? ");
            if (input.nextLine().toLowerCase().equals("no")){
                break;
            }
        }
        System.out.println("Thanks for playing! this is your total score: "+score);
    }
}