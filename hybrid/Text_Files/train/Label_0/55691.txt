import static java.util.Arrays.deepToString;

import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		new Main().run();
	}
	Scanner sc = new Scanner(System.in);
	public void run() {
		for (;sc.hasNext();) {
			int n = sc.nextInt();
			if (n == 0) break;
			int y = sc.nextInt();
			
			int bestB = 0;
			double bestValue = -1;
			
			for (int iii = 0; iii < n; iii++) {
				int b = sc.nextInt();
				int r = sc.nextInt();
				int t = sc.nextInt();
				double v = 0;
				if (t == 1) {
					v = 1 + y * r / 100.0; 
				} else {
					v = Math.pow(1.0 + r / 100.0, y);
				}
				if (bestValue < v) {
					bestValue = v;
					bestB = b;
				}
			}
			System.out.println(bestB);
		}
	}
}