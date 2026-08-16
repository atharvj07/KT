
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.Scanner;

class Main {

	@SuppressWarnings("unchecked")
	public void run() {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		long[] x = new long[n];
		long[] y = new long[n];
		char[] d = new char[n];
		for (int i = 0; i < n; ++i) {
			x[i] = sc.nextLong();
			y[i] = sc.nextLong();
			d[i] = sc.next().charAt(0);
		}
		shrink(x);
		shrink(y);
		ArrayList<Long>[] list1 = new ArrayList[3000];
		ArrayList<Long>[] list2 = new ArrayList[3000];
		for (int i = 0; i < list1.length; ++i) {
			list1[i] = new ArrayList();
		}
		for (int i = 0; i < list2.length; ++i) {
			list2[i] = new ArrayList();
		}
		for (int i = 0; i < n; ++i) {
			list1[(int) x[i]].add(y[i] << 32 | i);
			list2[(int) y[i]].add(x[i] << 32 | i);
		}
		int[] up = new int[n];
		int[] down = new int[n];
		int[] left = new int[n];
		int[] right = new int[n];
		Arrays.fill(up, -1);
		Arrays.fill(down, -1);
		Arrays.fill(left, -1);
		Arrays.fill(right, -1);
		for (int i = 0; i < 3000; ++i) {
			Collections.sort(list1[i]);
			Collections.sort(list2[i]);
			for (int j = 0; j + 1 < list1[i].size(); ++j) {
				int u = (int) (list1[i].get(j) & ((1L << 32) - 1));
				int v = (int) (list1[i].get(j + 1) & ((1L << 32) - 1));
				up[u] = v;
				down[v] = u;
			}
			for (int j = 0; j + 1 < list2[i].size(); ++j) {
				int u = (int) (list2[i].get(j) & ((1L << 32) - 1));
				int v = (int) (list2[i].get(j + 1) & ((1L << 32) - 1));
				right[u] = v;
				left[v] = u;
			}
		}
		int ans = 0;
		for (int i = 0; i < n; ++i) {
			int[] UP = Arrays.copyOf(up, up.length);
			int[] DOWN = Arrays.copyOf(down, down.length);
			int[] RIGHT = Arrays.copyOf(right, right.length);
			int[] LEFT = Arrays.copyOf(left, left.length);
			int cur = i;
			int pre = -1;
			int tmp = 0;
			while (true) {
				pre = cur;
				if (d[cur] == 'v') {
					cur = UP[cur];
				} else if (d[cur] == '^') {
					cur = DOWN[cur];
				} else if (d[cur] == '>') {
					cur = RIGHT[cur];
				} else if (d[cur] == '<') {
					cur = LEFT[cur];
				} else {
					throw new AssertionError();
				}
				++tmp;
				if (cur == -1)
					break;
				else {
					erase(pre, UP, DOWN, RIGHT, LEFT);
				}
			}
			ans = Math.max(ans, tmp);
		}
		System.out.println(ans);
	}

	void erase(int id, int[] up, int[] down, int[] right, int[] left) {
		if (id == -1)
			return;
		if (down[id] != -1)
			up[down[id]] = up[id];
		if (up[id] != -1)
			down[up[id]] = down[id];
		if (left[id] != -1)
			right[left[id]] = right[id];
		if (right[id] != -1)
			left[right[id]] = left[id];
		up[id] = -1;
		down[id] = -1;
		right[id] = -1;
		left[id] = -1;
	}

	void shrink(long[] a) {
		long[][] b = new long[a.length][2];
		for (int i = 0; i < a.length; ++i) {
			b[i][0] = a[i];
			b[i][1] = i;
		}
		Arrays.sort(b, new Comparator<long[]>() {
			@Override
			public int compare(long[] arg0, long[] arg1) {
				return Long.compare(arg0[0], arg1[0]);
			}
		});
		int p = 0;
		for (int i = 0; i < b.length; ++i) {
			if (i - 1 >= 0 && b[i][0] != b[i - 1][0]) {
				++p;
			}
			a[(int) b[i][1]] = p;
		}
	}

	void tr(Object... objects) {
		System.out.println(Arrays.deepToString(objects));
	}

	public static void main(String[] args) {
		new Main().run();
	}
}

