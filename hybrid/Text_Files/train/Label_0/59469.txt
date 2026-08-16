import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.*;

public class Main {
	static final long MOD=1000000007;//998244353;
	static long[] dp1;
	static long[] dp2;
	static long[] size1;
	static long[] size2;
	static Binomial bi;
	static long[] ans;
	public static void main(String[] args) {
		PrintWriter out = new PrintWriter(System.out);
		InputReader sc=new InputReader(System.in);
		int N=sc.nextInt();
		long M=MOD;
		graph G=new graph(N);
		for (int i = 0; i < N-1; i++) {
			int a=sc.nextInt()-1;
			int b=sc.nextInt()-1;
			G.addEdge(a, b, 1);
			G.addEdge(b, a, 1);
		}
		dp1=new long[N];
		dp2=new long[N];
		size1=new long[N];
		size2=new long[N];
		ans=new long[N];
		bi=new Binomial();
		G.dfs1(0, -1, M);
		G.dfs2(0, -1, M);
		G.dfs3(0, -1, M);
		for (int i = 0; i < ans.length; i++) {
			out.println(ans[i]);
		}
		out.flush();
 	}
	static class Binomial{
		int MAX = 510000;//ほしいサイズ
		long[] fac=new long[MAX];
		long[] finv=new long[MAX];
		long[] inv=new long[MAX];
		public Binomial(){
			fac[0] = fac[1] = 1;
		    finv[0] = finv[1] = 1;
		    inv[1] = 1;
		    for (int i = 2; i < MAX; i++){
		        fac[i] = fac[i - 1] * i % MOD;
		        inv[i] = MOD - inv[(int) (MOD%i)] * (MOD / i) % MOD;
		        finv[i] = finv[i - 1] * inv[i] % MOD;
		    }//facがx!、finvがx!の逆元,10^7くらいまでのテーブル(MAXまで)
		}
		long fac(int x) {
			return fac[x];
		}
		long invf(int x) {
			return finv[x];
		}
		long nCk(int n,int k,long MOD) {
		    if (n < k) return 0;
		    if (n < 0 || k < 0) return 0;
		    return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD;
		}
	}
	static class graph{
		ArrayList<Edge>[] list;
		int size;
		long INF=Long.MAX_VALUE/2;
		int[] color;
		@SuppressWarnings("unchecked")
		public graph(int n) {
			size = n;
			list = new ArrayList[n];
			color =new int[n];
			for(int i=0;i<n;i++){
				list[i] = new ArrayList<Edge>();
			}
		}
		void addEdge(int from,int to,long w) {
			list[from].add(new Edge(to,w));
		}
		void dfs1(int v,int p,long M) {
			long dpmul=1L;
			long sizes=0;
			for (Edge edge: list[v]) {
				if (edge.to==p) {
					continue;
				}
				dfs1(edge.to, v,M);
				sizes+=size1[edge.to];
				dpmul*=(dp1[edge.to]*bi.invf((int)size1[edge.to]))%M;
				dpmul%=M;
			}
			size1[v]=sizes+1;
			dp1[v]=dpmul*bi.fac((int)sizes);
			dp1[v]%=M;
		}
		void dfs2(int v,int p,long M) {
			if (p==-1) {
				dp2[v]=1;
				size2[v]=0;
			}
			long[] left=new long[list[v].size()+1];
			long[] right=new long[list[v].size()+1];
			left[0]=1;
			right[right.length-1]=1;
			for (int i = 1; i < right.length; i++) {
				if (list[v].get(i-1).to==p) {
					left[i]=left[i-1];
					continue;
				}
				left[i]=(((left[i-1]*dp1[list[v].get(i-1).to])%M)*bi.invf((int)size1[list[v].get(i-1).to]))%M;
				left[i]%=M;
			}
			for (int i = right.length-2; i >= 0; i--) {
				if (list[v].get(i).to==p) {
					right[i]=right[i+1];
					continue;
				}
				right[i]=(((right[i+1]*dp1[list[v].get(i).to])%M)*bi.invf((int)size1[list[v].get(i).to]))%M;
				right[i]%=M;
			}
			for (int i = 0; i < list[v].size(); i++) {
				int to=list[v].get(i).to;
				if (to==p) {
					continue;
				}
				dp2[to]=(left[i]*right[i+1])%M;
				dp2[to]*=(dp2[v]*bi.invf((int)size2[v]))%M;
				dp2[to]%=M;
				dp2[to]*=bi.fac((int)(size2[v]+size1[v]-size1[to]-1));
				dp2[to]%=M;
				size2[to]=size1[v]-size1[to]+size2[v];
				dfs2(to, v, M);
			}
		}
		void dfs3(int v,int p,long M) {
			ans[v]=(bi.invf((int)size2[v])*dp2[v])%M;
			for (Edge nv: list[v]) {
				if (nv.to==p) {
					continue;
				}
				ans[v]*=(bi.invf((int)size1[nv.to])*dp1[nv.to])%M;
				ans[v]%=M;
				dfs3(nv.to, v, M);
			}
			ans[v]*=bi.fac((int)(size1[v]-1+size2[v]));
			ans[v]%=M;
		}
	}
	
	static class Edge implements Comparable<Edge>{
		int to;
		long v;
		public Edge(int to,long v) {
			this.to=to;
			this.v=v;
		}
		@Override
    	public boolean equals(Object obj) {
    		if(obj instanceof Edge) {
    			Edge other = (Edge) obj;
    			return other.to==this.to && other.v==this.v;
    		}
    		return false;
    	}//同値の定義
    	@Override
    	public int hashCode() {
    		return Objects.hash(this.to,this.v);
    	}
    	@Override
		  public int compareTo( Edge p2 ){
			 if (this.v>p2.v) {
				return 1;
			}
			 else if (this.v<p2.v) {
				return -1;
			}
			 else {
				return 0;
			}
		  }
	} 
	static class InputReader { 
		private InputStream in;
		private byte[] buffer = new byte[1024];
		private int curbuf;
		private int lenbuf;
		public InputReader(InputStream in) {
			this.in = in;
			this.curbuf = this.lenbuf = 0;
		}
 
		public boolean hasNextByte() {
			if (curbuf >= lenbuf) {
				curbuf = 0;
				try {
					lenbuf = in.read(buffer);
				} catch (IOException e) {
					throw new InputMismatchException();
				}
				if (lenbuf <= 0)
					return false;
			}
			return true;
		}
 
		private int readByte() {
			if (hasNextByte())
				return buffer[curbuf++];
			else
				return -1;
		}
 
		private boolean isSpaceChar(int c) {
			return !(c >= 33 && c <= 126);
		}
 
		private void skip() {
			while (hasNextByte() && isSpaceChar(buffer[curbuf]))
				curbuf++;
		}
 
		public boolean hasNext() {
			skip();
			return hasNextByte();
		}
 
		public String next() {
			if (!hasNext())
				throw new NoSuchElementException();
			StringBuilder sb = new StringBuilder();
			int b = readByte();
			while (!isSpaceChar(b)) {
				sb.appendCodePoint(b);
				b = readByte();
			}
			return sb.toString();
		}
 
		public int nextInt() {
			if (!hasNext())
				throw new NoSuchElementException();
			int c = readByte();
			while (isSpaceChar(c))
				c = readByte();
			boolean minus = false;
			if (c == '-') {
				minus = true;
				c = readByte();
			}
			int res = 0;
			do {
				if (c < '0' || c > '9')
					throw new InputMismatchException();
				res = res * 10 + c - '0';
				c = readByte();
			} while (!isSpaceChar(c));
			return (minus) ? -res : res;
		}
 
		public long nextLong() {
			if (!hasNext())
				throw new NoSuchElementException();
			int c = readByte();
			while (isSpaceChar(c))
				c = readByte();
			boolean minus = false;
			if (c == '-') {
				minus = true;
				c = readByte();
			}
			long res = 0;
			do {
				if (c < '0' || c > '9')
					throw new InputMismatchException();
				res = res * 10 + c - '0';
				c = readByte();
			} while (!isSpaceChar(c));
			return (minus) ? -res : res;
		}
 
		public double nextDouble() {
			return Double.parseDouble(next());
		}
 
		public int[] nextIntArray(int n) {
			int[] a = new int[n];
			for (int i = 0; i < n; i++)
				a[i] = nextInt();
			return a;
		}
 
		public long[] nextLongArray(int n) {
			long[] a = new long[n];
			for (int i = 0; i < n; i++)
				a[i] = nextLong();
			return a;
		}
 
		public char[][] nextCharMap(int n, int m) {
			char[][] map = new char[n][m];
			for (int i = 0; i < n; i++)
				map[i] = next().toCharArray();
			return map;
		}
	}
}
