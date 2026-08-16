import java.util.*;

import javafx.util.Pair;

import java.io.*;
/*

5 7
1 2 2
1 3 2
2 3 1
2 4 1
3 4 1
3 5 2
4 5 2
4
2 3 4
3 3 4 5
2 1 7
2 1 2

4 4
1 2 1
2 3 3
3 4 1
4 1 3
2
3 1 2 3
2 2 4


3 3
1 2 1
2 3 1
3 1 1
1
2 2 3

 */
public class e {
	public static void main(String[] arg) throws IOException {
		new e();
	}
	public e() throws IOException {
		FastScanner in = new FastScanner(System.in);
		PrintWriter out = new PrintWriter(System.out);
		int n = in.nextInt();
		int m = in.nextInt();
		ArrayList<Edge> eList = new ArrayList<Edge>();
		for(int i = 0; i < m; i++) {
			eList.add(new Edge(in.nextInt()-1, in.nextInt()-1, in.nextInt(), i));
		}
		int numQueries = in.nextInt();
		boolean[] ans = new boolean[numQueries];
		Arrays.fill(ans, true);
		ArrayList<Edge>[] q = new ArrayList[numQueries];
		PriorityQueue<Pair> pq = new PriorityQueue<Pair>();
		for(int i = 0; i < numQueries; i++) {
			int numEdges = in.nextInt();
			ArrayList<Edge> list = new ArrayList<Edge>();
			for(int j = 0; j < numEdges; j++) {
				int id = in.nextInt()-1;
				list.add(eList.get(id));
			}
			Collections.sort(list);
			q[i] = list;
			pq.add(new Pair(i, 0, list.get(0).w));
		}
		Collections.sort(eList);
		DJ dj = new DJ(n);
		int ptr = 0;
		while(pq.size() > 0) {
			Pair p = pq.poll();
			int qid = p.id;
			int idx = p.idx;
			int w = p.v;
			while(ptr < m && eList.get(ptr).w < w) {
				dj.union(eList.get(ptr).v1, eList.get(ptr).v2);
				ptr++;
			}
			dj.persistent = true;
			while(idx < q[qid].size() && q[qid].get(idx).w == w) {
				Edge e = q[qid].get(idx);
				if(!dj.union(e.v1, e.v2)) ans[qid] = false;
				idx++;
			}
			if(idx < q[qid].size()) {
				pq.add(new Pair(qid, idx, q[qid].get(idx).w));
			}
			dj.undo();
			dj.persistent = false;
		}
		for(int i = 0; i < numQueries; i++) out.println(ans[i]?"YES":"NO");
		in.close(); out.close();
	}
	class Pair implements Comparable<Pair>{
		int id, idx, v;
		public Pair(int a, int b, int c) {
			id = a;
			idx = b;
			v = c;
		}
		public int compareTo(Pair p) {
			return Integer.compare(v, p.v);
		}
	}
	class DJ {
		int[] vs;
		ArrayDeque<Integer> st;
		boolean persistent;
		public DJ(int s) {
			vs = new int[s];
			Arrays.fill(vs, -1);
			st = new ArrayDeque<Integer>();
			persistent = false;
		}
		public int find(int a) {
			if(vs[a] < 0) return a;
			int ret = find(vs[a]);
			return ret;
		}
		public boolean union(int a, int b) {
			int pa = find(a);
			int pb = find(b);
			if(pa == pb) return false;
			if(vs[pb] < vs[pa]) {
				pa = pb^pa^(pb=pa);
			}
			if(persistent) {
				st.push(vs[pa]);
				st.push(pa);
				st.push(vs[pb]);
				st.push(pb);
			}
			vs[pa] += vs[pb];
			vs[pb] = pa;
			return true;
		}
		public void undo() {
			while(st.size() > 0) {
				vs[st.pop()] = st.pop(); 
			}
		}
	}
	class Edge implements Comparable<Edge> {
		int v1, v2, w, id;
		public Edge(int a, int b, int c, int d) {
			v1 = a;
			v2 = b;
			w = c;
			id = d;
		}
		public Edge(Edge e) {
			v1 = e.v1;
			v2 = e.v2;
			w = e.w;
			id = e.id;
		}
		public int compareTo(Edge e) {
			return Integer.compare(w, e.w);
		}
		public String toString() {
			return (v1+1) + " " + (v2+1) + " " + w;
		}
	}
	
	class FastScanner {
		BufferedReader br;
		StringTokenizer st;
		public FastScanner(InputStream in) {
			br = new BufferedReader(new InputStreamReader(in));
			st = new StringTokenizer("");
		}
		public String next() throws IOException {
			while(!st.hasMoreElements()) st = new StringTokenizer(br.readLine());
			return st.nextToken();
		}
		public int nextInt() throws IOException {
			return Integer.parseInt(next());
		}
		public void close() throws IOException {
			br.close();
		}
	}
}
