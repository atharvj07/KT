import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.io.Reader;

public class Main {
	static FastScanner sc = new FastScanner();

	public static void main(String[] args) throws Exception {
		PrintWriter writer = new PrintWriter(System.out);
		while (true) {
			int R = sc.nextInt();
			if (R == 0) break;
			int C = sc.nextInt();
			int Q = sc.nextInt();
			int[][] G = new int[R][C];
			int[][] tr = new int[C][R];
			for (int i = 0; i < R; ++i) {
				for (int j = 0; j < C; ++j) {
					tr[j][i] = G[i][j] = sc.nextInt();
				}
			}
			int ru = 1;
			while (ru < C * 2) {
				ru *= 2;
			}
			int[][] row = new int[R][ru];
			for (int i = 0; i < R; ++i) {
				build(G[i], row[i]);
			}
			int cu = 1;
			while (cu < R * 2) {
				cu *= 2;
			}
			int[][] col = new int[C][cu];
			for (int i = 0; i < C; ++i) {
				build(tr[i], col[i]);
			}
			for (int i = 0; i < Q; ++i) {
				int R1 = sc.nextInt();
				int C1 = sc.nextInt();
				int R2 = sc.nextInt();
				int C2 = sc.nextInt();
				int ans = Integer.MAX_VALUE;
				if (R2 - R1 < C2 - C1) {
					for (int j = R1; j <= R2; ++j) {
						ans = Math.min(ans, get(row[j], 0, C1, C2 + 1, 0, ru / 2));
					}
				} else {
					for (int j = C1; j <= C2; ++j) {
						ans = Math.min(ans, get(col[j], 0, R1, R2 + 1, 0, cu / 2));
					}
				}
				writer.println(ans);
			}
		}
		writer.flush();
	}

	static void build(int[] in, int[] out) {
		for (int i = 0; i < in.length; ++i) {
			out[out.length / 2 - 1 + i] = in[i];
		}
		for (int i = in.length; i < out.length / 2; ++i) {
			out[out.length / 2 - 1 + i] = Integer.MAX_VALUE;
		}
		for (int i = out.length / 2 - 2; i >= 0; --i) {
			out[i] = Math.min(out[i * 2 + 1], out[i * 2 + 2]);
		}
	}

	static int get(int[] tree, int cur, int f, int e, int left, int right) {
		if (right <= f || e <= left) return Integer.MAX_VALUE;
		if (f <= left && right <= e) return tree[cur];
		int mid = (left + right + 1) / 2;
		return Math.min(get(tree, cur * 2 + 1, f, e, left, mid), get(tree, cur * 2 + 2, f, e, mid, right));
	}

	static class FastScanner {
		Reader input;

		FastScanner() {
			this(System.in);
		}

		FastScanner(InputStream stream) {
			this.input = new BufferedReader(new InputStreamReader(stream));
		}

		int nextInt() throws IOException {
			int sign = 1;
			int b = input.read();
			while ((b < '0' || '9' < b) && b != '-' && b != '+') {
				b = input.read();
			}
			if (b == '-') {
				sign = -1;
				b = input.read();
			} else if (b == '+') {
				b = input.read();
			}
			int ret = b - '0';
			while (true) {
				b = input.read();
				if (b < '0' || '9' < b) return ret * sign;
				ret *= 10;
				ret += b - '0';
			}
		}
	}
}