// practice with rainboy
import java.io.*;
import java.util.*;

public class CF474E extends PrintWriter {
	CF474E() { super(System.out, true); }
	Scanner sc = new Scanner(System.in);
	public static void main(String[] $) {
		CF474E o = new CF474E(); o.main(); o.flush();
	}

	int[] tr; int n_;
	int query(int l, int r) {
		int k = 0;
		for (l += n_, r += n_; l <= r; l >>= 1, r >>= 1) {
			if ((l & 1) == 1)
				k = Math.max(k, tr[l++]);
			if ((r & 1) == 0)
				k = Math.max(k, tr[r--]);
		}
		return k;
	}
	void update(int i, int k) {
		for (i += n_; i > 0; i >>= 1)
			tr[i] = Math.max(tr[i], k);
	}
	void main() {
		int n = sc.nextInt();
		int d = sc.nextInt();
		long[] aa = new long[n];
		Integer[] ii = new Integer[n];
		for (int i = 0; i < n; i++) {
			aa[i] = sc.nextLong();
			ii[i] = i;
		}
		Arrays.sort(ii, (i, j) -> Long.signum(aa[i] - aa[j]));
		long[] bb = new long[n];
		for (int i = 0; i < n; i++) {
			bb[n_] = aa[ii[i]];
			aa[ii[i]] = i + 1 == n || aa[ii[i + 1]] != aa[ii[i]] ? n_++ : n_;
		}
		tr = new int[n_ * 2];
		int[] dp = new int[n];
		for (int i = 0; i < n; i++) {
			int a = (int) aa[i];
			long b = bb[a] - d;
			int lower, upper;
			lower = -1; upper = a + 1;
			while (upper - lower > 1) {
				int a_ = (lower + upper) / 2;
				if (bb[a_] <= b)
					lower = a_;
				else
					upper = a_;
			}
			int k1 = lower < 0 ? 0 : query(0, lower);
			b = bb[a] + d;
			lower = a - 1; upper = n_;
			while (upper - lower > 1) {
				int a_ = (lower + upper) / 2;
				if (bb[a_] >= b)
					upper = a_;
				else
					lower = a_;
			}
			int k2 = upper == n_ ? 0 : query(upper, n_ - 1);
			update(a, dp[i] = Math.max(k1, k2) + 1);
		}
		int i_ = 0;
		for (int i = 1; i < n; i++)
			if (dp[i_] < dp[i])
				i_ = i;
		int k = dp[i_];
		println(k);
		int[] qq = new int[n]; int cnt = 0;
		qq[cnt++] = i_;
		for (int i = i_ - 1; i >= 0; i--)
			if (dp[i] == k - 1 && Math.abs(bb[(int) aa[i]] - bb[(int) aa[i_]]) >= d) {
				qq[cnt++] = i_ = i;
				k--;
			}
		while (cnt-- > 0)
			print(qq[cnt] + 1 + " ");
		println();
	}
}
