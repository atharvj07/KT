import java.util.Scanner;

//Make KND So Fat
public class Main{

	void run(){
		Scanner sc = new Scanner(System.in);
		while(sc.hasNext()){
			int S = sc.nextInt(), D = sc.nextInt(), M = sc.nextInt();
			int[][] buy = new int[S][M+1];
			for(int i=0;i<S;i++){
				int k = sc.nextInt();
				int[] w = new int[k], p = new int[k];
				for(int j=0;j<k;j++){
					w[j] = sc.nextInt();
					p[j] = sc.nextInt();
				}
				int[][] dp = new int[k][M+1];
				for(int u=0;u<k;u++)for(int j=0;j<=M;j++){
					if(u>0)dp[u][j] = dp[u-1][j];
					if(p[u]<=j)dp[u][j] = Math.max(dp[u][j], w[u] + (u>0?dp[u-1][j-p[u]]:0));
				}
				for(int j=0;j<=M;j++)buy[i][j] = dp[k-1][j];
			}
			int[] f = new int[D+1];
			for(int i=0;i<D;i++)f[i]=sc.nextInt();
			int[][] dp = new int[D][M+1];
			for(int i=0;i<D;i++)for(int j=0;j<=M;j++){
				if(i>0)dp[i][j] = dp[i-1][j];
				int s = f[i];
				for(int u=0;u<=j;u++)dp[i][j] = Math.max(dp[i][j], buy[s][u] + (i>0?dp[i-1][j-u]:0));
			}
			int res = -1, m = -1;
			for(int i=0;i<=M;i++)if(res<dp[D-1][i]){
				res = dp[D-1][i];
				m = i;
			}
			System.out.println(res+" "+m);
		}
	}
	
	public static void main(String[] args) {
		new Main().run();
	}
}