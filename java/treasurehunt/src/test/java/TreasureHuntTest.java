import com.treasurehunt.*;
import org.junit.Test;
import static org.junit.Assert.*;

public class TreasureHuntTest {
    @Test
    public void testGenerateRandomCoordinate() {
        assertTrue(TreasureHunt.generateTreasureCoordinate()>0 && TreasureHunt.generateTreasureCoordinate()<6);
    }

    @Test 
    public void testIsValidRow() {
        assertTrue(TreasureHunt.isValidRow("A"));
        assertTrue(TreasureHunt.isValidRow("B"));
        assertFalse(TreasureHunt.isValidRow("F"));
        assertTrue(TreasureHunt.isValidRow("a"));
        assertTrue(TreasureHunt.isValidRow("b"));
        assertFalse(TreasureHunt.isValidRow("f"));
    }

    @Test 
    public void testGetRowNumber() {
        assertTrue(TreasureHunt.getRowLetter(1)=='A');
        assertTrue(TreasureHunt.getRowLetter(3)=='C');
    }

    @Test
    public void testIsValidCoordinate() {
        assertTrue(TreasureHunt.isValidCoordinate(1));
        assertTrue(TreasureHunt.isValidCoordinate(3));
        assertTrue(TreasureHunt.isValidCoordinate(5));
        assertFalse(TreasureHunt.isValidCoordinate(7));
    }

    @Test 
    public void testIsTreasureFound() {
        assertTrue(TreasureHunt.isTreasureFound(2, 5, 2, 5));
        assertFalse(TreasureHunt.isTreasureFound(3, 5, 2, 5));
        assertFalse(TreasureHunt.isTreasureFound(2, 5, 2, 3));
    }

    @Test 
    public void testGetVerticalDirection() {
        assertEquals("North", TreasureHunt.getVerticalDirection(2, 4));
        assertEquals("South", TreasureHunt.getVerticalDirection(4, 2));
        assertEquals("", TreasureHunt.getVerticalDirection(2, 2));
        
    }

    @Test 
    public void testGetHorizontalDirection() {
        assertEquals("West", TreasureHunt.getHorizontalDirection(2, 4));
        assertEquals("East", TreasureHunt.getHorizontalDirection(4, 2));
        assertEquals("", TreasureHunt.getHorizontalDirection(2, 2));
        
    }

    @Test 
    public void testGetDirection() {
        assertEquals("Northeast", TreasureHunt.getDirection(2, 5, 4, 2));
        assertEquals("Southwest", TreasureHunt.getDirection(4, 2, 2, 5));
        assertEquals("East", TreasureHunt.getDirection(2, 5, 2, 2));
        assertEquals("", TreasureHunt.getDirection(2, 5, 2, 5));
    }

    @Test 
    public void testCalculateDifference() {
        assertEquals(3, TreasureHunt.calculateDifference(5, 2));
        assertEquals(3, TreasureHunt.calculateDifference(2, 5));
        assertEquals(0, TreasureHunt.calculateDifference(5, 5));
    }

    @Test 
    public void testCalculateDistance() {
        assertEquals(5, TreasureHunt.calculateDistance(2, 5, 4, 2));
        assertEquals(8, TreasureHunt.calculateDistance(1, 1, 5, 5));
        assertEquals(0, TreasureHunt.calculateDistance(2, 5, 2, 5));
    }

    @Test 
    public void testGetDistanceWord() {
        assertEquals("Found!", TreasureHunt.getDistanceWord(0));
        assertEquals("Nearby", TreasureHunt.getDistanceWord(1));
        assertEquals("Hot", TreasureHunt.getDistanceWord(3));
        assertEquals("Warm", TreasureHunt.getDistanceWord(5));
        assertEquals("Cold", TreasureHunt.getDistanceWord(8));
    }

    @Test 
    public void testGetClue() {
        assertEquals("Found!", TreasureHunt.getClue(2, 5, 2, 5));
        assertEquals("Direction: East\nDistance : Nearby", TreasureHunt.getClue(2, 5, 2, 4));
        assertEquals("Direction: Northeast\nDistance : Warm", TreasureHunt.getClue(2, 5, 4, 2));
    }
}
