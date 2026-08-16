import java.util.Scanner;

public class D {

	private void work() {
		Scanner sc = new Scanner(System.in);
		while (sc.hasNextInt()) {
			int n = sc.nextInt();
			int w = sc.nextInt();
			int m = sc.nextInt();
			int[][] a = new int[55][55];
			int[][] f = new int[55][55];
			int[] d = new int[55];
			int[] t = new int[55];
			int cur = 1;
			int rem = m;
			for (int i = 0; i < m; i++) {
				while (t[i] < n) {
					a[i][d[i]] = n - t[i] < rem ? n - t[i] : rem;
					f[i][d[i]] = cur;
					rem -= a[i][d[i]];
					t[i] += a[i][d[i]];
					d[i]++;
					if (rem == 0) {
						cur++;
						rem = m;
					}
				}
			}
			boolean ok = true;
			for (int i = 1; i <= n; i++) {
				int cnt = 0;
				for (int j = 0; j < m; j++) {
					for (int k = 0; k < d[j]; k++) {
						if (f[j][k] == i) {
							cnt++;
						}
					}
				}
				if (cnt > 2) {
					ok = false;
					break;
				}
			}
			if (ok) {
				System.out.println("YES");
				for (int i = 0; i < m; i++) {
					for (int j = 0; j < d[i]; j++) {
						System.out.printf("%d %.8f ", f[i][j], 1.0 * w
								* a[i][j] / m);
					}
					System.out.println();
				}
			} else {
				System.out.println("NO");
			}
		}
	}

	public static void main(String[] args) {
		new D().work();
	}

}
