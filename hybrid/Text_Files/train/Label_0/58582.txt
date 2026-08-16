import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] a = new int[n];
		for(int i = 0 ; i < n ; i++) a[i] = sc.nextInt();
		boolean[][] dp = new boolean[101][10010];
		dp[0][0] = true;
		for(int i = 0 ; i < n ; i++) {
			for(int j = 0 ; j <= 10000 ; j++) {
				if(dp[i][j] == true) {
					dp[i + 1][j] = true;
					dp[i + 1][j + a[i]] = true;
				}
			}
		}
		for(int i = 10000 ; i >= 0 ; i--) {
			if(i % 10 != 0 && dp[n][i] == true) {
				System.out.println(i);
				return;
			}
		}
		System.out.println(0);
	}
}
