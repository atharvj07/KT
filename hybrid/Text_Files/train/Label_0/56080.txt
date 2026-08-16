// upsolve with rainboy
import java.io.*;
import java.util.*;

public class CF1288F extends PrintWriter {
	CF1288F() { super(System.out); }
	Scanner sc = new Scanner(System.in);
	public static void main(String[] $) {
		CF1288F o = new CF1288F(); o.main(); o.flush();
	}

	static final int INF = 0x3f3f3f3f;
	int[] oo, oh; int __ = 1;
	int link(int o, int h) {
		oo[__] = o; oh[__] = h;
		return __++;
	}
	int[] ii, jj, cc, cost, cost_; int m_;
	int[] ae, pi, dd, ff; int n_;
	int[] pq, iq; int cnt;
	void init() {
		oo = new int[1 + m_ * 2]; oh = new int[1 + m_ * 2];
		ii = new int[m_]; jj = new int[m_];
		cc = new int[m_ * 2];
		cost = new int[m_]; cost_ = new int[m_];
		ae = new int[n_]; pi = new int[n_]; dd = new int[n_]; ff = new int[n_];
		pq = new int[1 + n_]; iq = new int[n_];
		m_ = 0;
	}
	void link_(int i, int j, int c, int co) {
		int h = m_++;
		ii[h] = i; jj[h] = j; cc[h << 1] = c; cost[h] = co;
		ae[i] = link(ae[i], h << 1);
		ae[j] = link(ae[j], h << 1 | 1);
	}
	boolean less(int u, int v) {
		return pi[u] < pi[v] || pi[u] == pi[v] && dd[u] < dd[v];
	}
	int i2(int i) {
		return (i *= 2) > cnt ? 0 : i < cnt && less(pq[i + 1], pq[i]) ? i + 1 : i;
	}
	void pq_up(int u) {
		int i, j, v;
		for (i = iq[u]; (j = i / 2) > 0 && less(u, v = pq[j]); i = j)
			pq[iq[v] = i] = v;
		pq[iq[u] = i] = u;
	}
	void pq_dn(int u) {
		int i, j, v;
		for (i = iq[u]; (j = i2(i)) > 0 && less(v = pq[j], u); i = j)
			pq[iq[v] = i] = v;
		pq[iq[u] = i] = u;
	}
	void pq_add_last(int u) {
		pq[iq[u] = ++cnt] = u;
	}
	int pq_remove_first() {
		int u = pq[1], v = pq[cnt--];
		if (v != u) {
			iq[v] = 1; pq_dn(v);
		}
		iq[u] = 0;
		return u;
	}
	boolean dijkstra(int s, int t) {
		Arrays.fill(pi, INF);
		pi[s] = 0; pq_add_last(s);
		while (cnt > 0) {
			int i = pq_remove_first();
			int d = dd[i] + 1;
			for (int o = ae[i]; o != 0; o = oo[o]) {
				int h_ = oh[o];
				if (cc[h_] > 0) {
					int h = h_ >> 1;
					int j = i ^ ii[h] ^ jj[h];
					int p = pi[i] + ((h_ & 1) == 0 ? cost_[h] : -cost_[h]);
					if (pi[j] > p || (pi[j] == p && dd[j] > d)) {
						if (pi[j] == INF)
							pq_add_last(j);
						pi[j] = p; dd[j] = d; ff[j] = h_;
						pq_up(j);
					}
				}
			}
		}
		return pi[t] != INF;
	}
	boolean trace(int s, int t) {
		int sum = 0;
		for (int i = t; i != s; ) {
			int h_ = ff[i], h = h_ >> 1;
			sum += (h_ & 1) == 0 ? cost[h] : -cost[h];
			i ^= ii[h] ^ jj[h];
		}
		if (sum >= 0)
			return false;
		for (int i = t; i != s; ) {
			int h_ = ff[i], h = h_ >> 1;
			cc[h_]--; cc[h_ ^ 1]++;
			i ^= ii[h] ^ jj[h];
		}
		return true;
	}
	int edmonds_karp(int s, int t) {
		for (int h = 0; h < m_; h++)
			cost_[h] = cost[h];
		while (dijkstra(s, t)) {
			if (!trace(s, t))
				break;
			for (int h = 0; h < m_; h++) {
				int i = ii[h], j = jj[h];
				if (pi[i] != INF && pi[j] != INF) {
					// pi[j] <= pi[i] + cost_[h]
					// cost_[h] + pi[i] - pi[j] >= 0
					cost_[h] += pi[i] - pi[j];
				}
			}
		}
		int sum = 0;
		for (int h = 0; h < m_; h++)
			sum += cost[h] * cc[h << 1 | 1];
		return sum;
	}
	void main() {
		int n1 = sc.nextInt();
		int n2 = sc.nextInt();
		int m = sc.nextInt();
		int r = sc.nextInt();
		int b = sc.nextInt();
		int inf = m * (r + b) + 1;
		n_ = 1 + n1 + n2 + 1;
		m_ = (m + n1 + n2) * 2;
		init();
		byte[] c1 = sc.next().getBytes();
		byte[] c2 = sc.next().getBytes();
		for (int h = 0; h < m; h++) {
			int i = sc.nextInt() - 1;
			int j = sc.nextInt() - 1;
			int i_ = 1 + i;
			int j_ = 1 + n1 + j;
			link_(i_, j_, 1, r);
			link_(j_, i_, 1, b);
		}
		int s = 0, t = n_ - 1;
		for (int i = 0; i < n1; i++) {
			int i_ = 1 + i;
			if (c1[i] == 'R') {
				link_(s, i_, 1, -inf);
				link_(s, i_, m, 0);
			} else if (c1[i] == 'B') {
				link_(i_, t, 1, -inf);
				link_(i_, t, m, 0);
			} else {
				link_(s, i_, m, 0);
				link_(i_, t, m, 0);
			}
		}
		for (int j = 0; j < n2; j++) {
			int j_ = 1 + n1 + j;
			if (c2[j] == 'R') {
				link_(j_, t, 1, -inf);
				link_(j_, t, m, 0);
			} else if (c2[j] == 'B') {
				link_(s, j_, 1, -inf);
				link_(s, j_, m, 0);
			} else {
				link_(s, j_, m, 0);
				link_(j_, t, m, 0);
			}
		}
		int ans = edmonds_karp(s, t);
		for (int h = 0; h < m_; h++)
			if (cost[h] == -inf) {
				if (cc[h << 1 | 1] == 0) {
					println(-1);
					return;
				}
				ans += inf;
			}
		println(ans);
		char[] colors = new char[m];
		for (int h = 0; h < m; h++) {
			int hr = h << 1, hb = h << 1 | 1;
			if (cc[hr << 1 | 1] > 0)
				colors[h] = 'R';
			else if (cc[hb << 1 | 1] > 0)
				colors[h] = 'B';
			else
				colors[h] = 'U';
		}
		println(colors);
	}
}
