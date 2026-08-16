import java.io.ByteArrayInputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.InputMismatchException;

public class c {
	
	static class Solver {
		
		int N, dist[][], size[][], stsz[]; ArrayList<Integer> adj[];
		
		void distDFS(int vtx, int rt, int par, int dep) {
			dist[rt][vtx] = dep;
			for(int v : adj[vtx])
				if(v != par)
					distDFS(v, rt, vtx, dep + 1);
		}
		
		void sizeDFS(int v, int p) {
			stsz[v] = 1;
			for(int w : adj[v]) {
				if(w == p) continue;
				sizeDFS(w, v);
				stsz[v] += stsz[w];
				size[v][w] = stsz[w];
				size[w][v] = N - size[v][w];
			}
		}
		
		@SuppressWarnings("unchecked")
		void solve(FastScanner s, PrintWriter out) {
			Arrays.setAll(adj = new ArrayList[N = s.nextInt()], x -> new ArrayList<>());
			for(int i = 1, u, v; i < N; i++) {
				u = s.nextInt() - 1; v = s.nextInt() - 1;
				adj[u].add(v); adj[v].add(u);
			}
			
			dist = new int[N][N];
			for(int rt = 0; rt < N; rt++) distDFS(rt, rt, -1, 0);
			size = new int[N][N]; stsz = new int[N];
			sizeDFS(0, -1);
			
			memo = new long[N][N];
			for(long[] row : memo) Arrays.fill(row, -1);
			
			long mx = 0, p;
			for(int i = 0; i < N; i++)
				for(int j : adj[i])
					if(i < j) {
						p = size[i][j] * size[j][i] + dp(i, j);
						if(p > mx) mx = p;
					}
			out.println(mx);
			
		}
		
		long memo[][];
		
		// max mex assuming u to v has all [0, dist(u,v)]
		long dp(int u, int v) {
			if(u > v) u = v ^ u ^ (v = u);
			if(memo[u][v] != -1) return memo[u][v];
			long max = 0, poss, usz = 0, vsz = 0;
			for (int w : adj[u])
				if (dist[u][v] > dist[w][v]) {
					usz = size[w][u];
					break;
				}
			for(int w : adj[v])
				if(dist[v][u] > dist[w][u]) {
					vsz = size[w][v];
					break;
				}
			// try all edges out of u, if they're not in the direction of v
			for(int w : adj[u]) {
				if(dist[u][v] > dist[w][v]) continue;
				poss = size[u][w] * vsz + dp(w, v);
				if(poss > max) max = poss;
			}
			for(int w : adj[v]) {
				if(dist[v][u] > dist[w][u]) continue;
				poss = size[v][w] * usz + dp(w, u);
				if(poss > max) max = poss;
			}
			return memo[u][v] = max;
		}
		
	}
	
	public static void main(String[] args) {
		FastScanner s = new FastScanner(System.in);
		PrintWriter out = new PrintWriter(System.out);
		new Solver().solve(s, out);
		out.close(); s.close();
	}
	
	static class FastScanner {
		private InputStream stream;
		private byte[] buf = new byte[1 << 22];
		private int curChar;
		private int numChars;
		
		public FastScanner(InputStream stream) {
			this.stream = stream;
		}
		
		public FastScanner(File f) throws FileNotFoundException {
			this(new FileInputStream(f));
		}
		
		public FastScanner(String s) {
			this.stream = new ByteArrayInputStream(s.getBytes(StandardCharsets.UTF_8));
		}
		
		void close() {
			try {
				stream.close();
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
		
		int read() {
			if (numChars == -1)
				throw new InputMismatchException();
			if (curChar >= numChars) {
				curChar = 0;
				try {
					numChars = stream.read(buf);
				} catch (IOException e) {
					throw new InputMismatchException();
				}
				if (numChars <= 0)
					return -1;
			}
			return buf[curChar++];
		}
		
		boolean isSpaceChar(int c) {
			return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
		}
		
		boolean isEndline(int c) {
			return c == '\n' || c == '\r' || c == -1;
		}
		
		public int nextInt() {
			return Integer.parseInt(next());
		}
		
		public long nextLong() {
			return Long.parseLong(next());
		}
		
		public double nextDouble() {
			return Double.parseDouble(next());
		}
		
		public String next() {
			int c = read();
			while (isSpaceChar(c))
				c = read();
			StringBuilder res = new StringBuilder();
			do {
				res.appendCodePoint(c);
				c = read();
			} while (!isSpaceChar(c));
			return res.toString();
		}
		
		public String nextLine() {
			int c = read();
			while (isEndline(c))
				c = read();
			StringBuilder res = new StringBuilder();
			do {
				res.appendCodePoint(c);
				c = read();
			} while (!isEndline(c));
			return res.toString();
		}
		
		public int[] nextIntArray(int N) {
			int[] ret = new int[N];
			for (int i = 0; i < N; i++)
				ret[i] = this.nextInt();
			return ret;
		}
		
		public int[][] next2DIntArray(int N, int M) {
			int[][] ret = new int[N][];
			for (int i = 0; i < N; i++)
				ret[i] = this.nextIntArray(M);
			return ret;
		}
		
		public long[] nextLongArray(int N) {
			long[] ret = new long[N];
			for (int i = 0; i < N; i++)
				ret[i] = this.nextLong();
			return ret;
		}
		
		public long[][] next2DLongArray(int N, int M) {
			long[][] ret = new long[N][];
			for (int i = 0; i < N; i++)
				ret[i] = nextLongArray(M);
			return ret;
		}
		
		public double[] nextDoubleArray(int N) {
			double[] ret = new double[N];
			for (int i = 0; i < N; i++)
				ret[i] = this.nextDouble();
			return ret;
		}
		
		public double[][] next2DDoubleArray(int N, int M) {
			double[][] ret = new double[N][];
			for (int i = 0; i < N; i++)
				ret[i] = this.nextDoubleArray(M);
			return ret;
		}
		
	}
	
}
