import java.io.*;
import java.math.BigInteger;
import java.util.*;

public class E implements Runnable {
	public static void main (String[] args) {new Thread(null, new E(), "_cf", 1 << 28).start();}

	int n, m;
	char[] str;
	int[][] occs, cost;
	int[] dp;
	
	public void run() {
		FastScanner fs = new FastScanner();
		PrintWriter out = new PrintWriter(System.out);
		System.err.println("");

		//where's my 420???? :(
		long tot = 0;
		for(int i = 0; i < 19999; i++) tot += i;
		System.err.println(tot);
		
		n = fs.nextInt(); m = fs.nextInt();
		byte[] str = fs.next().getBytes();
		int[] occs = new int[1<<m];
		for(int i = 0; i < n-1; i++) {
			int l1 = str[i] - 'a';
			int l2 = str[i+1] - 'a';
			occs[(1<<l1) | (1<<l2)]++;
			occs[(1<<l2) | (1<<l1)]++;
		}
		//cost[mask][v] = numPairs with v for some all bits on in mask
		int all = (1<<m)-1;
		cost = new int[m][1<<m];
		for(int i = 0; i < m; i++) {
			for(int mask = 1; mask < all; mask++) {
				if(((1<<i)&mask) > 0) continue;
				int lb = mask & (-mask);
				int trail = Integer.numberOfTrailingZeros(lb);
				int nmask = mask ^ lb;
				cost[i][mask] = cost[i][nmask]+occs[1<<i | 1<<trail];
			}
		}
		
		dp = new int[1<<m];
		for(int mask = dp.length-2; mask >= 0; mask--) {
			int addOn = 0;
			for(int nxt = 0; nxt < m; nxt++) {
				if(((1<<nxt)&mask) > 0) continue;
				addOn += cost[nxt][mask];
			}
			int res = oo;
			for(int nxt = 0; nxt < m; nxt++) {
				if(((1<<nxt)&mask) > 0) continue;
				int ret = addOn+dp[mask | (1<<nxt)];
				res = min(res, ret);
			}
			dp[mask] = res;
		}
		
		System.out.println(dp[0]>>1);
		
		out.close();
	}
	
	int oo = (int)1e9;
	int min(int a, int b) {
		if(a < b) return a;
		return b;
	}
	
	class FastScanner {
		public int BS = 1<<16;
		public char NC = (char)0;
		byte[] buf = new byte[BS];
		int bId = 0, size = 0;
		char c = NC;
		double num = 1;
		BufferedInputStream in;

		public FastScanner() {
			in = new BufferedInputStream(System.in, BS);
		}

		public FastScanner(String s) {
			try {
				in = new BufferedInputStream(new FileInputStream(new File(s)), BS);
			}
			catch (Exception e) {
				in = new BufferedInputStream(System.in, BS);
			}
		}

		public char nextChar(){
			while(bId==size) {
				try {
					size = in.read(buf);
				}catch(Exception e) {
					return NC;
				}                
				if(size==-1)return NC;
				bId=0;
			}
			return (char)buf[bId++];
		}

		public int nextInt() {
			return (int)nextLong();
		}

		public long nextLong() {
			num=1;
			boolean neg = false;
			if(c==NC)c=nextChar();
			for(;(c<'0' || c>'9'); c = nextChar()) {
				if(c=='-')neg=true;
			}
			long res = 0;
			for(; c>='0' && c <='9'; c=nextChar()) {
				res = (res<<3)+(res<<1)+c-'0';
				num*=10;
			}
			return neg?-res:res;
		}

		public double nextDouble() {
			double cur = nextLong();
			return c!='.' ? cur:cur+nextLong()/num;
		}

		public String next() {
			StringBuilder res = new StringBuilder();
			while(c<=32)c=nextChar();
			while(c>32) {
				res.append(c);
				c=nextChar();
			}
			return res.toString();
		}

		public String nextLine() {
			StringBuilder res = new StringBuilder();
			while(c<=32)c=nextChar();
			while(c!='\n') {
				res.append(c);
				c=nextChar();
			}
			return res.toString();
		}

		public boolean hasNext() {
			if(c>32)return true;
			while(true) {
				c=nextChar();
				if(c==NC)return false;
				else if(c>32)return true;
			}
		}
		
		public int[] nextIntArray(int n) {
			int[] res = new int[n];
			for(int i = 0; i < n; i++) res[i] = nextInt();
			return res;
		}
		
	}

}