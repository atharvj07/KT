import java.util.Scanner;

public class Main {

	public static void main(String[] args) { //No MLE!
		Scanner input = new Scanner(System.in);
		int N = input.nextInt(); 
		long[][] dp;
		long[] arr = new long[N];
		for (int i = 0; i < N; i++) {
			arr[i] = input.nextLong();
		}
		if (N%2==0) {
			dp = new long[N/2][2];
			for (int i = 0; i < N/2; i++) {
				for (int j = 0; j < 2; j++) {
					if (i==0&&j==0) {
						dp[i][j] = arr[i*2+j];
					}
					else if (j==0) {
						dp[i][j] = dp[i-1][j]+arr[i*2];
					}
					else if (i>0){
						dp[i][j] = dp[i][j-1];
						long curNum = arr[i*2+1];
						dp[i][j] = Math.max(dp[i][j], curNum+dp[i-1][j]);
					}else if (i==0) {
						dp[i][j] = Math.max(dp[i][j-1],arr[i*2+1]);
					}	
				}
			}
			/*for (int i = 0; i < N/2; i++) {
				for (int j = 0; j < 2; j++) {
					System.out.print(dp[i][j]+" ");
				}
				System.out.print("\n");
			}*/
			System.out.println(dp[N/2-1][1]);
		}
		else {
			dp = new long[N/2][3];
			for (int i = 0; i < N/2; i++) {
				for (int j = 0; j < 3; j++) {
					if (j==0&&i==0) dp[i][j] = dp[i][j] = arr[0];
					else if (j==0) {
						dp[i][j] = dp[i-1][j]+arr[i*2];
					}
					else if (i==0){
						dp[i][j] = Math.max(dp[i][j-1],arr[i*2+j]);
					}else if (i>0) {
						dp[i][j] = dp[i][j-1];
						long curNum = arr[i*2+j];
						dp[i][j] = Math.max(dp[i][j], dp[i-1][j]+curNum);
					}
				}
			}
			/*for (int i = 0; i < N/2; i++) {
				for (int j = 0; j < 3; j++) {
					System.out.print(dp[i][j]+" ");
				}
				System.out.print("\n");
			}*/
			System.out.println(dp[N/2-1][2]);
		}
	}
}