import java.io.*;
import java.util.*;

public class E implements Runnable{
	public static void main (String[] args) {new Thread(null, new E(), "_cf", 1 << 26).start();}

	int n, k, log;
	int[][] adj;
	int[][] lift;
	
	public void run() {
		FastScanner fs = new FastScanner();
		PrintWriter out = new PrintWriter(System.out);
		System.err.println("Go!");

		n = fs.nextInt();
		log = Integer.numberOfTrailingZeros(Integer.highestOneBit(n));
		k = fs.nextInt();
		int[] size = new int[n];
		int[] us = new int[n - 1], vs = new int[n - 1];
		for(int i = 0; i < n - 1; i++) {
			int u = fs.nextInt() - 1;
			int v = fs.nextInt() - 1;
			us[i] = u; vs[i] = v;
			size[u]++; size[v]++;
		}
		adj = new int[n][];
		for(int i = 0; i < n; i++) adj[i] = new int[size[i]];
		for(int i = 0; i < n - 1; i++) {
			int u = us[i], v = vs[i]; 
			adj[u][--size[u]] = v;
			adj[v][--size[v]] = u;
		}
		lift = new int[log][n];
		for(int i = 0; i < log; i++)
			Arrays.fill(lift[i], -1);
		
		dfs(n - 1, -1);
		for(int p = 1; p < log; p++) {
			for(int i = 0; i < n; i++) {
				int up = lift[p - 1][i];
				if(up == -1) continue;
				lift[p][i] = lift[p - 1][up];
			}
		}
		
//		us = null; vs = null;
		Arrays.fill(size, 0);
		size[n - 1] = 1;
		int total = 1;
		
		for(int find = n - 2; find >= 0; find--) {
			if(size[find] == 1) continue;
			int dist = 0, u = find;
			for(int p = log - 1; p >= 0; p--) {
				if(lift[p][u] == -1) continue;
				if(size[lift[p][u]] == 1) continue;
				dist += 1 << p;
				u = lift[p][u];
			}
			dist++;
			if(dist + total <= n - k) {
				total += dist;
				u = find;
				while(!(size[u] == 1)) {
					size[u] = 1;
					u = lift[0][u];
				}
			}
		}
		
		StringBuilder sb = new StringBuilder();
		for(int i = 0; i < n; i++) {
			if(size[i] != 1) sb.append((i+1) + " ");
		}
		out.println(sb);
		out.close();
	}
	
	void dfs(int u, int p) {
		int[] queue = new int[n];
		int tail = 1;
		queue[0] = u;
		for(int i = 0; i < n; i++) {
			u = queue[i];
			for(int j = 0; j < adj[u].length; j++) {
				int v = adj[u][j];
				if(v == lift[0][u]) continue;
				lift[0][v] = u;
				queue[tail++] = v;
			}
		}
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

		public FastScanner(String s) throws FileNotFoundException {
			in = new BufferedInputStream(new FileInputStream(new File(s)), BS);
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