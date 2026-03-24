package com.rummy;

public class Deck{
    private Card[] deck = new Card[40];
    
    public Deck(){
        char[] suit = {'S', 'H', 'C', 'D'};
        int index = 0;
        for (int i = 0; i<suit.length; i++){
            for (int j = 1; j<11; j++){
                deck[index]= new Card(j, suit[i]);
                index++;
            }
        }
    }

    public int length() {
        return this.deck.length;
    }

    public Card[] getDeck(){
        return this.deck;
    }

    public Card getCard(int index){
        return this.deck[index];
    }

    public void setCard(int index, Card value){
        this.deck[index]=value;
    }

    public static Card dealCard(Deck cardArray){
        for (int i = 0; i<cardArray.length(); i++){
            if (cardArray.getCard(i)!=null){
                Card card = cardArray.getCard(i);
                cardArray.setCard(i, null);
                return card;
            }
        }
        return null;
    }

    public Deck sortHand(){
        boolean repeat=true;
        while (repeat){
            repeat=false;
            for (int i = 0; i<(this.deck.length-1); i++){
                if (Card.cardNum(hand[i])>Card.cardNum(hand[i+1]) || Card.cardNum(hand[i])==Card.cardNum(hand[i+1]) && Card.cardSuit(hand[i])>Card.cardSuit(hand[i+1])){
                    repeat = true;
                    Card temp = this.deck[i];
                    hand.setCard(i, hand.getCard(+1));
                    hand.setCard(i+1, temp);
                }
            }
        }
        return hand;
    }
}