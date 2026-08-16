import static java.util.Arrays.*;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;

public class Main {

	static void tr(Object... os) {
		System.err.println(deepToString(os));
	}

	void solve() {
		int n = sc.nextInt();
		if (n == 0) return;
		int m = sc.nextInt();
		int ans = 0;
		E[] es = new E[m];
		for (int i = 0; i < m; i++) {
			String[] ss = sc.next().split(",");
			int a = Integer.parseInt(ss[0]);
			int b = Integer.parseInt(ss[1]);
			int d = Integer.parseInt(ss[2]);
			es[i] = new E(a, b, d / 100 - 1);
		}
		sort(es);
		UnionFind uf = new UnionFind(n);
		for (E e : es) {
			if (uf.same(e.a, e.b)) {

			} else {
				uf.link(e.a,  e.b);
				ans += e.w;
			}
		}
		out.println(ans);
	}

	static class E implements Comparable<E> {
		int a;
		int b;
		int w;
		public E(int a, int b, int w) {
			this.a = a;
			this.b = b;
			this.w = w;
		}
		@Override
		public int compareTo(E o) {
			return w - o.w;
		}
	}

	public class UnionFind {
		int[] data;

		public UnionFind(int n) {
			data = new int[n];
			fill(data, -1);
		}

		boolean link(int x, int y) {
			x = root(x);
			y = root(y);
			if (x != y) {
				if (data[y] < data[x]) {
					data[y] += data[x];
					data[x] = y;
				} else {
					data[x] += data[y];
					data[y] = x;
				}
			}
			return x != y;
		}

		int root(int x) {
			return data[x] < 0 ? x : (data[x] = root(data[x]));
		}

		int size(int x) { // 要素xが含まれる集合の大きさ
			return -data[root(x)];
		}

		boolean same(int x, int y) { // 同じ集合ならtrue
			return root(x) == root(y);
		}

		int num() { // 異なる集合の数
			int res = 0;
			for (int i = 0; i < data.length; i++)
				res += (root(i) == i) ? 1 : 0;
			return res;
		}
	}




	public static void main(String[] args) throws Exception {
		new Main().run();
	}

	MyScanner sc = null;
	PrintWriter out = null;
	public void run() throws Exception {
		sc = new MyScanner(System.in);
		out = new PrintWriter(System.out);
		for (;sc.hasNext();) {
			solve();
			out.flush();
		}
		out.close();
	}

	class MyScanner {
		String line;
		BufferedReader reader;
		StringTokenizer tokenizer;

		public MyScanner(InputStream stream) {
			reader = new BufferedReader(new InputStreamReader(stream));
			tokenizer = null;
		}
		public void eat() {
			while (tokenizer == null || !tokenizer.hasMoreTokens()) {
				try {
					line = reader.readLine();
					if (line == null) {
						tokenizer = null;
						return;
					}
					tokenizer = new StringTokenizer(line);
				} catch (IOException e) {
					throw new RuntimeException(e);
				}
			}
		}
		public String next() {
			eat();
			return tokenizer.nextToken();
		}
		public String nextLine() {
			try {
				return reader.readLine();
			} catch (IOException e) {
				throw new RuntimeException(e);
			}
		}
		public boolean hasNext() {
			eat();
			return (tokenizer != null && tokenizer.hasMoreElements());
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
		public int[] nextIntArray(int n) {
			int[] a = new int[n];
			for (int i = 0; i < n; i++) a[i] = nextInt();
			return a;
		}
	}
}