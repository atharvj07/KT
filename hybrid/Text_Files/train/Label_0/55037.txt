import java.util.Scanner;

public class Main {
	static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {
		int n = sc.nextInt();
		int m = sc.nextInt();

		int[] a = new int[m * 2];

		for (int i = 0; i < m * 2; i++) {
			a[i] = sc.nextInt();
		}

		for (int i = 1; i <= n; i++) {
			int count = 0;
			for (int j = 0; j < m * 2; j++) {
				if (a[j] == i) {
					count++;
				}
			}
			System.out.println(count);
		}

	}
}