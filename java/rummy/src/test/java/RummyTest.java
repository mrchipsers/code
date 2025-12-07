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
        String[] hand2 = {"8H", "4S", "2C", "7D", "4D", "9S", "7C", "8D", "2H", "9D"};
        String[] sort2 = {"2C", "2H", "4D", "4S", "7C", "7D", "8D", "8H", "9D", "9S"};
        String[] hand3 = {"6S", "10D", "3H", "1C", "10H", "6D", "3C", "1D", "6H", "3S"};
        String[] sort3 = {"1C", "1D", "3C", "3H", "3S", "6D", "6H", "6S", "10D", "10H"};
        assertArrayEquals(sort, Rummy.sortHand(hand));
        assertArrayEquals(sort2, Rummy.sortHand(hand2));
        assertArrayEquals(sort3, Rummy.sortHand(hand3));
    }

     @Test
    public void testSorter(){
        String[] hand = {"10H", "3H", "2D", "10S", "3D", "1S", "2S", "3S", "4S", "3C"};
        String[] sort = {"1S", "2D", "2S", "3C", "3D", "3H", "3S", "4S", "10H", "10S"};
        String[] hand2 = {"8H", "4S", "2C", "7D", "4D", "9S", "7C", "8D", "2H", "9D"};
        String[] sort2 = {"2C", "2H", "4D", "4S", "7C", "7D", "8D", "8H", "9D", "9S"};
        String[] hand3 = {"6S", "10D", "3H", "1C", "10H", "6D", "3C", "1D", "6H", "3S"};
        String[] sort3 = {"1C", "1D", "3C", "3H", "3S", "6D", "6H", "6S", "10D", "10H"};
        assertArrayEquals(sort, Rummy.sorter(hand));
        assertArrayEquals(sort2, Rummy.sorter(hand2));
        assertArrayEquals(sort3, Rummy.sorter(hand3));
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
        String[] hand3 = {"3S", "4S", "5S"};
        String[] hand4 = {"5H", "6H", "4H", "3H"};
        String[] handNotEnough = {"3S", "3C", "4H", "5H"};
        String[] HandWrongSuit = {"3S", "4S", "5C", "5D"};
        String[] all = {"1S", "2S", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C"};
        assertTrue(Rummy.isRun(hand3));
        assertTrue(Rummy.isRun(hand4));
        assertTrue(Rummy.isRun3(all));
        assertFalse(Rummy.isRun(handNotEnough));
        assertFalse(Rummy.isRun(HandWrongSuit));
    }

    @Test 
    public void testIsRun3(){
        String[] hand3 = {"3S", "4S", "5S"};
        String[] hand4 = {"5H", "6H", "4H", "3H"};
        String[] handNotEnough = {"3S", "3C", "4H", "5H"};
        String[] HandWrongSuit = {"3S", "4S", "5C", "5D"};
        String[] all = {"1S", "2S", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C"};
        assertTrue(Rummy.isRun3(hand3));
        assertTrue(Rummy.isRun3(hand4));
        assertTrue(Rummy.isRun3(all));
        assertFalse(Rummy.isRun3(handNotEnough));
        assertFalse(Rummy.isRun3(HandWrongSuit));
    }

    @Test
    public void testIndex(){
        String[] hand = {"5H", "6H", "4H", "3H", "10S", "3D"};
        assertEquals(2, Rummy.index(hand, "4H"));
        assertEquals(-1, Rummy.index(hand, "1C"));
    }

    @Test
    public void testMeldScore(){
        String[] hand = {"5H", "6H", "4H", "3H", "10S", "3D"};
        assertEquals(31, Rummy.meldScore(hand));
    }

    @Test
    public void testAssessMeld(){
        String[] valid1 = {"5H", "6H", "4H", "3H"};
        String[] valid2 = {"3S", "4S", "5S"};
        String[] invalid = {"3S", "3C", "4H", "5H"};
        assertEquals(18, Rummy.assessMeld(valid1));
        assertEquals(12, Rummy.assessMeld(valid2));
        assertEquals(0, Rummy.assessMeld(invalid));
    }

    @Test
    public void testPlayedAllCards(){
        String[] no = {"0", "0", "0", "3H", "10S", "3D"};
        String[] yes = {"0", "0", "0", "0", "0", "0"};
        assertFalse(Rummy.playedAllCards(no));
        assertTrue(Rummy.playedAllCards(yes));
    }
}
