import com.bonkers.*;
import org.junit.Test;
import static org.junit.Assert.*;
public class BonkersTest {
    @Test
    public void testContainsCharacter(){
        assertEquals(false, Bonkers.containsCharacter("456", '2'));
        assertEquals(true, Bonkers.containsCharacter("456", '5'));
    }

    @Test
    public void testConcatenateClues(){
        assertEquals("@ @ Close ", Bonkers.concatenateClues(2, 1));
        assertEquals("", Bonkers.concatenateClues(0, 0));
    }

    @Test
    public void testGetClues(){
        assertEquals("Congratulations! Your guess is correct!", Bonkers.getClues("12345", "12345"));
        assertEquals("@ @ @ Close Close ", Bonkers.getClues("12354", "12345"));
        assertEquals("@ Close Close Close Close ", Bonkers.getClues("13254", "12345"));
        assertEquals("@ @ Close Close ", Bonkers.getClues("12654", "12345"));
        assertEquals("Bonkers", Bonkers.getClues("1234", "6789"));
    }

    @Test
    public void testAllDigits(){
        assertTrue(Bonkers.allDigits("12345"));
        assertFalse(Bonkers.allDigits("1@345"));
    }

    public static boolean noRepeats(String secretNum){
        for (int i = 0; i<secretNum.length(); i++){
            for (int j = 0; j<secretNum.length(); j++){
                if (i!=j && secretNum.charAt(i)==secretNum.charAt(j)){
                    return false;
                }
            }
        }
        return true;
    }

    @Test
    public void testNoRepeats(){
        assertTrue(noRepeats("1234"));
        assertFalse(noRepeats("12234"));
    }
    @Test
    public void testGenerateSecretNum(){
        assertTrue(noRepeats(Bonkers.generateSecretNum(-3)));
        assertTrue(noRepeats(Bonkers.generateSecretNum(0)));
        assertTrue(noRepeats(Bonkers.generateSecretNum(1)));
        assertTrue(noRepeats(Bonkers.generateSecretNum(2)));
        assertTrue(noRepeats(Bonkers.generateSecretNum(3)));
        assertTrue(noRepeats(Bonkers.generateSecretNum(4)));
        assertTrue(noRepeats(Bonkers.generateSecretNum(5)));
        assertTrue(noRepeats(Bonkers.generateSecretNum(6)));
    }
}

