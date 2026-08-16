import java.util.Scanner;

public class Main {
	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		double th[] = new double[1001];
		double r[] = new double[1001];
		r[1] = 1;
		th[1] = 0;
		for (int i = 1; i < 1000; i++) {
			r[i + 1] = Math.sqrt(r[i] * r[i] + 1);
			th[i + 1] = th[i] + Math.atan(1.0 / r[i]);
		}
		while (true) {
			int n = sc.nextInt();
			if (n == -1)
				break;
			System.out.printf("%.2f\n", r[n] * Math.cos(th[n]));
			System.out.printf("%.2f\n", r[n] * Math.sin(th[n]));
		}
	}
}