import java.util.*;
import java.lang.*;
import java.math.*;
import java.io.*;
import static java.lang.Math.*;
import static java.util.Arrays.*;
import static java.util.Collections.*;

// Hotel
// 2013/09/10
public class Main{
	Scanner sc=new Scanner(System.in);

	long B=1000000000L;

	int m, n;
	int[][] a;

	void run(){
		m=sc.nextInt();
		n=sc.nextInt();
		a=new int[n][m];
		for(int i=0; i<m; i++){
			for(int j=0; j<n; j++){
				a[j][i]=sc.nextInt();
			}
		}
		solve();
	}

	long[][] dp;

	void solve(){
		dp=new long[n][m];
		for(int i=0; i<n; i++){
			fill(dp[i], -1);
		}
		long min=Long.MAX_VALUE;
		for(int i=0; i<m; i++){
			min=min(min, rec(i, 0));
		}
		println(min/B+" "+min%B);
		int now=-1;
		for(int j=0; j<n; j++){
			int next=0;
			for(int i=0; i<m; i++){
				if(rec(i, j)+(i==now?0:1)<rec(next, j)+(next==now?0:1)){
					next=i;
				}
			}
			now=next;
			println(next+1+"");
		}
	}

	long rec(int i, int j){
		if(dp[j][i]>=0){
			return dp[j][i];
		}
		long min;
		if(j<n-1){
			min=Long.MAX_VALUE;
			for(int k=0; k<m; k++){
				min=min(min, rec(k, j+1)+(k==i?0:1));
			}
		}else{
			min=0;
		}
		return dp[j][i]=min+a[j][i]*B;
	}

	void println(String s){
		System.out.println(s);
	}

	public static void main(String[] args){
		new Main().run();
	}
}