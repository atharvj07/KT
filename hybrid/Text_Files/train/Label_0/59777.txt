import java.util.*;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		double[] arr = new double[n];
		double[] acc = new double[n + 1];
		acc[0] = 0;
		for (int i=0;i<n;i++) {
			arr[i] = sc.nextInt();
			acc[i + 1] = acc[i] + arr[i];
		}
		double [][] dp = new double[n + 1][m + 1];
		for (int i=0;i<n+1;i++) {
			for (int j=0;j<m+1;j++) {
				dp[i][j] = Integer.MIN_VALUE;
			}
		}
		dp[0][0] = 0;
		for (int i=1;i<n+1;i++) {
			for (int j=1;j<Math.min(m+1,i+1);j++) {
				for (int k=j-1;k<i;k++) {
					dp[i][j] = Math.max(dp[i][j], dp[k][j - 1] + (acc[i] - acc[k]) / (i - k));
				}
			}
		}
		System.out.printf("%.6f", dp[n][m]);
	}
}

