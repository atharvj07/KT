import java.util.*;
import java.math.*;

// **** A. 2048 Game ****

public class A {
	static char [] in = new char [1000005];
	public static void main (String [] arg) throws Throwable {
		int q = nextInt();
		for (int ii = 0; ii<q; ++ii) {
			int total = 0;
			int n = nextInt();
			for (int i = 0; i<n; ++i) {
				int s = nextInt();
				if (s <= 2048) total += s;
			}
			System.out.println(total >= 2048 ? "YES" :"NO");
		}	
	}

	
	
	
	
	
	
	
	
	
	
	
	
	
	/************** HELPER CLASSES ***************/
    //static class HS extends HashSet<Integer>{public HS(){super();}public HS(int a){super(a);}};
	//static class AL extends ArrayList<Integer>{public AL(){super();}public AL(int a){super (a);}};
	static class Pair implements Comparable<Pair> {
		int i,j;long L; public Pair(int xx, int yy, long LL){i=xx;j=yy;L=LL;} 
		public int compareTo(Pair p) { return (this.L < p.L) ? -1 : (this.L == p.L) ? this.i - p.i : 1;}
	}
	/************** FAST IO CODE FOLLOWS *****************/
	public static long nextLong() throws Throwable {
		long i = System.in.read();boolean neg = false;while (i < 33) i = System.in.read();if (i == 45) {neg=true;i=48;}i = i - 48;
		int j = System.in.read();while (j > 32) {i*=10;i+=j-48;j = System.in.read();}return (neg) ? -i : i;
	}
	public static int nextInt() throws Throwable {return (int)nextLong();}
	public static String next() throws Throwable {
		int i = 0; while (i < 33 && i != -1) i = System.in.read(); int cptr = 0; while (i >= 33) { in[cptr++] = (char)i; i = System.in.read();}
		return new String(in, 0,cptr);
	}
	/**** LIBRARIES ****/
	public static long gcdL(long a, long b) {while (b != 0) {long tmp = b;b = (a % b);a = tmp;}return a;}
	public static int gcd(int a, int b) {while (b != 0) {int tmp = b;b = (a % b);a = tmp;}return a;}
	public static int[] sieve(int LIM) {
		int i,count = 0;
		boolean [] b = new boolean [LIM];
		for (i = 2;i<LIM; ++i) if (!b[i]) {count++; for (int j = i<<1; j<LIM; j+=i) b[j] = true;}
		int [] primes = new int[count];
		for (i = 2,count=0;i<LIM;++i) if (!b[i]) primes[count++] = i;
		return primes;
	}
	public static int[] numPrimeFactors(int LIM) {
		int i,count = 0;
		int [] b = new int [LIM];
		for (i = 2;i<LIM; ++i) if (b[i] == 0) {count++; for (int j = i; j<LIM; j+=i) b[j]++;}
		return b;
	}
	public static StringBuilder stringFromArray(int [] a) {
		StringBuilder b = new StringBuilder(9*a.length);
		for (int i = 0; i<a.length; ++i) {
			if (i != 0) b = b.append(' ');
			b = b.append(a[i]);
		}
		return b;
	}
	public static long modPow (long a, long n, long MOD) { long S = 1; for (;n > 0; n>>=1, a=(a*a)%MOD) if ((n & 1) != 0) S = (a*S) % MOD; return S;}
}

/* Full Problem Text:
  
You are playing a variation of game 2048.
Initially you have a multiset s of n integers.
Every integer in this multiset is a power of two.
You may perform any number (possibly, zero) operations with this multiset.
During each operation you choose two equal integers from s, remove them from s and insert the number equal to their sum into s.
For example, if s = \{1, 2, 1, 1, 4, 2, 2\} and you choose integers 2 and 2, then the multiset becomes \{1, 1, 1, 4, 4, 2\}.
You win if the number 2048 belongs to your multiset.
For example, if s = \{1024, 512, 512, 4\} you can win as follows: choose 512 and 512, your multiset turns into \{1024, 1024, 4\}.
Then choose 1024 and 1024, your multiset turns into \{2048, 4\} and you win.
You have to determine if you can win this game.
You have to answer q independent queries.

 */