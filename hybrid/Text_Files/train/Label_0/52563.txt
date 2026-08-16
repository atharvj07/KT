import static java.lang.Math.*;
import static java.lang.System.currentTimeMillis;
import static java.lang.System.exit;
import static java.lang.System.arraycopy;
import static java.util.Arrays.sort;
import static java.util.Arrays.binarySearch;
import static java.util.Arrays.fill;
import java.util.*;
import java.io.*;

public class Main {

	public static void main(String[] args) throws IOException {
		new Main().run();
	}

	BufferedReader in;
	PrintWriter out;
	StringTokenizer st = new StringTokenizer("");

	final int maxn = 60;
	final int inf = Integer.MAX_VALUE / 3;

	int n, k;

	int a[][] = new int[maxn][maxn];
	int f[][] = new int[maxn][maxn];
	int d[] = new int[maxn];
	int p[] = new int[maxn];

	void bf() {
		fill(d, inf);
		d[0] = 0;
		fill(p, -1);
		for (int count = 0; count < n; count++)
			for (int i = 0; i < n; i++)
				for (int j = 0; j < n; j++)
					if (a[i][j] != -1) {
						if (a[i][j] > f[i][j]) {
							if (d[j] > d[i]) {
								d[j] = d[i];
								p[j] = i;
							}
						} else if (d[j] > d[i] + 1) {
							d[j] = d[i] + 1;
							p[j] = i;
						}
					}
	}

	private void run() throws IOException {
		// in = new BufferedReader(new FileReader("input.txt"));
		// out = new PrintWriter("output.txt");

		if (new File("input.txt").exists())
			in = new BufferedReader(new FileReader("input.txt"));
		else
			in = new BufferedReader(new InputStreamReader(System.in));
		if (new File("output.txt").exists())
			out = new PrintWriter("output.txt");
		else
			out = new PrintWriter(System.out);

		n = nextInt();
		k = nextInt();
		for (int i = 0; i < n; i++) {
			// fill(a[i], -1);
			for (int j = 0; j < n; j++) {
				a[i][j] = nextInt();
				if (a[i][j] == 0)
					a[i][j] = -1;
			}
		}
		int ans = 0;
		while (true) {
			bf();
//			System.err.println("dist = " + d[n - 1]);
			if (d[n - 1] != 0) {

				int minf = inf;
				for (int pr = n - 1; p[pr] >= 0; pr = p[pr]) {
					// System.err.println(p[pr] + " " + pr);
					if (a[p[pr]][pr] > f[p[pr]][pr])
						minf = min(minf, a[p[pr]][pr] - f[p[pr]][pr]);
				}
				// System.err.println("minf = " + minf);
				if (minf == inf) {
					ans += k / d[n - 1];
					break;
				} else {
					int addf = min(minf, k / d[n - 1]);
					ans += addf;
					if (addf == 0)
						break;
					k -= (addf * d[n - 1]);
					for (int pr = n - 1; p[pr] >= 0; pr = p[pr]) {
						f[p[pr]][pr] += addf;
						f[pr][p[pr]] -= addf;
					}
					// System.err.println("midle = " + addf);
				}
				if (k == 0)
					break;
			} else {
				int addf = inf;
				for (int pr = n - 1; p[pr] >= 0; pr = p[pr]) {
					addf = min(addf, max(0, a[p[pr]][pr] - f[p[pr]][pr]));
//					System.err.println(p[pr] + " " + pr);
				}
				for (int pr = n - 1; p[pr] >= 0; pr = p[pr]) {
					f[p[pr]][pr] += addf;
					f[pr][p[pr]] -= addf;
				}
				ans += addf;
//				System.err.println("clear = " + addf);
			}
		}
		System.err.println(a[0][2]);
		System.err.println(a[2][3]);
		out.println(ans);

		in.close();
		out.close();
	}

	void chk(boolean b) {
		if (b)
			return;
		System.out.println(new Error().getStackTrace()[1]);
		exit(999);
	}

	void deb(String fmt, Object... args) {
		System.out.printf(Locale.US, fmt + "%n", args);
	}

	String nextToken() throws IOException {
		while (!st.hasMoreTokens())
			st = new StringTokenizer(in.readLine());
		return st.nextToken();
	}

	int nextInt() throws IOException {
		return Integer.parseInt(nextToken());
	}

	long nextLong() throws IOException {
		return Long.parseLong(nextToken());
	}

	double nextDouble() throws IOException {
		return Double.parseDouble(nextToken());
	}

	String nextLine() throws IOException {
		st = new StringTokenizer("");
		return in.readLine();
	}

	boolean EOF() throws IOException {
		while (!st.hasMoreTokens()) {
			String s = in.readLine();
			if (s == null)
				return true;
			st = new StringTokenizer(s);
		}
		return false;
	}
}
