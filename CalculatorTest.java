public class CalculatorTest {
    public static void main(String[] args) {
        Calculator calc = new Calculator();

        // Enable assertions with -ea when running
        assert calc.add(2, 3) == 5 : "Addition failed!";
        assert calc.add(10, -5) == 5 : "Addition with negative failed!";

        System.out.println("All assertions passed.");
    }
}
