import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n, m;
		int max, min;
		int k[];

		n = sc.nextInt();
		while (n-- != 0) {
			m = sc.nextInt();
			k = new int[m];
			max = Integer.MIN_VALUE;
			min = Integer.MAX_VALUE;
			for (int i = 0; i < m; i++) {
				k[i] = sc.nextInt();
			}
			for (int i = 1; i < m; i++) {
				int t = k[i] - k[i - 1];
				if (0 <= t) {
					max = Math.max(max, k[i] - k[i - 1]);
				} else {
					min = Math.min(min, k[i] - k[i - 1]);
				}
			}

			System.out.print(max == Integer.MIN_VALUE ? 0 : max);
			System.out.print(" ");
			System.out.println(min == Integer.MAX_VALUE ? 0 : -min);
		}
	}
}