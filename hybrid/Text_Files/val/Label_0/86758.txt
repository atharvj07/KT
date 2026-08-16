import java.util.*;
import java.lang.*;
import java.math.*;
import java.io.*;
import static java.lang.Math.*;
import static java.util.Arrays.*;
import static java.util.Collections.*;

// Round Table
// 2012/12/15
public class Main{
	BufferedReader br=new BufferedReader(new InputStreamReader(System.in));

	int INF=1<<28;
	double EPS=1e-12;

	int n, m;
	int[] a;

	void run(){
		try{
			String[] ss=br.readLine().split(" ");
			n=Integer.parseInt(ss[0]);
			m=Integer.parseInt(ss[1]);
			ss=br.readLine().split(" ");
			a=new int[n];
			for(int i=0; i<n; i++){
				a[i]=Integer.parseInt(ss[i]);
			}
			solve();
		}catch(IOException e){}
	}

	int logM;
	int[] sum;
	int[][] dp;

	void solve(){
		logM=31-Integer.numberOfLeadingZeros(m)+1;
		dp=new int[logM][3*n];
		sum=new int[3*n];
		for(int i=0; i<3*n-1; i++){
			sum[i+1]=sum[i]+a[i%n];
		}
		int left=0, right=(int)1e8;
		for(; right-left>1;){
			int mid=(left+right)/2;
			if(check(mid)){
				right=mid;
			}else{
				left=mid;
			}
		}
		println(right+"");
	}

	boolean check(int t){
		if(t==0){
			return false;
		}
		for(int i=0; i<logM; i++){
			fill(dp[i], -1);
		}
		for(int i=0; i<3*n; i++){
			int index=binarySearch(sum, sum[i]+t);
			if(index<0){
				index=-index-1;
				index--;
			}
			dp[0][i]=index;
		}
		for(int j=1; j<logM; j++){
			for(int i=0; i<3*n; i++){
				dp[j][i]=dp[j-1][dp[j-1][i]];
			}
		}
		for(int i=0; i<n; i++){
			int now=i;
			for(int b=0; b<logM; b++){
				if((m>>b&1)==1){
					now=dp[b][now];
				}
			}
			if(now-i>=n){
				return true;
			}
		}
		return false;
	}

	void println(String s){
		System.out.println(s);
	}

	public static void main(String[] args){
		new Main().run();
	}
}