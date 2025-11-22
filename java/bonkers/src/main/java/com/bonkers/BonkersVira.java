package com.bonkers;
import java.util.Scanner;
import java.util.Random;
public class BonkersVira{
	
	public static void main(String[] args){
		Scanner reader = new Scanner(System.in);//why do you have this
		runGame();
	}
	
	public static void instructions(int numDigits, int maxGuesses){
		System.out.println("You will have " + maxGuesses + " guesses to guess a " +numDigits+ " -digit number.");
		System.out.println("After each subsequent incorrect guess, you will be given clues categorized as follows:");
		System.out.println( );
		System.out.println("Clue:    Meaning:");
		System.out.println("Bonkers  None of the digits in your guess is correct.");
		System.out.println("Close    One digit is correct but in the wrong position.");
		System.out.println("@        One digit is correct and in the right position.");
	}
	
	public static boolean containsCharacter( String word, char literal){
		int length = word.length();
		int loop = 0;
		
		while (loop < length){//you can make this a for
			char check = word.charAt(loop);
			++loop;
			if (check == literal){
				return true;
			}
		}
		return false;
	}
	
	public static String generateSecretNum(int numDigits){
		Random makeNum = new Random();
		int loop = 0;
		String secretNum="";
		while(loop < numDigits){
			String num = ""+ makeNum.nextInt(10);
			String secretNumStore = secretNum+num;
			if (containsCharacter(secretNum, num.charAt(0))== false){
				secretNum= ""+secretNumStore;
				loop++;
			}
		}
		return secretNum;
	}
	
	public static String concatenateClues(int countAt, int countClose){
		String allClues = "";
		for (int loop =0; loop < countAt; loop++){
			allClues += "@ ";
		}
		for (int loop = 0; loop< countClose; loop++){
			allClues += "Close ";
		}
		return allClues;
	}
	
	public static String getClues( String secretNum, String userGuess){//did you copy my code for this
		int match = 0;
		int semiTrue = 0;
		if (secretNum.equals(userGuess)){
			return "Congratulations! Your guess is correct!";
		}
		for (int loop = 0;loop < secretNum.length(); loop++){
			if (secretNum.charAt(loop)==userGuess.charAt(loop)){
				match += 1;
			}
			else if (containsCharacter(secretNum, userGuess.charAt(loop))){
				semiTrue += 1;
			}
		}
		if (match==0 && semiTrue == 0){
			return "Bonkers";
		}
		else{
			return concatenateClues(match, semiTrue);
		}
	}
	
	public static void playRound(String secretNum, int maxGuesses){
		Scanner reader = new Scanner(System.in);
		for (int loop = 1; loop <= maxGuesses; loop++){
			String userGuess = reader.nextLine();
			System.out.println("Guess #" +loop +": " +userGuess);
			userGuess = valid(userGuess, secretNum.length());
			if (getClues(secretNum, userGuess).equals("Contratulations! Your guess is correct!")){
				System.out.println("Contratulations! Your guess is correct!");
				return;
			}
			else{
				System.out.println(getClues(secretNum, userGuess));
			}
		}
	System.out.println("You ran out of guesses.  The answer was " +secretNum+ ".  GAME OVER!!! Thanks for playing!");
	}
	
	public static void runGame(){
		Scanner reader = new Scanner(System.in);
		System.out.println("Enter number of digits of secret number:");
		int secretNumLength = reader.nextInt();
		System.out.println("Enter the number of guesses the player has:");
		int userGuessAmount = reader.nextInt();
		String secretNum= generateSecretNum(secretNumLength);
		instructions(userGuessAmount, secretNumLength);
		playRound(secretNum, userGuessAmount);
	}
	
	public static boolean allDigits(String userGuess){
		for (int loop = 0; loop < userGuess.length(); loop++){
			if (!(userGuess.charAt(loop) >= '0' && userGuess.charAt(loop) <= '9')){
				return false;
			}
		}
		return true;
	}
	
	public static String valid(String userGuess, int numDigits){
		Scanner reader = new Scanner(System.in);
		while (true){
			if(allDigits(userGuess)==true && (userGuess.length()==numDigits)){
				return userGuess;
			}
			System.out.println("Guess a number that is "+numDigits+ " digits long:");
			userGuess = reader.nextLine();
		}
	}
}