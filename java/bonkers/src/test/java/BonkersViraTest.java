import com.bonkers.*;
import org.junit.Test;
import static org.junit.Assert.*;
public class BonkersViraTest {
    @Test
    public void testContainsCharacter(){
        assertEquals(false, BonkersVira.containsCharacter("456", '2'));
        assertEquals(true, BonkersVira.containsCharacter("456", '5'));
    }

    @Test
    public void testConcatenateClues(){
        assertEquals("@ @ Close ", BonkersVira.concatenateClues(2, 1));
        assertEquals("", BonkersVira.concatenateClues(0, 0));
    }

    @Test
    public void testGetClues(){
        assertEquals("Congratulations! Your guess is correct!", BonkersVira.getClues("12345", "12345"));
        assertEquals("@ @ @ Close Close ", BonkersVira.getClues("12354", "12345"));
        assertEquals("@ Close Close Close Close ", BonkersVira.getClues("13254", "12345"));
        assertEquals("@ @ Close Close ", BonkersVira.getClues("12654", "12345"));
        assertEquals("Bonkers", BonkersVira.getClues("1234", "6789"));
    }

    @Test
    public void testAllDigits(){
        assertTrue(BonkersVira.allDigits("12345"));
        assertFalse(BonkersVira.allDigits("1@345"));
        assertTrue(BonkersVira.allDigits("0123"));
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
        for (int i = 0; i<50; i++){
            assertTrue(noRepeats(BonkersVira.generateSecretNum(-3)) && BonkersVira.generateSecretNum(-3).length()==0);
            assertTrue(noRepeats(BonkersVira.generateSecretNum(0)) && BonkersVira.generateSecretNum(0).length()==0);
            assertTrue(noRepeats(BonkersVira.generateSecretNum(1)) && BonkersVira.generateSecretNum(1).length()==1);
            assertTrue(noRepeats(BonkersVira.generateSecretNum(2)) && BonkersVira.generateSecretNum(2).length()==2);
            assertTrue(noRepeats(BonkersVira.generateSecretNum(3)) && BonkersVira.generateSecretNum(3).length()==3);
            assertTrue(noRepeats(BonkersVira.generateSecretNum(4)) && BonkersVira.generateSecretNum(4).length()==4);
            assertTrue(noRepeats(BonkersVira.generateSecretNum(5)) && BonkersVira.generateSecretNum(5).length()==5);
            assertTrue(noRepeats(BonkersVira.generateSecretNum(6)) && BonkersVira.generateSecretNum(6).length()==6);
        }
    }
}

