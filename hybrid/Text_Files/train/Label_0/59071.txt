
import java.io.IOException;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws IOException {

		new Main().run();
	}

	private void run() throws IOException {
		Scanner scanner = new Scanner(System.in);
		while (true) {
			int n = scanner.nextInt();
			int m = scanner.nextInt();
			if ((n | m) == 0)
				break;
			int[] pow3 = new int[n + 1];
			pow3[0] = 1;
			for (int i = 1; i <= n; i++)
				pow3[i] = pow3[i - 1] * 3;
			int[] c = new int[n];
			for (int i = 0; i < 3; i++) {
				int a = scanner.nextInt();
				for (int j = a; j > 0; j--) {
					int b = scanner.nextInt();
					c[n - b] = i;
				}
			}
			int p = 0;
			int x = 0;
			for (int i = 0; i < n; i++) {
				int d = Math.abs(p - c[i]);
				x += pow3[i] * d;
				if (d == 1)
					p = 2 - p;
			}
			int y = pow3[n] - x - 1;
			x = Math.min(x, y);
			System.out.println(x > m ? -1 : x);
		}
	}
}