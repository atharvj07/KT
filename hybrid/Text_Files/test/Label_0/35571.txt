import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;
import java.util.StringTokenizer;
import java.util.TreeMap;
import java.util.TreeSet;

public class CodeForces {

	static int OO = (int) 1e9;

	static int[][] grid;
	static TreeSet<Pair> chess;
	static TreeSet<Pair> visited;

	static int[] dx = { -1, 1, 0, 0, -1, -1, 1, 1 };
	static int[] dy = { 0, 0, -1, 1, 1, -1, 1, -1 };

	static boolean valid(int x, int y) {
		return (x >= 1 && x < OO && y >= 1 && y < OO && chess.contains(new Pair(x, y)))
				&& !visited.contains(new Pair(x, y));
	}

	static int bfs(int x0, int y0, int x1, int y1) {

		Queue<Pair> qu = new LinkedList<>();

		TreeMap<Pair, Integer> dis = new TreeMap<>();
		visited = new TreeSet<>();

		dis.put(new Pair(x0, y0), 0);
		qu.add(new Pair(x0, y0));

		while (!qu.isEmpty()) {

			Pair cur = qu.poll();

			if (cur.x == x1 && cur.y == y1)
				return dis.get(cur);

			for (int i = 0; i < 8; i++) {
				int x = cur.x + dx[i], y = cur.y + dy[i];
				Pair tmp = new Pair(x, y);
				if (valid(x, y)) {
					qu.add(tmp);
					dis.put(tmp, dis.get(cur) + 1);
					visited.add(new Pair(x, y));
				}
			}
		}

		return -1;

	}

	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
		PrintWriter pw = new PrintWriter(System.out);

		int x0 = sc.nextInt(), y0 = sc.nextInt(), x1 = sc.nextInt(), y1 = sc.nextInt();

		int n = sc.nextInt();

		chess = new TreeSet<Pair>();

		for (int i = 0; i < n; i++) {
			int r = sc.nextInt();
			int a = sc.nextInt();
			int b = sc.nextInt();
			for (int j = a; j <= b; j++)
				chess.add(new Pair(r, j));
		}
		if(!chess.contains(new Pair(x0, y0)))
		{
			System.out.println(-1);
			return;
		}
		int ans = bfs(x0, y0, x1, y1);
		pw.print(ans);
		pw.close();

	}

	static class Triple {

		int r, a, b;

		public Triple(int r, int a, int b) {
			this.a = a;
			this.b = b;
			this.r = r;
		}
	}

	static class Pair implements Comparable<Pair> {

		int x, y;

		public Pair(int x, int y) {
			this.x = x;
			this.y = y;
		}

		@Override
		public int compareTo(Pair a){
			if(a.x==x)return a.y-y;
			return a.x-x;
			
		}

		public String toString() {
			return x + " " + y;
		}
	}

	static class Scanner {
		StringTokenizer st;
		BufferedReader br;

		public Scanner(InputStream s) {
			br = new BufferedReader(new InputStreamReader(s));
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
			String x = next();
			StringBuilder sb = new StringBuilder("0");
			double res = 0, f = 1;
			boolean dec = false, neg = false;
			int start = 0;
			if (x.charAt(0) == '-') {
				neg = true;
				start++;
			}
			for (int i = start; i < x.length(); i++)
				if (x.charAt(i) == '.') {
					res = Long.parseLong(sb.toString());
					sb = new StringBuilder("0");
					dec = true;
				} else {
					sb.append(x.charAt(i));
					if (dec)
						f *= 10;
				}
			res += Long.parseLong(sb.toString()) / f;
			return res * (neg ? -1 : 1);
		}

		public boolean ready() throws IOException {
			return br.ready();
		}

	}
}
