import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		while (scan.hasNext()) {
			String[] data = scan.nextLine().split(" ", 0);
			double[] num = new double[6];
			for (int i = 0; i < 6; i++) {
				num[i] = Double.parseDouble(data[i]);
			}
			double x = (num[2]*num[4]-num[1]*num[5])/(num[0]*num[4]-num[1]*num[3]);
			if (abs(x) < 10E-9) x = 0;
			double y = -(num[2]*num[3]-num[0]*num[5])/(num[0]*num[4]-num[1]*num[3]);
			if (abs(y) < 10E-9) y = 0;
			String sx = String.format("%.3f", x);
			String sy = String.format("%.3f", y);
			System.out.println(sx + " " + sy);
		}
	}

	private static double abs(double x) {
		if (x >= 0) return x;
		else return -x;
	}
}