import java.util.*;
import java.lang.*;
import java.math.*;
import java.io.*;
import static java.lang.Math.*;
import static java.util.Arrays.*;
import static java.util.Collections.*;

// Complex Integer Solutions
// 2012/12/25
public class Main{
	Scanner sc=new Scanner(System.in);

	int n;
	int[] a;

	void run(){
		n=sc.nextInt();
		a=new int[n+1];
		for(int i=n; i>=0; i--){
			a[i]=sc.nextInt();
		}
		solve();
	}

	void solve(){
		int p1=nextPrime(1500), p2=nextPrime(p1);
		int p=p1*p2;

		ArrayList<P> list1=new ArrayList<P>(), list2=new ArrayList<P>();

		for(int x=0; x<p1; x++){
			for(int y=0; y<p1; y++){
				P eval=evalMod(x, y, p1);
				if(eval.x==0&eval.y==0){
					list1.add(new P(x, y));
				}
			}
		}
		for(int x=0; x<p2; x++){
			for(int y=0; y<p2; y++){
				P eval=evalMod(x, y, p2);
				if(eval.x==0&eval.y==0){
					list2.add(new P(x, y));
				}
			}
		}

		// debug("list1", list1);
		// debug("list2", list2);

		TreeSet<P> set=new TreeSet<P>();

		for(P z1 : list1){
			for(P z2 : list2){
				// z = z1 % p1
				// z = z2 % p2
				long x=linear(new long[]{1, 1}, new long[]{z1.x, z2.x},
						new long[]{p1, p2});
				long y=linear(new long[]{1, 1}, new long[]{z1.y, z2.y},
						new long[]{p1, p2});
				// debug(z);
				if(x>abs(x-p)){
					x=x-p;
				}
				if(y>abs(y-p)){
					y=y-p;
				}
				P eval=eval(x, y);
				if(eval.x==0&&eval.y==0){
					set.add(new P(x,y));
				}
				/*
				for(int i=0; i<=1; i++){
					for(int j=0; j<=1; j++){
						P zz=new P(z.x-i*p1*p2, z.y-j*p1*p2);
						// if (zz.x == -1)
						// debug(zz);
						if(eval(zz)){
							set.add(zz);
						}
					}
				}
				*/
			}
		}

		P[] ps=set.toArray(new P[0]);
		StringBuilder sb=new StringBuilder();
		sb.append(ps.length).append('\n');
		for(int i=0; i<ps.length; i++){
			long x=ps[i].x, y=ps[i].y;
			String s=x+"+"+y+"i";
			s=s.replaceAll("[\\+|-]0i", "").replaceAll("\\+-", "-")
					.replaceAll("\\+1i", "+i").replaceAll("-1i", "-i")
					.replaceAll("^0", "").replaceAll("^\\+", "");
			if(s.length()==0){
				s="0";
			}
			sb.append(s);
			if(i==ps.length-1){}else{
				sb.append(' ');
			}
		}
		println(sb.toString());
	}

	long linear(long[] A, long[] B, long[] M){
		long x=0, m=1;
		for(int i=0; i<A.length; i++){
			long a=A[i]*m, b=B[i]-A[i]*x, d=gcd(M[i], a);
			if(b%d!=0)
				return -1;
			long t=b/d*invMod(a/d, M[i]/d)%(M[i]/d);
			x=x+m*t;
			m*=M[i]/d;
		}
		return (x%m+m)%m;
	}

	long gcd(long a, long b){
		return a==0?b:gcd(b%a, a);
	}

	long invMod(long x, long mod){
		return powMod(x, mod-2, mod);
	}

	long powMod(long x, long k, long mod){
		if(k==0){
			return 1;
		}
		if((k&1)==0){
			return powMod(x*x%mod, k>>>1, mod);
		}
		return x*powMod(x, k-1, mod)%mod;
	}

	P evalMod(long x, long y, int mod){
		P eval=new P(0, 0);
		for(int i=0; i<=n; i++){
			mul(eval, x, y);
			add(eval, a[i], 0);
			eval.x%=mod;
			eval.y%=mod;
		}
		return eval;
	}

	P eval(long x, long y){
		P eval=new P(0, 0);
		for(int i=0; i<=n; i++){
			mul(eval, x, y);
			add(eval, a[i], 0);
		}
		return eval;
	}

	void add(P p, long x, long y){
		p.x+=x;
		p.y+=y;
	}

	void mul(P p, long x, long y){
		long nx=p.x*x-y*p.y;
		long ny=x*p.y+y*p.x;
		p.x=nx;
		p.y=ny;
	}

	class P implements Comparable<P>{
		long x, y;

		P(long x, long y){
			this.x=x;
			this.y=y;
		}

		P add(P p){
			return new P(x+p.x, y+p.y);
		}

		P mul(P p){
			return new P(x*p.x-y*p.y, x*p.y+p.x*y);
		}

		public boolean equals(P p){
			return x==p.x&&y==p.y;
		}

		@Override
		public String toString(){
			return "("+x+", "+y+")";
		}

		public int compareTo(P p){
			return Long.signum(x-p.x)*2+Long.signum(y-p.y);
		}
	}

	int nextPrime(int n){
		for(n++; !BigInteger.valueOf(n).isProbablePrime(200); n++);
		return n;
	}

	void println(String s){
		System.out.println(s);
	}

	void print(String s){
		System.out.print(s);
	}

	void debug(Object... os){
		System.err.println(deepToString(os));
	}

	public static void main(String[] args){
		new Main().run();
	}
}