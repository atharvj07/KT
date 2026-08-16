
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map.Entry;
import java.util.Scanner;
import java.util.StringTokenizer;
import java.util.TreeMap;

public class Main {

	public static void main(String[] args) throws IOException, InterruptedException {
		PrintWriter pw = new PrintWriter(System.out);
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		DSU dsu = new DSU(n+1);
		Edge[] edges = new Edge[m];
		for (int i = 0; i < m; i++) {
			edges[i] = new Edge(sc.nextInt(), sc.nextInt(), sc.nextInt());
		}
		int ans=0; 
		Arrays.sort(edges);
		for (int i = 0; i < m; i++) {
			int j = i;
			while (j < m && edges[i].c == edges[j].c)
				j++;
			j--;
			int c = 0;
			for (int k = i; k <= j; k++) {
				if (!dsu.isSameSet(edges[k].u, edges[k].v))
					c++;
			}
			int c2 = 0;
			for (int k = i; k <= j; k++) {
				if (!dsu.isSameSet(edges[k].u, edges[k].v)) {
					dsu.unionSet(edges[k].u, edges[k].v);
					c2++;
				}
			}
		ans+=c-c2;
		i=j; // v important 
			
		}pw.println(ans);
		pw.flush();
		pw.close();
	}

	static class Edge implements Comparable<Edge> {
		int u, v, c;

		public Edge(int u, int v, int c) {
			this.u = u;
			this.v = v;
			this.c = c;
		}

		public int compareTo(Edge o) {
			// TODO Auto-generated method stub
			return c - o.c;
		}

	}

	static class DSU {
		int[] p, rank, size;

		public DSU(int N) {
			p = new int[N + 1];
			rank = new int[N + 1];
			size = new int[N + 1];
			for (int i = 0; i < N; i++) {
				p[i] = i;
				size[i] = 1;
			}
		}

		public int findSet(int i) {
			return p[i] == i ? i : (p[i] = findSet(p[i]));
		}

		public boolean isSameSet(int i, int j) {
			return findSet(i) == findSet(j);
		}

		public void unionSet(int i, int j) {
			if (isSameSet(i, j))
				return;

			int x = findSet(i), y = findSet(j);
			if (rank[x] > rank[y]) {
				size[x] += size[y];
				p[y] = x;
			} else {
				p[x] = y;
				size[y] += size[x];
				if (rank[x] == rank[y])
					rank[y]++;
			}
		}

	}

	static class Scanner {
		StringTokenizer st;
		BufferedReader br;

		public Scanner(InputStream s) {
			br = new BufferedReader(new InputStreamReader(s));
		}

		public Scanner(String file) throws FileNotFoundException {
			br = new BufferedReader(new FileReader(file));
		}

		public String next() throws IOException {
			while (st == null || !st.hasMoreTokens())
				st = new StringTokenizer(br.readLine());
			return st.nextToken();
		}

		public int nextInt() throws IOException {
			return Integer.parseInt(next());
		}

		public long nextLong() throws IOException {
			return Long.parseLong(next());
		}

		public String nextLine() throws IOException {
			return br.readLine();
		}

		public double nextDouble() throws IOException {
			return Double.parseDouble(next());
		}

		public boolean ready() throws IOException {
			return br.ready();
		}

	}
}

   	 	 	  				 		    	   	  	