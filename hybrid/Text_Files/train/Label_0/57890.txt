import java.util.Scanner;

public class Main {

	static Scanner sc = new Scanner(System.in);

	public static void main(String[] a) {
		int N = sc.nextInt();
		int[][] g = new int[N][N];
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < N; ++j) {
				g[i][j] = sc.nextInt();
			}
		}
		long ans = 0;
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < i; ++j) {
				ans += Math.min(g[i][j], g[j][i]);
			}
		}
		System.out.println(ans);
	}

}