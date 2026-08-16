
import java.util.*;

public class Main {
	public static void main(String[] args) {
		new Main().run();
	}

	void run() {
		solver();
	}

	int N;
	int Q;
	long A, B, C;
	int[] row;
	int[] column;
	int[][] back = new int[][] { { 1, 0 }, { 0, 1 } };
	final int[][] RR = new int[][] { { 0, -1 }, { 1, 0 } };
	final int[][] RL = new int[][] { { 0, 1 }, { -1, 0 } };
	final int[][] RH = new int[][] { { 1, 0 }, { 0, -1 } };
	final int[][] RV = new int[][] { { -1, 0 }, { 0, 1 } };
	HashMap<List<Integer>, Long> map = new HashMap<>();
	final long MODULO = 1_000_000_000 + 7;

	void solver() {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		Q = sc.nextInt();
		A = sc.nextLong();
		B = sc.nextLong();
		C = sc.nextLong();
		row = new int[N + 1];
		column = new int[N + 1];
		for (int i = 0; i <= N; ++i) {
			row[i] = i;
			column[i] = i;
		}
		int D = sc.nextInt();
		int E = sc.nextInt();
		int F = sc.nextInt();
		int G = sc.nextInt();
		for (int q = 0; q < Q; ++q) {
			String s = sc.next();
			if (s.equals("WR")) {
				int r = sc.nextInt();
				int c = sc.nextInt();
				long v = sc.nextLong();
				int[][] pos = get(r, c);
				c = pos[0][0];
				r = pos[1][0];
				map.put(Arrays.asList(row[r], column[c]), v);
			} else if (s.equals("CP")) {
				int r1 = sc.nextInt();
				int c1 = sc.nextInt();
				int r2 = sc.nextInt();
				int c2 = sc.nextInt();
				long v = getValue(r1, c1);
				int[][] pos = get(r2, c2);
				int r = pos[1][0];
				int c = pos[0][0];
				map.put(Arrays.asList(row[r], column[c]), v);
			} else if (s.equals("RL")) {
				back = mul(back, RR);
			} else if (s.equals("RR")) {
				back = mul(back, RL);
			} else if (s.equals("RH")) {
				back = mul(back, RH);
			} else if (s.equals("RV")) {
				back = mul(back, RV);
			} else if (s.equals("SR")) {
				int r1 = sc.nextInt();
				int r2 = sc.nextInt();
				int[][] v1 = get(r1, 0);
				int[][] v2 = get(r2, 0);
				swap(v1, v2);
			} else if (s.equals("SC")) {
				int c1 = sc.nextInt();
				int c2 = sc.nextInt();
				int[][] v1 = get(0, c1);
				int[][] v2 = get(0, c2);
				swap(v1, v2);
			}
		}

		long h = 314159265;
		for (int r = D; r <= E; ++r) {
			for (int c = F; c <= G; ++c) {
				h = (31 * h + getValue(r, c)) % MODULO;
			}
		}
		System.out.println(h);
		sc.close();
	}

	long getValue(int r, int c) {
		int[][] pos = get(r, c);
		int rp = pos[1][0];
		int cp = pos[0][0];
		if (map.containsKey(Arrays.asList(row[rp], column[cp]))) {
			return map.get(Arrays.asList(row[rp], column[cp])) % MODULO;
		} else {
			return init(row[rp], column[cp]);
		}
	}

	int[][] get(int r, int c) {
		int[][] v = new int[][] { { c }, { r } };
		v = mul(back, v);
		if (v[0][0] < 0)
			v[0][0] += N + 1;
		if (v[1][0] < 0)
			v[1][0] += N + 1;
		return v;
	}

	long init(long r, long c) {
		return (r * A + c * B) % C;
	}

	void swap(int[][] v1, int[][] v2) {
		int c1 = v1[0][0];
		int c2 = v2[0][0];
		int r1 = v1[1][0];
		int r2 = v2[1][0];
		int d = row[r1];
		row[r1] = row[r2];
		row[r2] = d;
		d = column[c1];
		column[c1] = column[c2];
		column[c2] = d;
	}

	int[][] mul(int[][] a, int[][] b) {
		assert a[0].length == b.length;
		int n = a[0].length;
		int[][] ret = new int[a.length][b[0].length];
		for (int i = 0; i < a.length; ++i) {
			for (int j = 0; j < b[0].length; ++j) {
				for (int k = 0; k < n; ++k) {
					ret[i][j] += a[i][k] * b[k][j];
				}
			}
		}
		return ret;
	}

	void tr(Object... objects) {
		System.out.println(Arrays.deepToString(objects));
	}
}