package com.rummy;
public class Card {
    private int number;
    private char suit;
    //TODO change colours to apply to which player owns that tile on the board, or default if none have it (for sequence specifically)
    private static final String BLUE = "\u001B[34m";
    private static final String RED = "\u001B[31m";
    private static final String RESET = "\u001B[0m";
    
    public Card(int number, char suit) {
        this.number = number;
        this.suit = suit;
    }

    public  static char cardSuit(Card card){
        return card.suit;
    }

    public static int cardNum(Card card){
        return card.number;
    }   

    @Override
    public boolean equals(Object object){
        if (object instanceof Card){
            Card card=(Card)object;
            return (card.suit==this.suit && card.number==this.number);
        }
        return false;
    }

    public String[] print() {
        String suitIcon = "";
        String numberIcon = "";
        
        String colour = RESET;
        switch (this.suit) {
            case 'H':
                suitIcon = "";
                colour = RED;
                break;
            case 'S':
                suitIcon = "󰣑";
                colour = BLUE;
                break;
            case 'D':
                suitIcon = "󰣏";
                colour = RED;
                break;
            case 'C':
                suitIcon = "󰣎";
                colour = BLUE;
                break;
        }
        switch (this.number) {
            case 1:
                numberIcon = " A";
                break;
            case 10:
                numberIcon = this.number + "";
                break;
            case 11:
                numberIcon = " J";
                break;
            case 12:
                numberIcon = " Q";
                break;
            case 13:
                numberIcon = " K";
                break;
            default:
                numberIcon = " " + this.number;
                break;
        }
        String[] card = {
            colour + "┌------┐", 
            "|      |",
            "| " + numberIcon + "" + suitIcon + "  |",
            "|      |",
            "└------┘" + RESET
        };
        return card;
    }
}

// Spade: 󰣑, heart: , diamond: 󰣏, clubs: 󰣎