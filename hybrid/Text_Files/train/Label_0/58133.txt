import java.util.*;
import java.io.*;
import java.math.BigInteger;
import static java.lang.Math.*;

public class Main implements Runnable {
	StringTokenizer tokenizer = new StringTokenizer("");
	BufferedReader in;
	PrintStream out;

	public void debug(String s) {
		System.out.println(s);
	}

	public static void main(String[] args) {
		new Thread(new Main()).start();
	}

	int [] par;

	int parent(int u) {
		return par[u] = (par[u] == u ? u : parent(par[u]));
	}

	Random rand = new Random();

	void unite(int u, int v) {
		int pu = parent(u), pv = parent(v);
		if (rand.nextBoolean()) par[pu] = pv; else par[pv] = pu;	
	}

	class Comp implements Comparable <Comp> {
		int size, x;

		public int compareTo(Comp c) {
			if (size != c.size) return size - c.size;
			return x - c.x;
		}

		Comp(int size, int x) {
			this.size = size;
			this.x = x;
		}
	}

	int x = 0;

	public void run() {
		try {
			Locale.setDefault(Locale.US);
			in = new BufferedReader(new InputStreamReader(System.in));
			out = new PrintStream(System.out);

			int n = nextInt(), m = nextInt(), k = nextInt();
			par = new int[n];
			for (int i = 0; i < n; i++) par[i] = i;
			for (int i = 0; i < m; i++) {
				int u = nextInt() - 1, v = nextInt() - 1;
				unite(u, v);
			}

			int [] cnt = new int[n];
			for (int i = 0; i < n; i++) cnt[parent(i)]++;

			int C = 0;
			int total = 0;

			TreeSet <Comp> set = new TreeSet <Comp> ();

			for (int i = 0; i < n; i++) {
				if (cnt[i] > 0) {
					C++;
					total += min(cnt[i], k);
					set.add(new Comp(cnt[i], x++));
				} 
			}

			int ans = 0;
			while (total / 2 < C - 1) {
				ans++;
				int m1 = set.pollFirst().size, m2 = set.pollFirst().size;
				total -= min(m1, k) + min(m2, k);
				total += min(m1 + m2, k);
				set.add(new Comp(m1 + m2, x++));
				x++;
				C--;	
			}

			out.println(ans);

		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	boolean seekForToken() {
		while (!tokenizer.hasMoreTokens()) {
			String s = null;
			try {
				s = in.readLine();
			} catch (Exception e) {
				e.printStackTrace();
			}
			if (s == null)
				return false;
			tokenizer = new StringTokenizer(s);
		}
		return true;
	}

	String nextToken() {
		return seekForToken() ? tokenizer.nextToken() : null;
	}

	int nextInt() {
		return Integer.parseInt(nextToken());
	}

	long nextLong() {
		return Long.parseLong(nextToken());
	}

	double nextDouble() {
		return Double.parseDouble(nextToken());
	}

	BigInteger nextBig() {
		return new BigInteger(nextToken());
	}
}
