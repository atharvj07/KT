import static java.util.Arrays.deepToString;

import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		new Main().run();
	}
	void tr(Object... os) {
		System.err.println(deepToString(os));
	}

	Scanner sc = new Scanner(System.in);
	public void run() {
		for (;sc.hasNext();) {
			int n = sc.nextInt();
			if (n == 0) break;
			int[] a = new int[10];
			for (int i = 0; i < n; i++) {
				a[sc.nextInt()]++;
			}
			for (int i = 0; i < 10; i++) {
				if (a[i] == 0) System.out.println("-");
				else {
					for (int j = 0; j < a[i]; j++) {
						System.out.print("*");
					}
					System.out.println();
				}
			}
		}
	}
}