
import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {

		new Main().run();
	}

	private void run() {
		Scanner scanner = new Scanner(System.in);
		loop:
		while (true) {
			int n = scanner.nextInt();
			if (n == 0)
				break;
			Integer[] a = new Integer[n];
			Integer[] b = new Integer[n];
			for (int i = 0; i < n; i++)
				a[i] = scanner.nextInt();
			for (int i = 0; i < n; i++)
				b[i] = scanner.nextInt();
			Arrays.sort(a, Collections.reverseOrder());
			Arrays.sort(b, Collections.reverseOrder());
			n /= 2;
			for (int i = 0; i < n; i++) {
				if (a[i * 2] > b[i]) {
					System.out.println((i * 2) + 1);
					continue loop;
				}
			}
			System.out.println("NA");
		}
	}
}