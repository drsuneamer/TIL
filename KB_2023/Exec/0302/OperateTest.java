package day01;

public class OperateTest {

	public static void main(String[] args) {
		int i = 100;
		int j = 0;
		
		// int형 으로 나누면 Java.lang.ArithmeticException: / by zero 발생
//		int result = i / j;
		
		double a = 100.0;
		double b = 0.0;
		
		double result2 = a / b;	// Infinity
		double result3 = a % b;	// NaN
		System.out.println(result2);
		
		if (!Double.isNaN(result3)) {
			System.out.println(result3);
		}
	}

}
