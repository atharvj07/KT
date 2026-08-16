
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();
		int[] p = new int[n + 1];
		int[][] m = new int[n + 1][n + 1];

		for (int i = 0; i < n; i++) {
			p[i] = scan.nextInt();
			p[i + 1] = scan.nextInt();
		}
		

		// (M1)(M2M3M4M5) l=2
		// (M1M2)(M3M4M5) l=3
		for (int l = 2; l <= n; l++) {
			for (int i = 1; i <= n - l + 1; i++) {
				int j = i + l - 1;
				m[i][j] = (1 << 21);
				for (int k = i; k <= j - 1; k++) {
					m[i][j] = Math.min(m[i][j], m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]);
				}
			}
		}
		
		System.out.println(m[1][n]);
		scan.close();
	}
}