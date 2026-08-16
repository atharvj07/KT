import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Objects;
import java.util.StringTokenizer;
 
public class Main {
 
	public static void main(String[] args) {
		InputStream inputStream = System.in;
		OutputStream outputStream = System.out;
		InputReader in = new InputReader(inputStream);
		PrintWriter out = new PrintWriter(outputStream);
		DreamTask solver = new DreamTask();
		solver.solve(1, in, out);
		out.close();
 
	}
	static class DreamTask{
		
		public void solve(int testcaseNumber, InputReader in, PrintWriter out) {
			int n = in.nextInt(), k= in.nextInt(), l = in.nextInt();
			UF road = new UF(n);
			UF rail = new UF(n);
			int x,y;
			for(int i = -1; ++i < k;) {
				x = in.nextInt(); y = in.nextInt();
				road.union(x,y);
			}
			for(int i = -1; ++i < l;) {
				x = in.nextInt(); y = in.nextInt();
				rail.union(x,y);
			}
			
			HashMap<pair, Integer> map = new HashMap<pair, Integer>();
			pair[] vp = new pair[n+1];
			for(int i = 0; ++i <= n;) {
				pair p = new pair(road.root(i), rail.root(i));
				vp[i] = p;
				if(map.containsKey(p)) map.put(p, map.get(p)+1);
				else map.put(p, 1);
			}
			
			for(int i = 0; ++i <= n;) {
				out.print(map.get(vp[i])+" ");
				
			}
			
			
		}
		
	}
	
/*
4
3
6
9
10
 */
	static class pair{
		int f,s;
 
		public pair(int f, int s) {
			this.f = f;
			this.s = s;
		}
		
		@Override
		public boolean equals(Object o) {
			if(o==null||getClass()!=o.getClass()) return false;
			if(this == o) return true;
			pair p = (pair) o;
			return f == p.f && s == p.s;
			
		}
		
		@Override
		public int hashCode() {
			return Objects.hash(f,s);
		}
	}
	static class UF{
		int[] u;
 
		public UF(int n) {
			u = new int[n+5];
			Arrays.fill(u,-1);
		}
		
		public int root(int x) {return u[x] <0?x:(u[x] = root(u[x]));}
		public void union(int x, int y) {
			x = root(x); y=root(y);
			if(x!=y) {u[x]+=u[y];u[y] = x;}
		}
		
	}
	static class InputReader{
		public BufferedReader reader;
		public StringTokenizer tokenizer;
		
		public InputReader(InputStream stream) {
			reader = new BufferedReader(new InputStreamReader(stream), 32768);
			tokenizer = null;
		}
		
		public String next() {
			while(tokenizer==null || !tokenizer.hasMoreTokens()) {
				try {
					tokenizer = new StringTokenizer(reader.readLine());
				} catch (IOException e) {
					throw new RuntimeException(e);
				}
			}
			return tokenizer.nextToken();
		}
		
		public int nextInt() {
			return Integer.parseInt(next());
		}
	}
 
}