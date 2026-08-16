import java.util.Arrays;
import java.util.Scanner;

//Beautiful Currency
public class Main{

	void run(){
		Scanner sc = new Scanner(System.in);
		int N = 200000;
		int n = sc.nextInt();
		int[] a = new int[n];
		for(int i=0;i<n;i++)a[i] = sc.nextInt();
		double[][] dp = new double[n][N];
		for(int i=0;i<n;i++)Arrays.fill(dp[i], 1<<29);
		for(int i=1;i<N;i++)dp[0][i] = Math.abs(a[0]-i)*1.0/a[0];
		for(int i=0;i<n-1;i++){
			for(int j=1;j<N;j++){
				for(int k=j;k<N;k+=j){
					dp[i+1][k] = Math.min(dp[i+1][k], Math.max(dp[i][j], Math.abs(a[i+1]-k)*1.0/a[i+1]));
				}
			}
		}
		double min = 1<<29;
		for(int j=1;j<N;j++){
			min = Math.min(min, dp[n-1][j]);
		}
		System.out.printf("%.9f\n", min);
	}
	
	public static void main(String[] args) {
		new Main().run();
	}
}