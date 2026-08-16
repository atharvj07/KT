import java.util.*;
import java.lang.*;
import java.math.*;
import java.io.*;
import static java.util.Collections.*;
import static java.util.Arrays.*;
import static java.lang.Math.*;

// Divide the Water
// 2012/12/15
public class Main{
	Scanner sc=new Scanner(System.in);

	int INF=1<<28;

	int n;
	int[] a;

	void run(){
		n=sc.nextInt();
		a=new int[n];
		for(int i=0; i<n; i++){
			a[i]=sc.nextInt();
		}
		solve();
	}

	int[] sum;
	int[][] memo;

	void solve(){
		sum=new int[n+1];
		for(int i=0; i<n; i++){
			sum[i+1]=sum[i]+a[i];
		}
		memo=new int[n+1][n+1];
		for(int i=0; i<=n; i++){
			fill(memo[i], -1);
		}
		println(rec(0, n)+"");
	}

	int rec(int i, int j){
		if(memo[i][j]>=0){
			return memo[i][j];
		}
		if(j-i<=1){
			return memo[i][j]=j-i;
		}
		int res=INF;
		for(int k=i+1; k<j; k++){
			res=min(res, rec(i, k)+rec(k, j));
			if(sum[k]-sum[i]==sum[j]-sum[k]&&rec(i, k)==1&&rec(k, j)==1){
				res=min(res, 1);
			}
		}
		return memo[i][j]=res;
	}

	void println(String s){
		System.out.println(s);
	}

	public static void main(String[] args){
		new Main().run();
	}
}