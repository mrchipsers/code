package com.bonkers;
import java.util.Scanner;
import java.util.Random;
public class Bonkers {
    public static void main(String[] args){
        runGame();
    }

    public static void instructions(int numDigits, int maxGuesses){
        System.out.println("you will have "+maxGuesses+" guesses to guess a "+numDigits+" digit number. After each subsequent incorrect guess, you will be given clues categorized as follows:");
        System.out.println("Clue:\t\tMeaning:");
        System.out.println("Bonkers\tNone of the digits in your guess is correct.");
        System.out.println("Close\t\tOne digit is correct but in the wrong position.");
        System.out.println("@\t\tOne digit is correct and in the right position.");
    }

    public static boolean containsCharacter(String word, char literal){
        for (int i = 0; i<word.length(); i++){
            if (word.charAt(i)==literal){
                return true;
            }
        }
        return false;
    }

    public static String generateSecretNum(int numDigits){
        Random random = new Random();
        String num;
        for (int i = 0; i<numDigits; i++){
            
        }
    }

    public static String concatenateClues(int countAt, int countCLose){

    }

    public static String getClues(String secretNum, String userGuess){

    }

    public static void playRound(String secretNum, int maxGuesses){

    }

    public static void runGame(){

    }

    public static boolean allDigits(String userGuess){

    }

    public static String valid(String userGuess, int numDigits){

    }
}