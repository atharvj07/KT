import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Scanner;

public class Main {
	Scanner sc = new Scanner(System.in);
	public static void main(String[] args){
		new Main();
	}
	public Main(){
		new AOJ1611().doIt();
	}
	class AOJ1611{
		void doIt(){
			while(true) {
				int n = sc.nextInt();
				if(n == 0)break;
				int w[] = new int [n];
				for(int i = 0;i < n;i++)w[i] = sc.nextInt();
				int dp[][] = new int[n][n];
				for(int W = 2;W < n+1;W++) {
					for(int i = 0;i < n;i++) {
						int j = i+W-1;
						if(j >= n) break;
						if(dp[i+1][j-1] == W-2 && Math.abs(w[i] - w[j]) <= 1) dp[i][j] = W;
						for(int k = i;k < j;k++) {
							dp[i][j] = Math.max(dp[i][j], dp[i][k] + dp[k+1][j]);
						}
					}
				}
				
//				for(int i = 0;i < n;i++) {
//					for(int j = 0;j < n;j++) {
//						System.out.print(dp[i][j]+" ");
//					}
//					System.out.println();
//				}
				System.out.println(dp[0][n-1]);
			}
		}
	}
}

