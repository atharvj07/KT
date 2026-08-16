import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		double x1 = sc.nextDouble();
		double y1 = sc.nextDouble();
		double x2 = sc.nextDouble();
		double y2 = sc.nextDouble();
		double xx = x2 - x1;
		double yy = y2 - y1;
		double xxyy = xx * xx + yy * yy;
		System.out.println(Math.sqrt(xxyy));
	}
}
