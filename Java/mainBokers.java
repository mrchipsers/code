public class mainBokers {
    public static void main(String[] args){
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
}
