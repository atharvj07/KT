// upsolve with rainboy
import java.io.*;
import java.util.*;

public class CF1187G extends PrintWriter {
	CF1187G() { super(System.out); }
	static class Scanner {
		Scanner(InputStream in) { this.in = in; } InputStream in;
		int k, l; byte[] bb = new byte[1 << 15];
		byte getc() {
			if (k >= l) {
				k = 0;
				try { l = in.read(bb); } catch (IOException e) { l = 0; }
				if (l <= 0) return -1;
			}
			return bb[k++];
		}
		int nextInt() {
			byte c = 0; while (c <= 32) c = getc();
			int a = 0;
			while (c > 32) { a = a * 10 + c - '0'; c = getc(); }
			return a;
		}
	}
	Scanner sc = new Scanner(System.in);
	public static void main(String[] $) {
		CF1187G o = new CF1187G(); o.main(); o.flush();
	}

	static final int INF = 0x3f3f3f3f;
	ArrayList[] aa_;
	int n_, m_;
	int[] pi, bb;
	int[] uu, vv, uv, cost;
	int[] cc;
	void init() {
		aa_ = new ArrayList[n_];
		for (int u = 0; u < n_; u++)
			aa_[u] = new ArrayList<Integer>();
		pi = new int[n_];
		bb = new int[n_];
		qq = new int[nq];
		iq = new boolean[n_];
		uu = new int[m_];
		vv = new int[m_];
		uv = new int[m_];
		cost = new int[m_];
		cc = new int[m_ * 2];
		m_ = 0;
	}
	void link(int u, int v, int cap, int cos) {
		int h = m_++;
		uu[h] = u;
		vv[h] = v;
		uv[h] = u ^ v;
		cost[h] = cos;
		cc[h << 1 ^ 0] = cap;
		aa_[u].add(h << 1 ^ 0);
		aa_[v].add(h << 1 ^ 1);
	}
	int[] qq;
	int nq = 1 << 20, head, cnt;
	boolean[] iq;
	void enqueue(int v) {
		if (iq[v])
			return;
		if (head + cnt == nq) {
			if (cnt * 2 <= nq)
				System.arraycopy(qq, head, qq, 0, cnt);
			else {
				int[] qq_ = new int[nq *= 2];
				System.arraycopy(qq, head, qq_, 0, cnt);
				qq = qq_;
			}
			head = 0;
		}
		qq[head + cnt++] = v; iq[v] = true;
	}
	int dequeue() {
		int u = qq[head++]; cnt--; iq[u] = false;
		return u;
	}
	boolean spfa(int s, int t) {
		Arrays.fill(pi, INF);
		pi[s] = 0;
		head = cnt = 0;
		enqueue(s);
		while (cnt > 0) {
			int u = dequeue();
			ArrayList<Integer> adj = aa_[u];
			for (int h_ : adj)
				if (cc[h_] > 0) {
					int h = h_ >> 1;
					int p = pi[u] + ((h_ & 1) == 0 ? cost[h] : -cost[h]);
					int v = u ^ uv[h];
					if (pi[v] > p) {
						pi[v] = p;
						bb[v] = h_;
						enqueue(v);
					}
				}
		}
		return pi[t] != INF;
	}
	void push(int s, int t) {
		int c = INF;
		for (int u = t, h_, h; u != s; u ^= uv[h]) {
			h = (h_ = bb[u]) >> 1;
			c = Math.min(c, cc[h_]);
		}
		for (int u = t, h_, h; u != s; u ^= uv[h]) {
			h = (h_ = bb[u]) >> 1;
			cc[h_] -= c; cc[h_ ^ 1] += c;
		}
	}
	void push1(int s, int t) {
		for (int u = t, h_, h; u != s; u ^= uv[h]) {
			h = (h_ = bb[u]) >> 1;
			cc[h_]--; cc[h_ ^ 1]++;
		}
	}
	int edmonds_karp(int s, int t) {
		while (spfa(s, t))
			push1(s, t);
		int c = 0;
		for (int h = 0; h < m_; h++)
			c += cost[h] * cc[h << 1 ^ 1];
		return c;
	}
	void main() {
		int n = sc.nextInt();
		int m = sc.nextInt();
		int k = sc.nextInt();
		int c = sc.nextInt();
		int d = sc.nextInt();
		int[] ii = new int[k];
		for (int h = 0; h < k; h++)
			ii[h] = sc.nextInt() - 1;
		ArrayList[] aa = new ArrayList[n];
		for (int i = 0; i < n; i++)
			aa[i] = new ArrayList<Integer>();
		for (int h = 0; h < m; h++) {
			int i = sc.nextInt() - 1;
			int j = sc.nextInt() - 1;
			aa[i].add(j);
			aa[j].add(i);
		}
		int t = n + k + 1;
		n_ = n * t + 1;
		m_ = k + (m * 2 * k + n) * (t - 1);
		init();
		for (int i = 0; i < n; i++) {
			ArrayList<Integer> adj = aa[i];
			for (int s = 0; s < t - 1; s++) {
				int u = i * t + s;
				for (int j : adj) {
					int v = j * t + s + 1;
					for (int x = 1; x <= k; x++)
						link(u, v, 1, c + (x * 2 - 1) * d);
				}
			}
		}
		for (int i = 0; i < n; i++)
			for (int s = 0; s < t - 1; s++) {
				int u = i * t + s, v = u + 1;
				link(u, v, k, i == 0 ? 0 : c);
			}
		for (int h = 0; h < k; h++)
			link(n_ - 1, ii[h] * t + 0, 1, 0);
		println(edmonds_karp(n_ - 1, 0 * t + t - 1));
	}
}
