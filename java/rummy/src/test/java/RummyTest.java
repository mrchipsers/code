import com.rummy.Rummy;
import static org.junit.Assert.*;
import org.junit.Test;
public class RummyTest {
    @Test
    public void testBuildDeck(){
        String[] expected = {"1S", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "1H", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "1C", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "1D", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D"};
        assertArrayEquals(expected, Rummy.buildDeck());
    }

    @Test
    public void testDealCard(){
        String[] nothing = {"0", "0", "0", "0"};
        String[] something = {"0", "0", "3D", "4C", "1H"};
        assertEquals("nothing left", Rummy.dealCard(nothing));
        assertEquals(something[2], Rummy.dealCard(something));
    }

    @Test
    public void testDealHand(){
        String[] deck = {"1S", "2S", "3S", "4S", "3H", "4H", "5H", "6H", "8C", "9C", "10C", "1D", "2D"};
        String[] expected = {"1S", "2S", "3S", "4S", "3H", "4H", "5H", "6H", "8C", "9C"};
        assertArrayEquals(expected, Rummy.dealHand(deck));
    }

    @Test
    public void testCardSuit(){
        assertEquals('C', Rummy.cardSuit("3C"));
        assertEquals('C', Rummy.cardSuit("10C"));
        assertEquals('H', Rummy.cardSuit("1H"));
    }

    @Test
    public void testCardNum(){
        assertEquals(1, Rummy.cardNum("1C"));
        assertEquals(10, Rummy.cardNum("10C"));
        assertEquals(5, Rummy.cardNum("5C"));
    }

    @Test
    public void testSortHand(){
        String[] hand = {"10H", "3H", "2D", "10S", "3D", "1S", "2S", "3S", "4S", "3C"};
        String[] sort = {"1S", "2D", "2S", "3C", "3D", "3H", "3S", "4S", "10H", "10S"};
        assertArrayEquals(sort, Rummy.sortHand(hand));
    }

    @Test
    public void testIsSet(){
        String[] hand3 = {"3S", "3C", "4H", "3H"};
        String[] hand4 = {"3S", "3C", "4H", "3H", "10S", "3D"};
        String[] hand0 = {"3S", "3C", "4H", "5H"};
        assertTrue(Rummy.isSet(hand3));
        assertTrue(Rummy.isSet(hand4));
        assertFalse(Rummy.isSet(hand0));
    }

    @Test 
    public void testIsRun(){
        String[] hand3 = {"3S", "4S", "5S", "3H"};
        String[] hand4 = {"5H", "6H", "4H", "3H", "10S", "3D"};
        String[] hand0 = {"3S", "3C", "4H", "5H"};
        assertTrue(Rummy.isRun(hand3));
        assertTrue(Rummy.isRun(hand4));
        assertFalse(Rummy.isRun(hand0));
    }

    @Test
    public void testIndex(){
        String[] hand = {"5H", "6H", "4H", "3H", "10S", "3D"};
        assertEquals(2, Rummy.index(hand, "4H"));
        assertEquals(-1, Rummy.index(hand, "1C"));
    }
}
