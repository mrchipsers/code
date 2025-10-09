import com.tripevaluator.TripEvaluator;
import org.junit.Test;
import static org.junit.Assert.assertEquals;
public class TripEvaluatorTest {
    @Test
    public void testCalculateCarCost() {
        assertEquals(50.0,(TripEvaluator.calculateCarCost(50, 30)[0]), 1e-6);
        assertEquals(0.5,(TripEvaluator.calculateCarCost(50, 30)[1]), 1e-6);
    }

    @Test
    public void testCalculateFlightCost() {
        assertEquals(1200.0, (TripEvaluator.calculateFlightCost(5000)[0]), 1e-6);
        assertEquals(8.555555555555555,(TripEvaluator.calculateFlightCost(5000)[1]),1e-6);
    }

    @Test
    public void testCalculateTrainCost() {
        assertEquals(125.0,(TripEvaluator.calculateTrainCost(500)[0]), 1e-6);
        assertEquals(1.9285714285714286,(TripEvaluator.calculateTrainCost(500)[1]), 1e-6);
    }

    @Test
    public void testDecimalTimeConvert() {
        assertEquals(0,(TripEvaluator.decimalTimeConvert(0.5)[0]));
        assertEquals(30,(TripEvaluator.decimalTimeConvert(0.5)[1]));
        assertEquals(8,(TripEvaluator.decimalTimeConvert(8.555555555555555)[0]));
        assertEquals(33,(TripEvaluator.decimalTimeConvert(8.555555555555555)[1]));
        assertEquals(1,(TripEvaluator.decimalTimeConvert(1.9285714285714286)[0]));
        assertEquals(55,(TripEvaluator.decimalTimeConvert(1.9285714285714286)[1]));
    }
    
    @Test
    public void testTripEval(){
        assertEquals("You should take the train. it costs "+125.0+" and will take "+1+" hours and "+55+" minutes",TripEvaluator.tripEval(500,30));
        assertEquals("You should take the plane. it costs "+1200.0+" and will take "+8+" hours and "+33+" minutes",TripEvaluator.tripEval(5000,30));
        assertEquals("You should take the car. it costs "+0.4+" and will take "+0+" hours and "+0+" minutes",TripEvaluator.tripEval(1,0));
        assertEquals(null, TripEvaluator.tripEval(-1, 30));
        assertEquals(null, TripEvaluator.tripEval(30, -1));
    }

    @Test
    public void TripEvaluator(){
        new TripEvaluator();
    }
}
