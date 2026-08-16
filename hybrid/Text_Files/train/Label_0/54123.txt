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
	int[] s;
	P[][] ps;

	int mask=(1>>29)-1;

	void run(){
		for(;;){
			n=sc.nextInt();
			if(n==0){
				break;
			}
			s=new int[n];
			ps=new P[n][];
			for(int j=0; j<n; j++){
				s[j]=sc.nextInt();
				ps[j]=new P[s[j]];
				for(int i=0; i<s[j]; i++){
					int x=sc.nextInt();
					int y=sc.nextInt();;
					ps[j][i]=new P(x, y);
				}
			}
			solve();
		}
	}

	void solve(){
		int[][] graph=new int[n][n];
		for(int j=0; j<n; j++){
			for(int i=0; i<n; i++){
				graph[j][i]=cross(i, j)?1:0;
			}
		}

		int[] N=new int[n];
		for(int j=0; j<n; j++){
			for(int i=0; i<n; i++){
				if(graph[j][i]==1){
					N[j]|=1<<i;
				}
			}
		}

		int[] dp=new int[1<<n];
		dp[0]=1;
		for(int sup=1; sup<1<<n; sup++){
			int i=Integer.numberOfTrailingZeros(sup);
			dp[sup]=(dp[sup^(1<<i)]+dp[sup&~N[i]])&mask;
		}

		int left=0, right=n;
		for(; left+1<right;){
			int mid=(left+right)/2;
			if(kCover(mid, dp)){
				right=mid;
			}else{
				left=mid;
			}
		}
		println(right+"");
	}

	long powMod(long x, int k){
		long res=1;
		for(; k!=0; k>>=1){
			if((k&1)==1){
				res=(res*x)&mask;
			}
			x=(x*x)&mask;
		}
		return res&mask;
	}

	boolean kCover(int k, int[] a){
		long ans=0;
		for(int i=0; i<1<<n; i++){
			if(Integer.bitCount((1<<n)^i)%2==0){
				ans=(ans+powMod(a[i], k))&mask;
			}else{
				ans=(ans-powMod(a[i], k))&mask;
			}
		}
		return ans!=0;
	}

	boolean cross(int a, int b){
		for(int i=0; i<s[a]-1; i++){
			for(int j=0; j<s[b]-1; j++){
				if(crsSS(ps[a][i], ps[a][i+1], ps[b][j], ps[b][j+1])){
					return true;
				}
			}
		}
		return false;
	}

	boolean crsSS(P p1, P p2, P q1, P q2){
		if(max(p1.x, p2.x)+EPS<min(q1.x, q2.x))
			return false;
		if(max(q1.x, q2.x)+EPS<min(p1.x, p2.x))
			return false;
		if(max(p1.y, p2.y)+EPS<min(q1.y, q2.y))
			return false;
		if(max(q1.y, q2.y)+EPS<min(p1.y, p2.y))
			return false;
		return signum(p2.sub(p1).det(q1.sub(p1)))
				*signum(p2.sub(p1).det(q2.sub(p1)))<EPS
				&&signum(q2.sub(q1).det(p1.sub(q1)))
						*signum(q2.sub(q1).det(p2.sub(q1)))<EPS;
	}

	class P{
		double x, y;

		P(){
			this(0, 0);
		}

		P(double x, double y){
			this.x=x;
			this.y=y;
		}

		P add(P p){
			return new P(x+p.x, y+p.y);
		}

		P sub(P p){
			return new P(x-p.x, y-p.y);
		}

		P mul(double m){
			return new P(x*m, y*m);
		}

		P div(double d){
			return new P(x/d, y/d);
		}

		double abs(){
			return sqrt(abs2());
		}

		double abs2(){
			return x*x+y*y;
		}

		double arg(){
			return atan2(y, x);
		}

		double dot(P p){
			return x*p.x+y*p.y;
		}

		double det(P p){
			return x*p.y-y*p.x;
		}

		double ang(P p){
			return atan2(det(p), dot(p));
		}

		P rot(double d){
			return new P(cos(d)*x-sin(d)*y, sin(d)*x+cos(d)*y);
		}
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
		// System.setOut(new PrintStream(new BufferedOutputStream(System.out)));
		new Main().run();
	}
}