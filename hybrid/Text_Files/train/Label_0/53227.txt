import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

class Main {
	static int n, m;
	static long[] a;
	static int[] b;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		m = sc.nextInt();
		a = new long[m + 1];
		b = new int[m];
		for (int i = 0; i < m + 1; ++i) {
			a[i] = sc.nextLong();
		}
		for (int i = 0; i < m; ++i) {
			b[i] = sc.nextInt();
		}
		long[] ret = dfs(0, 1 << n, 0);
		System.out.println(ret[0]);
	}

	static long[] dfs(int l, int r, int depth) {
		int lIdx = binarySearch(a, l);
		int rIdx = lIdx + 1;
		if (a[lIdx] <= l && r <= a[rIdx]) {
			long[] ret = new long[n + 1];
			if (b[lIdx] > depth) {
				Arrays.fill(ret, (1L << (n - depth)) - (1L << (b[lIdx] - 1 - depth)));
			} else {
				Arrays.fill(ret, 1L << (n - depth));
				ret[b[lIdx]] -= 1;
			}
			return ret;
		} else {
			long[] lDp = dfs(l, (l + r) / 2, depth + 1);
			long[] rDp = dfs((l + r) / 2, r, depth + 1);
			long[] ret = new long[n + 1];
			Arrays.fill(ret, Long.MAX_VALUE / 16);
			for (int i = 0; i <= depth; ++i) {
				ret[i] = Math.min(lDp[depth + 1] + rDp[i], lDp[i] + rDp[depth + 1]);
			}
			return ret;
		}
	}

	// key??\?????????????????????????????????
	static int binarySearch(long[] arr, long key) {
		int left = 0;
		int right = arr.length;
		while (right - left > 1) {
			int middle = (left + right) / 2;
			if (arr[middle] <= key)
				left = middle;
			else
				right = middle;
		}
		return left;
	}

	static void tr(Object... objects) {
		System.out.println(Arrays.deepToString(objects));
	}
}