import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class C {
	MyScanner sc = new MyScanner();
	Scanner sc2 = new Scanner(System.in);
	final int MOD = 1000000007;
	int[] dx = { 1, 0, 0, -1 };
	int[] dy = { 0, 1, -1, 0 };

	ArrayList<int[]> list;
	int n, k, d;

	void run() {
		n = sc.nextInt();
		k = sc.nextInt();
		d = sc.nextInt();
		list = new ArrayList<int[]>();
		int tmp = 1;
		boolean ok = false;
		for (int i = 0; i < d; i++) {
			tmp *= k;
			if (tmp >= n) {
				ok = true;
				break;
			}
		}
		if (!ok) {
			System.out.println(-1);
			return;
		}
		gen(0, new int[d]);
		StringBuilder out = new StringBuilder();
		for (int i = 0; i < d; i++) {
			for (int j = 0; j < n; j++) {
				out.append(list.get(j)[i] + " ");
			}
			out.append("\n");
		}
		System.out.print(out);
	}

	void gen(int depth, int a[]) {
		if (depth == d) {
			int[] add = a.clone();
			list.add(add);
			return;
		}

		for (int i = 1; i <= k; i++) {
			if (list.size() >= n) {
				return;
			}
			a[depth] = i;
			gen(depth + 1, a);
		}
	}

	public static void main(String[] args) {
		new C().run();
	}

	void debug(Object... o) {
		System.out.println(Arrays.deepToString(o));
	}

	void debug2(int[][] array) {
		for (int i = 0; i < array.length; i++) {
			for (int j = 0; j < array[i].length; j++) {
				System.out.print(array[i][j]);
			}
			System.out.println();
		}
	}

	class MyScanner {
		int nextInt() {
			try {
				int c = System.in.read();
				while (c != '-' && (c < '0' || '9' < c))
					c = System.in.read();
				if (c == '-')
					return -nextInt();
				int res = 0;
				do {
					res *= 10;
					res += c - '0';
					c = System.in.read();
				} while ('0' <= c && c <= '9');
				return res;
			} catch (Exception e) {
				return -1;
			}
		}

		double nextDouble() {
			return Double.parseDouble(next());
		}

		String next() {
			try {
				StringBuilder res = new StringBuilder("");
				int c = System.in.read();
				while (Character.isWhitespace(c))
					c = System.in.read();
				do {
					res.append((char) c);
				} while (!Character.isWhitespace(c = System.in.read()));
				return res.toString();
			} catch (Exception e) {
				return null;
			}
		}
	}
}
