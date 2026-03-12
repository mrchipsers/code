package com.rummy;

public class Deck{
    private Card[] deck = new Card[40];
    private char[] suit = {'S', 'H', 'C', 'D'};
    
    public Deck(){
        this.deck = buildDeck();
    }

    private Card[] buildDeck(){
        int index = 0;
        for (int i = 0; i<suit.length; i++){
            for (int j = 1; j<11; j++){
                deck[index]= new Card(j, suit[i]);
                index++;
            }
        }
        return deck;
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
}