import java.io.*;
import java.util.*;

public class Main {

	void submit() {
		int r = nextInt();
		int c = nextInt();
		int n = nextInt();

		int[] allX = new int[2 * n + 2];
		int[] allY = new int[2 * n + 2];

		int[] xb = new int[n];
		int[] yb = new int[n];
		for (int i = 0; i < n; i++) {
			xb[i] = nextInt();
			yb[i] = nextInt();
			allX[2 * i] = xb[i];
			allX[2 * i + 1] = xb[i] + 1;
			allY[2 * i] = yb[i];
			allY[2 * i + 1] = yb[i] + 1;
		}
		allX[2 * n] = 0;
		allX[2 * n + 1] = r;
		allY[2 * n] = 0;
		allY[2 * n + 1] = c;

		allX = unique(allX);
		allY = unique(allY);

		int tot = (int) (((long) r * c - n) % P);

		r = allX.length - 1;
		c = allY.length - 1;

		boolean[][] occ = new boolean[r][c];
		for (int i = 0; i < n; i++) {
			int cx = Arrays.binarySearch(allX, xb[i]);
			int cy = Arrays.binarySearch(allY, yb[i]);
			occ[cx][cy] = true;
		}

		int ans = (go(occ, allX, tot, allY[c] - allY[0]) + go(transpose(occ),
				allY, tot, allX[r] - allX[0])) % P;

		int[][] d = new int[r][c];
		int[] que = new int[2 * r * c];

		int[][] cellSz = new int[r][c];
		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++) {
				cellSz[i][j] = (int) ((long) (allX[i + 1] - allX[i])
						* (allY[j + 1] - allY[j]) % P);
			}
		}

		for (int x0 = 0; x0 < r; x0++) {
			for (int y0 = 0; y0 < c; y0++) {
				if (occ[x0][y0]) {
					continue;
				}
				for (int[] row : d) {
					Arrays.fill(row, INF);
				}
				d[x0][y0] = 0;
				int qh = 0, qt = 0;
				que[qt++] = x0;
				que[qt++] = y0;

				while (qh < qt) {
					int x = que[qh++];
					int y = que[qh++];
					if (x0 * c + y0 < x * c + y) {
						
//						System.err.println(x0 + " " + y0 + " " + x + " " + y + " " + d[x][y]);
						
						ans += (int) ((long) cellSz[x0][y0] * cellSz[x][y] % P
								* d[x][y] % P);
						if (ans >= P) {
							ans -= P;
						}
					}

					for (int dir = 0; dir < 4; dir++) {
						int nx = x + DX[dir];
						int ny = y + DY[dir];
						if (nx >= 0 && nx < r && ny >= 0 && ny < c
								&& !occ[nx][ny] && d[nx][ny] > d[x][y] + 1) {
							d[nx][ny] = d[x][y] + 1;
							que[qt++] = nx;
							que[qt++] = ny;
						}
					}
				}
			}
		}

		out.println(ans);
	}

	static final int[] DX = { -1, 0, 1, 0 };
	static final int[] DY = { 0, -1, 0, 1 };

	static final int INF = Integer.MAX_VALUE;

	boolean[][] transpose(boolean[][] f) {
		boolean[][] g = new boolean[f[0].length][f.length];
		for (int i = 0; i < f.length; i++) {
			for (int j = 0; j < f[i].length; j++) {
				g[j][i] = f[i][j];
			}
		}
		return g;
	}

	int go(boolean[][] occ, int[] allX, int tot, int width) {
		int top = 0;
		int btm = tot;
		int ret = 0;
		for (int i = 0; i < occ.length; i++) {
			int blacks = 0;
			for (int j = 0; j < occ[i].length; j++) {
				blacks += occ[i][j] ? 1 : 0;
			}
			if (blacks > 0) {
				int delta = width - blacks;
				top += delta;
				if (top >= P) {
					top -= P;
				}

				btm -= delta;
				if (btm < 0) {
					btm += P;
				}
				continue;
			}
			for (int row = 1; row < allX[i + 1] - allX[i]; row++) {
				top += width;
				if (top >= P) {
					top -= P;
				}

				btm -= width;
				if (btm < 0) {
					btm += P;
				}

				ret += (int) ((long) top * btm % P);
				if (ret >= P) {
					ret -= P;
				}
			}
			top += width;
			if (top >= P) {
				top -= P;
			}

			btm -= width;
			if (btm < 0) {
				btm += P;
			}
		}
		return ret;
	}

	static final int P = 1_000_000_007;

	int[] unique(int[] a) {
		Arrays.sort(a);
		int sz = 1;
		for (int i = 1; i < a.length; i++) {
			if (a[i] != a[sz - 1]) {
				a[sz++] = a[i];
			}
		}
		return Arrays.copyOf(a, sz);
	}

	void preCalc() {

	}

	void stress() {

	}

	void test() {

	}

	Main() throws IOException {
		br = new BufferedReader(new InputStreamReader(System.in));
		out = new PrintWriter(System.out);
		preCalc();
		submit();
		// stress();
		// test();
		out.close();
	}

	static final Random rng = new Random();

	static int rand(int l, int r) {
		return l + rng.nextInt(r - l + 1);
	}

	public static void main(String[] args) throws IOException {
		new Main();
	}

	BufferedReader br;
	PrintWriter out;
	StringTokenizer st;

	String nextToken() {
		while (st == null || !st.hasMoreTokens()) {
			try {
				st = new StringTokenizer(br.readLine());
			} catch (IOException e) {
				throw new RuntimeException(e);
			}
		}
		return st.nextToken();
	}

	String nextString() {
		try {
			return br.readLine();
		} catch (IOException e) {
			throw new RuntimeException(e);
		}
	}

	int nextInt() {
		return Integer.parseInt(nextToken());
	}

	long nextLong() {
		return Long.parseLong(nextToken());
	}

	double nextDouble() {
		return Double.parseDouble(nextToken());
	}
}
