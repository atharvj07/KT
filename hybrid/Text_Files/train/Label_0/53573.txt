import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class F {

	static int INF = 1_000_000_000;
	static int R,C,Q;
	static Query qs[];
	static int addHere[];
	static boolean uselessQuery[];
	static ArrayDeque<Integer> hits[][];
	static int [] dr = new int[] {-1,1,0,0};
	static int [] dc = new int[] {0,0,-1,1};
	public static void main(String[] args) {
		FS in = new FS();
		PrintWriter out = new PrintWriter(System.out);
		
		R = in.nextInt();
		C = in.nextInt();
		Q = in.nextInt();
		qs = new Query[Q+R*C];
		for(int i = 0; i < R; i++)
			for(int j = 0; j < C; j++)
				qs[C*i+j] = new Query(i,j,0,C*i+j);
			
		for(int i = 0; i < Q; i++) {
			int r = in.nextInt()-1;
			int c = in.nextInt()-1;
			int v = in.nextInt();
			qs[R*C + i] = new Query(r,c,v,R*C + i);
		}
		
		addHere = new int[Q+R*C];
		uselessQuery = new boolean[Q+R*C];
		
		hits = new ArrayDeque[R][C];
		for(int i = 0; i < R; i++)
			for(int j = 0; j < C; j++)
				hits[i][j] = new ArrayDeque<Integer>();
		for(Query q : qs) {
			if(hits[q.r][q.c].size() > 0 && qs[hits[q.r][q.c].peek()].V == q.V) uselessQuery[q.id] = true;
			else hits[q.r][q.c].add(q.id);
		}
				
		DSU dsu = new DSU(R*C);
		int l = 0, r = 0;
		while(l < qs.length) {
			while(r < qs.length && qs[r].V == qs[l].V) r++;
			
//			System.out.println("["+l+", "+(r-1)+"]");
			
			// range [l, r)
			dsu.clear();
			
			// Get what it's like going forward
			for(int i = l; i < r; i++) {
				if(uselessQuery[i]) continue;
				int cur = dsu.numComponents;
				dsu.setActive(m(qs[i].r, qs[i].c));
				for(int k = 0; k < dr.length; k++) {
					int nr = qs[i].r + dr[k], nc = qs[i].c + dc[k];
					if(valid(nr,nc)) dsu.union(m(qs[i].r, qs[i].c), m(nr,nc));
				}
				int dif = dsu.numComponents - cur;
				addHere[i] += dif;
			}
			
			ArrayList<Pair> ps = new ArrayList<Pair>();
			for(int i = l; i < r; i++) {
				if(uselessQuery[i]) continue;
				int me = hits[qs[i].r][qs[i].c].poll();
				int next = hits[qs[i].r][qs[i].c].isEmpty() ? INF : hits[qs[i].r][qs[i].c].peek();
				ps.add(new Pair(qs[i].r, qs[i].c, me, next));
			}
			Collections.sort(ps);
			dsu.clear();
			for(Pair p : ps) {
				int afterKilled = dsu.numComponents;
				dsu.setActive(m(p.r,p.c));
				for(int k = 0; k < dr.length; k++) {
					int nr = p.r + dr[k], nc = p.c + dc[k];
					if(valid(nr,nc)) dsu.union(m(p.r, p.c), m(nr,nc));
				}
				int beforeKilled = dsu.numComponents;
//				System.out.println(p.r+" "+p.c+" "+p.whenMade+" "+p.whenKilled+"  ab = "+afterKilled+" "+beforeKilled);
				if(p.whenKilled == INF) continue;
				addHere[p.whenKilled] += (afterKilled-beforeKilled);
			}
			
			l = r;
		}
		
		int have = 0;
		for(int i = 0; i < Q+R*C; i++) {
			have += addHere[i];
			if(i >= R*C) out.println(have);
		}
		
//		System.out.println(Arrays.toString(addHere));
		
		out.close();
	}
	
	static int m(int r, int c) { return C*r + c;}
	static boolean valid(int r, int c) {
		return r >= 0 && r < R && c >= 0 && c < C;
	}
	
	static class Pair implements Comparable<Pair>{
		int r,c,whenMade,whenKilled;
		public Pair(int rr, int cc, int wM, int wK) {
			r=rr;
			c=cc;
			whenMade = wM;
			whenKilled = wK;
		}
		@Override
		public int compareTo(Pair o) {
			return o.whenKilled-whenKilled;
		}
	}
	
	static class Query {
		int r,c,V,id;
		public Query(int rr, int cc, int vv, int ii) {
			r=rr;
			c=cc;
			V=vv;
			id=ii;
		}
	}
	
	static class DSU {
		int [] sz, p;
		int numComponents;
		public DSU(int n) {
			sz = new int[n];
			p = new int[n];
			numComponents = 0;
			for(int i = 0; i < n; i++) {
				p[i] = i;
				sz[i] = -1;
			}
		}
		void setActive(int x) {
			if(sz[x] >= 0) return;
			sz[x] = 1;
			numComponents++;
		}
		int find(int x) {
			return p[x] == x ? x : (p[x] = find(p[x]));
		}
		void union(int a, int b) {
			if((a=find(a)) == (b=find(b))) return;
			if(sz[a] < 0 || sz[b] < 0) return;
			numComponents--;
			if(sz[a] > sz[b]) {
				p[b] = a;
				sz[a] += sz[b];
			}
			else {
				p[a] = b;
				sz[b] += sz[a];
			}
		}
		void clear() {
			numComponents = 0;
			for(int i = 0; i < p.length; i++) {
				p[i] = i;
				sz[i] = -1;
			}
		}
	}
	
	static class FS{
		BufferedReader br;
		StringTokenizer st;
		public FS() {
			br = new BufferedReader(new InputStreamReader(System.in));
		}
		String next() {
			while(st == null || !st.hasMoreElements()) {
				try {st = new StringTokenizer(br.readLine());}
				catch(Exception e) { throw null;}
			}
			return st.nextToken();
		}
		int nextInt() { return Integer.parseInt(next());}
		double nextDouble() { return Double.parseDouble(next());}
		long nextLong() { return Long.parseLong(next());}
		int[] NIA(int n) {
			int r[] = new int[n];
			for(int i = 0; i < n; i++) r[i] = nextInt();
			return r;
		}
		long[] NLA(int n) {
			long r[] = new long[n];
			for(int i = 0; i < n; i++) r[i] = nextLong();
			return r;
		}
		char[][] grid(int r, int c){
			char res[][] = new char[r][c];
			for(int i = 0; i < r; i++) {
				char l[] = next().toCharArray();
				for(int j = 0; j < c; j++) {
					res[i][j] = l[j];
				}
			}
			return res;
		}
	}
	
}
