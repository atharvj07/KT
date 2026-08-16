import java.util.*;
import java.lang.*;
import java.math.*;
import java.io.*;
import static java.lang.Math.*;
import static java.util.Arrays.*;
import static java.util.Collections.*;

// Sun and Moon
// 2013/03/23
public class Main{
	Scanner sc=new Scanner(System.in);

	long INF=1L<<60;

	int n;
	long[] as, bs;

	void run() throws Exception{
		n=sc.nextInt();
		as=new long[n];
		bs=new long[n];
		for(int i=0; i<n; i++){
			bs[i]=sc.nextLong();
			as[i]=sc.nextLong();
		}
		solve();
	}

	void solve() throws Exception{
		if(n==0){
			println("Yes 1");
			return;
		}
		int m=5;

		long[] ps=new long[m];
		ps[0]=BigInteger.valueOf((int)1e3).nextProbablePrime().longValue();
		for(int i=1; i<m; i++){
			ps[i]=BigInteger.valueOf(ps[i-1]+1).nextProbablePrime().longValue();
		}

		for(int x=1; x<=1000; x++){
			int mod1=(int)ps[0], mod2=(int)ps[1];
			if(f(x, mod1)==0&&df(x, mod1)==0&&f(x, mod2)==0&&df(x, mod2)==0){
				println("Yes "+x);
				return;
			}
		}

		long min=INF;
		long[] A=new long[m], B=new long[m];
		fill(A, 1);

		@SuppressWarnings("unchecked")
		ArrayList<Integer>[] list=new ArrayList[m];
		for(int i=0; i<m; i++){
			list[i]=candidate((int)ps[i]);
		}
		for(int x0 : list[0]){
			for(int x1 : list[1]){
				for(int x2 : list[2]){
					for(int x3 : list[3]){
						for(int x4 : list[4]){
							B[0]=x0;
							B[1]=x1;
							B[2]=x2;
							B[3]=x3;
							B[4]=x4;
							long res=linearCongruence(A, B, ps);
							if(res!=-1&&res>0){
								min=min(min, res);
							}
						}
					}
				}
			}
		}
		if(min<INF){
			println("Yes "+min);
		}else{
			println("No");
		}
	}

	ArrayList<Integer> candidate(int p){
		ArrayList<Integer> list=new ArrayList<Integer>();
		for(int i=0; i<p; i++){
			if(f(i, p)==0&&df(i, p)==0){
				list.add(i);
			}
		}
		return list;
	}

	long linearCongruence(long[] A, long[] B, long[] M){
		long x=0, m=1;
		for(int i=0; i<A.length; i++){
			long a=A[i]*m, b=B[i]-A[i]*x, d=gcd(M[i], a);
			if(b%d!=0)
				return -1;
			x+=m*(mulMod(b/d, invMod(a/d, M[i]/d), (M[i]/d)));
			m*=M[i]/d;
		}
		return x%m;
	}

	long powMod(long x, long k, int mod){
		long res=1;
		for(; k!=0; k>>>=1){
			if((k&1)==1){
				res=res*x%mod;
			}
			x=x*x%mod;
		}
		return res;
	}

	long gcd(long a, long b){
		return a==0?b:gcd(b%a, a);
	}

	long invMod(long a, long mod){
		return powMod(a, mod-2, mod);
	}

	long mulMod(long x, long y, long mod){
		long res=0;
		for(; y!=0; y>>>=1){
			if((y&1)==1){
				res=(res+x)%mod;
			}
			x=(x+x)%mod;
		}
		return res;
	}

	long powMod(long x, long k, long mod){
		long res=1;
		for(; k!=0; k>>>=1){
			if((k&1)==1){
				res=mulMod(res, x, mod);
			}
			x=mulMod(x, x, mod);
		}
		return res;
	}

	long f(long x, int mod){
		long val=0;
		for(int i=0; i<n; i++){
			val=(val+as[i]%mod*powMod(x, bs[i], mod)%mod)%mod;
		}
		return val;
	}

	long df(long x, int mod){
		long val=0;
		for(int i=0; i<n; i++){
			if(bs[i]>0){
				val=(val+bs[i]%mod*as[i]%mod*powMod(x, bs[i]-1, mod)%mod)%mod;
			}
		}
		return val;
	}

	void println(String s){
		System.out.println(s);
	}

	public static void main(String[] args) throws Exception{
		new Main().run();
	}
}