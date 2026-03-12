import com.rummy.Rummy;
import com.rummy.Deck;
import com.rummy.Card;
import static org.junit.Assert.*;
import org.junit.Test;
public class RummyTest {
    @Test
    public void testBuildDeck(){
        Card[] expected = {new Card(1,'S'), new Card(2,'S'), new Card(3,'S'), new Card(4,'S'), new Card(5,'S'), new Card(6,'S'), new Card(7,'S'), new Card(8,'S'), new Card(9,'S'), new Card(10,'S'), new Card(1,'H'), new Card(2,'H'), new Card(3,'H'), new Card(4,'H'), new Card(5,'H'), new Card(6,'H'), new Card(7,'H'), new Card(8,'H'), new Card(9,'H'), new Card(10,'H'), new Card(1,'C'), new Card(2,'C'), new Card(3,'C'), new Card(4,'C'), new Card(5,'C'), new Card(6,'C'), new Card(7,'C'), new Card(8,'C'), new Card(9,'C'), new Card(10,'C'), new Card(1,'D'), new Card(2,'D'), new Card(3,'D'), new Card(4,'D'), new Card(5,'D'), new Card(6,'D'), new Card(7,'D'), new Card(8,'D'), new Card(9,'D'), new Card(10,'D')};
        assertArrayEquals(expected, new Deck());
    }

    @Test
    public void testDealCard(){
        deck nothing = {null, null, null, null};
        deck something = {null, null, new Card(3,'D'), new Card(4, 'C'), new Card(1, 'H')};
        assertEquals(null, Deck.dealCard(nothing));
        assertEquals(something[2], Deck.dealCard(something));
    }

    @Test
    public void testDealHand(){
        Card[] deck = {new Card(1,'S'), new Card(2,'S'), new Card(3,'S'), new Card(4,'S'), new Card(3,'H'), new Card(4,'H'), new Card(5,'H'), new Card(6,'H'), new Card(8,'C'), new Card(9,'C'), new Card(10,'C'), new Card(1,'D'), new Card(2,'D')};
        Card[] expected = {new Card(1,'S'), new Card(2,'S'), new Card(3,'S'), new Card(4,'S'), new Card(3,'H'), new Card(4,'H'), new Card(5,'H'), new Card(6,'H'), new Card(8,'C'), new Card(9,'C')};
        assertArrayEquals(expected, Deck.dealHand(deck));
    }

    @Test
    public void testCardSuit(){
        assertEquals('C', Card.cardSuit(new Card(3, 'C')));
        assertEquals('C', Card.cardSuit(new Card(10, 'C')));
        assertEquals('H', Card.cardSuit(new Card(1, 'H')));
    }

    @Test
    public void testCardNum(){
        assertEquals(1, Card.cardNum(new Card(1, 'C')));
        assertEquals(10, Card.cardNum(new Card(10, 'H')));
        assertEquals(5, Card.cardNum(new Card(5, 'C')));
    }

    @Test
    public void testSortHand(){
        Card[] hand = {new Card(10,'H'), new Card(3,'H'), new Card(2,'D'), new Card(10,'S'), new Card(3,'D'), new Card(1,'S'), new Card(2,'S'), new Card(3,'S'), new Card(4,'S'), new Card(3,'C')};
        Card[] sort = {new Card(1,'S'), new Card(2,'D'), new Card(2,'S'), new Card(3,'C'), new Card(3,'D'), new Card(3,'H'), new Card(3,'S'), new Card(4,'S'), new Card(10,'H'), new Card(10,'S')};
        Card[] hand2 = {new Card(8,'H'), new Card(4,'S'), new Card(2,'C'), new Card(7,'D'), new Card(4,'D'), new Card(9,'S'), new Card(7,'C'), new Card(8,'D'), new Card(2,'H'), new Card(9,'D')};
        Card[] sort2 = {new Card(2,'C'), new Card(2,'H'), new Card(4,'D'), new Card(4,'S'), new Card(7,'C'), new Card(7,'D'), new Card(8,'D'), new Card(8,'H'), new Card(9,'D'), new Card(9,'S')};
        Card[] hand3 = {new Card(6,'S'), new Card(10,'D'), new Card(3,'H'), new Card(1,'C'), new Card(10,'H'), new Card(6,'D'), new Card(3,'C'), new Card(1,'D'), new Card(6,'H'), new Card(3,'S')};
        Card[] sort3 = {new Card(1,'C'), new Card(1,'D'), new Card(3,'C'), new Card(3,'H'), new Card(3,'S'), new Card(6,'D'), new Card(6,'H'), new Card(6,'S'), new Card(10,'D'), new Card(10,'H')};
        assertArrayEquals(sort, Deck.sortHand(hand));
        assertArrayEquals(sort2, Deck.sortHand(hand2));
        assertArrayEquals(sort3, Deck.sortHand(hand3));
    }

    @Test
    public void testIsSet(){
        Card[] hand3 = {new Card(3,'S'), new Card(3,'C'), new Card(4,'H'), new Card(3,'H')};
        Card[] hand4 = {new Card(3,'S'), new Card(3,'C'), new Card(4,'H'), new Card(3,'H'), new Card(10,'S'), new Card(3,'D')};
        Card[] hand0 = {new Card(3,'S'), new Card(3,'C'), new Card(4,'H'), new Card(5,'H')};
        assertTrue(Rummy.isSet(hand3));
        assertTrue(Rummy.isSet(hand4));
        assertFalse(Rummy.isSet(hand0));
    }

    @Test 
    public void testIsRun(){
        Card[] hand3 = {new Card(3,'S'), new Card(4,'S'), new Card(5,'S')};
        Card[] hand4 = {new Card(5,'H'), new Card(6,'H'), new Card(4,'H'), new Card(3,'H')};
        Card[] handNotEnough = {new Card(3,'S'), new Card(3,'C'), new Card(4,'H'), new Card(5,'H')};
        Card[] HandWrongSuit = {new Card(3,'S'), new Card(4,'S'), new Card(5,'C'), new Card(5,'D')};
        Card[] all = {new Card(1,'C'), new Card(2,'C'), new Card(3,'C'), new Card(4,'C'), new Card(5,'C'), new Card(6,'C'), new Card(7,'C'), new Card(8,'C'), new Card(9,'C'), new Card(10,'C')};
        assertTrue(Rummy.isRun(hand3));
        assertTrue(Rummy.isRun(hand4));
        assertTrue(Rummy.isRun3(all));
        assertFalse(Rummy.isRun(handNotEnough));
        assertFalse(Rummy.isRun(HandWrongSuit));
    }

    @Test 
    public void testIsRun3(){
        Card[] hand3 = {new Card(3,'S'), new Card(4,'S'), new Card(5,'S')};
        Card[] hand4 = {new Card(5,'H'), new Card(6,'H'), new Card(4,'H'), new Card(3,'H')};
        Card[] handNotEnough = {new Card(3,'S'), new Card(3,'C'), new Card(4,'H'), new Card(5,'H')};
        Card[] HandWrongSuit = {new Card(3,'S'), new Card(4,'S'), new Card(5,'C'), new Card(5,'D')};
        Card[] all = {new Card(1,'S'), new Card(2,'S'), new Card(3,'C'), new Card(4,'C'), new Card(5,'C'), new Card(6,'C'), new Card(7,'C'), new Card(8,'C'), new Card(9,'C'), new Card(10,'C')};
        assertTrue(Rummy.isRun3(hand3));
        assertTrue(Rummy.isRun3(hand4));
        assertTrue(Rummy.isRun3(all));
        assertFalse(Rummy.isRun3(handNotEnough));
        assertFalse(Rummy.isRun3(HandWrongSuit));
    }

    @Test
    public void testIndex(){
        Card[] hand = {new Card(5,'H'), new Card(6,'H'), new Card(4,'H'), new Card(3,'H'), new Card(10,'S'), new Card(3,'D')};
        assertEquals(2, Rummy.index(hand, new Card(4,'H')));
        assertEquals(-1, Rummy.index(hand, new Card(1,'C')));
    }

    @Test
    public void testMeldScore(){
        Card[] hand = {new Card(5,'H'), new Card(6,'H'), new Card(4,'H'), new Card(3,'H'), new Card(10,'S'), new Card(3,'D')};
        assertEquals(31, Rummy.meldScore(hand));
    }

    @Test
    public void testAssessMeld(){
        Card[] valid1 = {new Card(5,'H'), new Card(6,'H'), new Card(4,'H'), new Card(3,'H')};
        Card[] valid2 = {new Card(3,'S'), new Card(4,'S'), new Card(5,'S')};
        Card[] invalid = {new Card(3,'S'), new Card(3,'C'), new Card(4,'H'), new Card(5,'H')};
        assertEquals(18, Rummy.assessMeld(valid1));
        assertEquals(12, Rummy.assessMeld(valid2));
        assertEquals(0, Rummy.assessMeld(invalid));
    }

    @Test
    public void testPlayedAllCards(){
        Card[] no = {null, null, null, new Card(3,'H'), new Card(10,'S'), new Card(3,'D')};
        Card[] yes = {null, null, null, null, null, null};
        assertFalse(Rummy.playedAllCards(no));
        assertTrue(Rummy.playedAllCards(yes));
    }
}
