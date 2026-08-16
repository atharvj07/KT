import java.util.*;
import java.lang.*;
import java.math.*;
import java.io.*;
import static java.lang.Math.*;
import static java.util.Arrays.*;
import static java.util.Collections.*;

public class Main{
	Scanner sc=new Scanner(System.in);

	int INF=1<<28;
	double EPS=1e-12;

	int n;
	int[] xs, ys;

	void run(){
		n=sc.nextInt();
		xs=new int[n];
		ys=new int[n];
		for(int i=0; i<n; i++){
			xs[i]=sc.nextInt();
			ys[i]=sc.nextInt();
		}
		solve();
	}

	void solve(){
		int[][] dp1=new int[n+1][n+1];
		int[][] dp2=new int[n+1][n+1];
		int[][] dp=new int[n+1][n+1];
		int[][] k=new int[n+1][n+1];
		for(int i=0; i<=n; i++){
			fill(dp1[i], INF);
			fill(dp2[i], INF);
			fill(dp[i], INF);
			dp1[i][i]=0;
			dp2[i][i]=0;
			if(i<n){
				dp1[i][i+1]=0;
				dp2[i][i+1]=0;
			}
			k[i][i]=i;
		}
		// dp1テ」ツ?ッテッツシツ古ァツクツヲテ」ツつ津・ツ青ォテ」ツ?セテ」ツ?ェテ」ツ??
		if(false)
			for(int w=1; w<=n; w++){
				for(int i=0; i+w<=n; i++){
					int j=i+w;
					for(int s=i; s<=j; s++){
						dp1[i][j]=min(dp1[i][j], dp1[i][s]+dp2[s][j]+xs[j-1]
								-xs[i]);
						dp2[i][j]=min(dp2[i][j], dp1[i][s]+dp2[s][j]+ys[i]
								-ys[j-1]);
						dp[i][j]=min(dp[i][j], dp1[i][s]+dp2[s][j]+xs[j-1]
								-xs[i]+ys[i]-ys[j-1]);
					}
				}
			}

		for(int w=1; w<=n; w++){
			for(int i=0, j=w; j<=n; i++, j++){
				int min=INF;
				for(int r=k[i][j-1]; r<=k[i+1][j]; r++){
					int v=dp1[i][r]+dp2[r][j];
					if(v<min){
						min=v;
						k[i][j]=r;
						dp1[i][j]=v+xs[j-1]-xs[i];
						dp2[i][j]=v+ys[i]-ys[j-1];
						dp[i][j]=v+xs[j-1]-xs[i]+ys[i]-ys[j-1];
					}
				}
			}
		}
		for(int i=0; i<=n; i++){
//			debug(i, dp[i]);
		}
		println(dp[0][n]+"");
	}

	void debug(Object... os){
		System.err.println(Arrays.deepToString(os));
	}

	void print(String s){
		System.out.print(s);
	}

	void println(String s){
		System.out.println(s);
	}

	public static void main(String[] args){
		new Main().run();
	}
}