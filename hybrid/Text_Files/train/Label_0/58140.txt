import java.util.Scanner;

public class Main {

	private static long[][] dp;
	private static long[] input = new long[1000];
	
	public static void main(String[] args) {							
	
		Scanner scan = new Scanner(System.in);
		
		int i , j , n , k , x;
		long ans = - 1;
		
		n = scan.nextInt();
		k = scan.nextInt();
		x = scan.nextInt();
		
		for (i = 0;i < n;i ++) {
			input[i] = scan.nextLong();
		}
		
		dp = new long[n][x + 1];
		for (i = 0;i < n;i ++) {
			for (j = 0;j < x + 1;j ++) {
				dp[i][j] = - 1;
			}
		}
		
		for (i = 0;i < n;i ++) {
			dp[i][0] = 0;
			if (i <= k - 1) {
				dp[i][1] = input[i];
			}
			for (j = 0;j < i;j ++) {
				for (int time = 1;time < x;time ++) {			
					if (dp[j][time] >= 0 && (i - j) <= k) {
						long temp = dp[j][time] + input[i];
						if (temp > dp[i][time + 1]) {
							dp[i][time + 1] = temp;
						}
					}					
				}
			}				
		}
		
		for (i = 0;i < n;i ++) {
			if (dp[i][x] >= 0) {
				int remain = n - 1 - i;
				if (remain <= k - 1) {
					if (dp[i][x] > ans) {
						ans = dp[i][x];
					}
				}
			}
		}
		
		System.out.println(ans);
		
	}
	
}













