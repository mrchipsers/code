import com.bonkers.*;
import org.junit.Test;
import static org.junit.Assert.*;
public class BonkersTest {
    @Test
    public void testInstructions(){

    }
    @Test
    public void testContainsCharacter(){
        assertEquals(false, Bonkers.containsCharacter("456", '2'));
        assertEquals(true, Bonkers.containsCharacter("456", '5'));
    }
}

