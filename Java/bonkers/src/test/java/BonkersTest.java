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
        assertEquals(true, Bonkers.allDigits("12345"));
        assertEquals(false, Bonkers.allDigits("1@345"));
    }
}

