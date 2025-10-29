package com.bonkers;
import java.util.Scanner;
import java.util.Random;
public class Bonkers {
    static Scanner input = new Scanner(System.in);
    public static void main(String[] args){
        //runGame();
        validInt(10);
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
            String nextNum = ""+random.nextInt(10);
            if (!containsCharacter(num, nextNum.charAt(0))){
                num+=nextNum;
                i++;
            }
        }
        return num;
    }
    
    public static String generateSecretNum2(int numDigits){
        Random makeNum = new Random();
        int loop = 0;
        String secretNum="";
        while(loop < numDigits){
            String num = ""+makeNum.nextInt(10);
            String secretNumStore = secretNum+num;
            if (containsCharacter(secretNum, num.charAt(0))== false){
                secretNum= ""+secretNumStore;
                loop++;
            }
        }
        return secretNum;
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
        
        if (secretNum.equals(userGuess)){
            return "Congratulations! Your guess is correct!";
        }
        
        for (int i = 0; i<userGuess.length(); i++){
            if(secretNum.charAt(i)==userGuess.charAt(i)){ 
                on++;
            }else if (containsCharacter(secretNum, userGuess.charAt(i))){
                close++;
            }
        }
        
        if (close==0 && on==0){
            return "Bonkers";
        }else{
            return concatenateClues(on, close);
        }

    }

    public static void playRound(String secretNum, int maxGuesses){
        for (int i = 0; i<maxGuesses; i++){
            System.out.println("guess number "+(i+1));
            String guess = valid(secretNum.length());
            if (getClues(secretNum, guess).equals("Congratulations! Your guess is correct!")){
                System.out.println("Congratulations! Your guess is correct!");
                return;
            }else{
                System.out.println(getClues(secretNum, guess));
            }
        }
        System.out.println("You ran out of guesses. The answer was "+secretNum+". GAME OVER!!! Thanks for playing!");
    }

    public static void runGame(){
        int numLength = 0;
        boolean goodLen = false;
        while (!goodLen){
            System.out.println("Enter the number of digits in the secret number (max of 10): "); 
            numLength = validInt(10); 
            
            if (numLength<11 && numLength>0){
                goodLen = true;
            }
        }
        
        System.out.println("Enter the number of guesses the player has: "); 
        int maxGuesses = validInt(Integer.MAX_VALUE);
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

    public static String valid( int numDigits){
        String userIn = "";
        while (true) {
            try {
                userIn = input.nextLine();
                if (allDigits(userIn) && userIn.length()==numDigits){
                    return userIn;
                }
                System.out.println("guess a number that is "+numDigits+" digits long: ");
                userIn = input.nextLine();
            } catch (Exception e) {
                System.out.println("Please enter a "+numDigits+" long number. Try again.");
                return valid(numDigits);
            }
        }
    }

    public static int validInt( int max){
        int userIn;
        while (true){
            try {
                userIn = input.nextInt();
                if (userIn<=max){
                    return userIn;
                }    
                System.out.println("enter a number: ");
            } catch (Exception e) {
                System.out.println("Please enter a valid number. Try again.");
                input.nextLine();
            }    
        }
    }
}