import java.util.*;

public class Main {
	// BIT definition
	public static class BIT {
		int sz;
		long[] bit;
		BIT(int sz) {
			this.sz = sz;
			this.bit = new long[sz];
		}
		void add(int i, long x) {
			while(i < sz) {
				bit[i] += x;
				i |= i + 1;
			}
		}
		// [0, r)
		long sum(int r) {
			long ret = 0;
			--r;
			while(r >= 0) {
				ret += bit[r];
				r = (r & (r + 1)) - 1;
			}
			return ret;
		}
		// [l, r)
		long sum(int l, int r) {
			return sum(r) - sum(l);
		}
	}
	public static void main(String[] args) {
		// input
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] a = new int[n];
		for(int i = 0; i < n; ++i) {
			a[i] = sc.nextInt();
		}

		final int MAX = 100010;
		// ascend inversion
		BIT ascend = new BIT(MAX);
		long[] l = new long[n];
		for(int i = 0; i < n; ++i) {
			l[i] = ascend.sum(a[i] + 1, MAX);
			ascend.add(a[i], 1);
		}
		// descend inversion
		BIT descend = new BIT(MAX);
		long[] r = new long[n];
		for(int i = n - 1; i >= 0; --i) {
			r[i] = descend.sum(a[i] + 1, MAX);
			descend.add(a[i], 1);
		}
		
		long ans = 0;
		for(int i = 0; i < n; ++i) {
			ans += Math.min(l[i], r[i]);
		}
		System.out.println(ans);
	}
}
