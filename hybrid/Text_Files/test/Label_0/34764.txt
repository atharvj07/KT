import java.util.Arrays;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		try(Scanner sc = new Scanner(System.in)){
			while(sc.hasNext()) {
				int n=sc.nextInt();
				int m=sc.nextInt();
				if(n+m==0) break;
				int[] s=new int[n];
				int[] d=new int[m];
				for(int i=0; i<n; i++) {
					s[i]=sc.nextInt();
				}
				for(int i=0; i<m; i++) {
					d[i]=sc.nextInt();
				}
				Arrays.sort(d);
//				for(int i=0; i<m; i++) {
//					System.out.print(d[i]);
//				}
//				System.out.println();
				int INF=100000000;
				int[][] dp=new int[1<<n][m+1];//dp[使用布団][日にち]
				for(int i=0; i<(1<<n); i++) {
					for(int j=0; j<=m; j++) {
						dp[i][j]=INF;
					}
				}
				dp[0][0]=0;
				
				int[] sum=new int[1<<n];//使用布団の供給合計
				for(int i=0; i<(1<<n); i++) {
					sum[i]=0;
					for(int j=0; j<n; j++) {
						if((1&(i>>j))==1)	sum[i]+=s[j];
					}
				}
				
				for(int i=0; i<m; i++) {
					for(int j=0; j<(1<<n); j++) {//i日にjの布団が使われた
						dp[j][i+1]=Math.min(dp[j][i+1], dp[j][i]+Math.abs(sum[j]-d[i]));
						for(int k=0; k<n; k++) {
							if((1&(j>>k))==1) continue;
							int nextj=j|(1<<k);
							dp[nextj][i]=Math.min(dp[nextj][i], dp[j][i]);
						}
					}
				}
				int ans=INF;
				for(int i=0; i<(1<<n); i++) {
					ans=Math.min(ans, dp[i][m]);
				}
				System.out.println(ans);

			}
		}
	}
}
