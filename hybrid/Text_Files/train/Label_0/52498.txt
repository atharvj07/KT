import java.util.Scanner;

public class Main {
	public static void main(String args[]) {
		Scanner scn = new Scanner(System.in);
		int n,buf;
		while((n = scn.nextInt()) != 0) {
			int[][] ans = new int[n+1][n+1];
			for(int i = 0;i < n;i++) {
				buf = 0;
				for(int j = 0;j < n;j++) {
					ans[i][j] = scn.nextInt();
					buf += ans[i][j];
				}
				ans[i][n] = buf;
			}
			for(int j = 0; j <= n ;j++) {
				buf = 0;
				for(int i = 0;i < n;i++) {
					buf += ans[i][j];
				}
				ans[n][j] = buf;
			}

			for(int i = 0;i < n+1;i++) {
				for(int j = 0;j < n+1;j++) {
					System.out.print(String.format("%5d", ans[i][j]));
				}
				System.out.println();
			}

		}
	}
}
