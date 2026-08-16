import java.util.Arrays;
import java.util.Scanner;

//Gather on the Clock
public class Main{

	int n;
	int[] a;
	int[][] dp;
	
	int get(int i, int j){
		if(i==j)return 0;
		if(dp[i][j]!=-1)return dp[i][j];
		if((i+1)%n==j)return dp[i][j]=Math.abs(a[i]-a[j]);
		int res = get(i, (j-1+n)%n) + Math.abs(a[i]-a[j]);
		int k = (i+1)%n;
		while(k!=j){
			res = Math.max(res, get(i, k)+get(k, j));
			k = (k+1)%n;
		}
		return dp[i][j] = res;
	}
	
	void run(){
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		while(T--!=0){
			n = sc.nextInt();
			a = new int[n];
			for(int i=0;i<n;i++)a[i]=sc.nextInt();
			dp = new int[n][n];
			for(int[]d:dp)Arrays.fill(d, -1);
			int res = 0;
			for(int i=0;i<n;i++)res=Math.max(res, get(i, (i-1+n)%n));
			System.out.println(res);
		}
	}
	
	public static void main(String[] args) {
		new Main().run();
	}
}