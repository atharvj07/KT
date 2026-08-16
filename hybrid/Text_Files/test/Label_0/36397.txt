import java.io.*;
import java.util.*;

public class CF1197F extends PrintWriter {
	CF1197F() { super(System.out, true); }
	Scanner sc = new Scanner(System.in);
	public static void main(String[] $) {
		CF1197F o = new CF1197F(); o.main(); o.flush();
	}

	static final int MD = 998244353, K = 64;
	static class B {
		int j, c;
		B(int j, int c) {
			this.j = j; this.c = c;
		}
	}
	void mult(int[] uu, int[][] aa, int[] vv) {
		for (int j = 0; j < K; j++) {
			long v = 0;
			for (int i = 0; i < K; i++)
				v = (v + (long) uu[i] * aa[i][j]) % MD;
			vv[j] = (int) v;
		}
	}
	void mult(int[][] aa, int[][] bb, int[][] cc) {
		for (int i = 0; i < K; i++)
			for (int j = 0; j < K; j++) {
				long c = 0;
				for (int k = 0; k < K; k++)
					c = (c + (long) aa[i][k] * bb[k][j]) % MD;
				cc[i][j] = (int) c;
			}
	}
	int mex(int y) {
		if ((y & 1) == 0) return 0;
		if ((y & 2) == 0) return 1;
		if ((y & 4) == 0) return 2;
		return 3;
	}
	void solve(int n, B[] bb, int[] cnt) {
		Arrays.sort(bb, (a, b) -> a.j - b.j);
		int[] uu = new int[K];
		int[] vv = new int[K];
		uu[3 << 4 | 3 << 2 | 0] = bb.length == 0 || bb[0].j > 0 ? 3 : 1;
		int j = 0;
		for (B b : bb) {
			if (b.j == 0)
				continue;
			if (j < b.j - 1) {
				int p = b.j - 1 - j;
				for (int h = 0; 1 << h <= p; h++)
					if ((p & 1 << h) != 0) {
						mult(uu, pp[h], vv);
						int[] tmp = uu; uu = vv; vv = tmp;
					}
				j = b.j - 1;
			}
			if (j < b.j) {
				mult(uu, zz[b.c], vv);
				int[] tmp = uu; uu = vv; vv = tmp;
				j = b.j;
			}
		}
		if (j < n - 1) {
			int p = n - 1 - j;
			for (int h = 0; 1 << h <= p; h++)
				if ((p & 1 << h) != 0) {
					mult(uu, pp[h], vv);
					int[] tmp = uu; uu = vv; vv = tmp;
				}
		}
		for (int u = 0; u < 4; u++)
			for (int v = 0; v < 4; v++)
				for (int w = 0; w < 4; w++) {
					int uvw = u << 4 | v << 2 | w;
					cnt[w] = (cnt[w] + uu[uvw]) % MD;
				}
	}
	int[][][] pp, zz;
	void init(int[][] ff, int n) {
		int l = 0;
		while (1 << l + 1 <= n - 1)
			l++;
		pp = new int[l + 1][K][K];
		zz = new int[3][K][K];
		for (int u = 0; u < 4; u++)
			for (int v = 0; v < 4; v++)
				for (int w = 0; w < 4; w++)
					for (int c = 0; c < 3; c++) {
						int y = 0;
						if (ff[c][0] == 1) y |= 1 << w;
						if (ff[c][1] == 1) y |= 1 << v;
						if (ff[c][2] == 1) y |= 1 << u;
						int x = mex(y);
						int uvw = u << 4 | v << 2 | w;
						int vwx = v << 4 | w << 2 | x;
						zz[c][uvw][vwx]++;
						pp[0][uvw][vwx]++;
					}
		for (int h = 0; h < l; h++)
			mult(pp[h], pp[h], pp[h + 1]);
	}
	void main() {
		int n = sc.nextInt();
		int[] nn = new int[n];
		int n_ = 0;
		for (int i = 0; i < n; i++) {
			nn[i] = sc.nextInt();
			n_ = Math.max(n_, nn[i]);
		}
		int m = sc.nextInt();
		List[] ll = new List[n];
		for (int i = 0; i < n; i++)
			ll[i] = new ArrayList<B>();
		for (int h = 0; h < m; h++) {
			int i = sc.nextInt() - 1;
			int j = sc.nextInt() - 1;
			int c = sc.nextInt() - 1;
			ll[i].add(new B(j, c));
		}
		int[][] ff = new int[3][3];
		for (int c = 0; c < 3; c++)
			for (int d = 0; d < 3; d++)
				ff[c][d] = sc.nextInt();
		init(ff, n_);
		int[] dp = new int[4];
		int[] dq = new int[4];
		int[] cnt = new int[4];
		dp[0] = 1;
		for (int i = 0; i < n; i++) {
			Arrays.fill(dq, 0);
			Arrays.fill(cnt, 0);
			List<B> list = ll[i];
			solve(nn[i], list.toArray(new B[list.size()]), cnt);
			for (int u = 0; u < 4; u++)
				for (int v = 0; v < 4; v++) {
					int w = u ^ v;
					dq[w] = (int) ((dq[w] + (long) dp[u] * cnt[v]) % MD);
				}
			int[] tmp = dp; dp = dq; dq = tmp;
		}
		println(dp[0]);
	}
}
