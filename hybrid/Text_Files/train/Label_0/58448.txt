import java.util.Scanner;

public class Main {

	static Scanner sc = new Scanner(System.in);
	static long[] tree = new long[400000];

	static long max(int pos, int l, int r, int min, int max) {
		long ret = 0;
		if (l == min && r == max) return tree[pos];
		int m = (l + r) / 2;
		if (min < m) {
			ret = Math.max(ret, max(pos * 2 + 1, l, m, min, Math.min(m, max)));
		}
		if (m < max) {
			ret = Math.max(ret, max(pos * 2 + 2, m, r, Math.max(m, min), max));
		}
		return ret;
	}

	static void set(int pos, int l, int r, int index, long v) {
		tree[pos] = Math.max(tree[pos], v);
		if (l == r - 1) return;
		int m = (l + r) / 2;
		if (index < m) {
			set(pos * 2 + 1, l, m, index, v);
		} else {
			set(pos * 2 + 2, m, r, index, v);
		}
	}

	public static void main(String[] args) {
		int N = sc.nextInt();
		int size = 1;
		while (size <= N) {
			size *= 2;
		}
		for (int i = 0; i < N; ++i) {
			int x = sc.nextInt();
			long max = max(0, 0, size, 0, x);
			set(0, 0, size, x, max + x);
		}
		System.out.println((long) N * (N + 1) / 2 - tree[0]);
	}
}