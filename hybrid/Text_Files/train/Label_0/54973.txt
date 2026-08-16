
import java.io.*;
import java.math.BigInteger;
import java.util.*;
import java.util.Stack;

public class ROUGH{
	public static class FastReader {
		BufferedReader br;
		StringTokenizer root;
		
 
		public FastReader() {
			br = new BufferedReader(new InputStreamReader(System.in));
		}
 
		String next() {
			while (root == null || !root.hasMoreTokens()) {
				try {
					root = new StringTokenizer(br.readLine());
				} catch (Exception r) {
					r.printStackTrace();
				}
			}
			return root.nextToken();
		}
 
		int nextInt() {
			return Integer.parseInt(next());
		}
 
		double nextDouble() {
			return Double.parseDouble(next());
		}
 
		long nextLong() {
			return Long.parseLong(next());
		}
 
		String nextLine() {
			String str = "";
			try {
				str = br.readLine();
			} catch (Exception r) {
				r.printStackTrace();
			}
			return str;
		}
	}
	
	public static PrintWriter out = new PrintWriter (new BufferedOutputStream(System.out));
	static int mod = (int) (1e9+7);
	static long cf = 998244353;
    static long MAX = (long)(1e12),n,m;
    public static List<Integer>[] edges;
    static int freq[];
	static int dp[][];
	static int primes[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
				41, 43, 47, 53, 59, 61, 67};
	public static void main(String[] args) {
		FastReader sc = new FastReader();
		n = sc.nextInt();
		freq = new int[71];
		for(int i = 0; i < n; i++)
			freq[sc.nextInt()]++;
		dp = new int[71][(1<<19)+1];
		for(int i=0;i<dp.length;++i) Arrays.fill(dp[i], -1);
		out.println(f(0, 1)-1);
	    out.close();
	}
	static int f(int mask, int k) {
		if(k == 71) return mask == 0 ? 1 : 0;
		if(dp[k][mask] != -1) return dp[k][mask];
		int tot = freq[k];
		if(tot == 0) return f(mask, k+1);
		int ways = pow(2, tot-1);
		return dp[k][mask] =  (int)((((long)ways*f(mask, k+1))%mod + (long)ways*f(get(mask, k), k+1)%mod)%mod);
	}
	
	static int pow(int a, int b) { 
         if(b == 0) return 1;
		long p = pow(a,b/2)%mod;
		p = (p*p)%mod;
		if((b&1) == 1) p = (a*p)%mod;
		return (int) p;
	}
 
	static int get(int mask, int k) {
		int num = k;
		int newMask = mask;
		while(num != 1) {
			for(int i = 0; i < primes.length; i++) {
				if(num % primes[i] == 0) {
					num/=primes[i];
					newMask = newMask ^ (1 << i);
				}
			}
		}
		return newMask;
		
	}

}