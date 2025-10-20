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
        System.out.println("Bonkers\t\tNone of the digits in your guess is correct.");
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
        String num = "";
        int i = 0;
        while (i<numDigits){
            String nextNum = ""+random.nextInt(9);
            char nextNumChar = nextNum.charAt(0);
            if (!containsCharacter(num, nextNumChar)){
                num+=nextNum;
                i++;
            }
        }
        return num;
    }

    public static String concatenateClues(int countAt, int countCLose){
        String clue = "";
        for (int i = 0; i<countAt; i++){
            clue+="@ ";
        }
        for (int i = 0; i<countCLose; i++){
            clue+="Close ";
        }
        return clue;
    }

    public static String getClues(String secretNum, String userGuess){
        int close = 0;
        int on = 0;
        for (int i = 0; i<userGuess.length(); i++){
            if (!containsCharacter(secretNum, userGuess.charAt(i))){
                continue;
            }else{
                if (secretNum.charAt(i)==userGuess.charAt(i)){
                    on++;
                }else{
                    close++;
                }
            }
        }

        if (secretNum.equals(userGuess)){
            return "Congratulations! Your guess is correct!";
        }else if (concatenateClues(on, close)==""){
            return "Bonkers";
        }else{
            return concatenateClues(on, close);
        }

    }

    public static void playRound(String secretNum, int maxGuesses){
        Scanner input = new Scanner(System.in);
        for (int i = 0; i<maxGuesses; i++){
            System.out.println("guess number "+(i+1));
            String guess = ""+input.nextInt();
            guess = valid(guess, secretNum.length());
            if (getClues(secretNum, guess)=="Congratulations! Your guess is correct!"){
                System.out.println("Congratulations! Your guess is correct!");
                return;
            }else{
                System.out.println(getClues(secretNum, guess));
            }
        }
        input.close();
        System.out.println("You ran out of guesses. The answer was"+secretNum+". GAME OVER!!! Thanks for playing!");
    }

    public static void runGame(){
       Scanner input = new Scanner(System.in);
       System.out.println("Enter number of digits of secret number: "); 
       int numLength = input.nextInt();
       System.out.println("Enter the number of guesses the player has: "); 
       int maxGuesses = input.nextInt();
       String secretNum = generateSecretNum(numLength);
       instructions(numLength, maxGuesses);
       playRound(secretNum, maxGuesses);
    }

    public static boolean allDigits(String userGuess){
        for (int i = 0; i<userGuess.length(); i++){
            if (!(userGuess.charAt(i)>= '0' && userGuess.charAt(i)<= '9')){
                return false;
            }
        }
        return true;
    }

    public static String valid(String userGuess, int numDigits){
         Scanner input = new Scanner(System.in);
        while (true){
            if (allDigits(userGuess) && userGuess.length()==numDigits){
                return userGuess;
            }
            System.out.println("guess a number that is "+numDigits+"long: ");
            userGuess = input.nextLine();
            input.close();
        } 
    }
}