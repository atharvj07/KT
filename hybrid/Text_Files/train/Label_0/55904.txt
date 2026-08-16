
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
			int[] map = new int[n];
			for (int i = 0; i < n; i++)
				map[i] = scanner.nextInt();
			int[] a = new int[m];
			for (int i = 0; i < m; i++)
				a[i] = scanner.nextInt();
			int x = 0;
			for (int i = 0; i < m; i++) {
				x = Math.min(n - 1, a[i] + x);
				x += map[x];
				if (x >= n - 1) {
					System.out.println(i + 1);
					break;
				}
			}

		}
	}
}