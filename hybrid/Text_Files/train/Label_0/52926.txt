import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.Locale;
import java.util.StringTokenizer;

@SuppressWarnings("unchecked")
public class Main {
	private static final String TASKNAME = "c";

	private void solve() throws Exception {
		long ax = nextLong();
		long ay = nextLong();
		long bbx = nextLong();
		long bby = nextLong();
		long cx = nextLong();
		long cy = nextLong();
		boolean ans = false;
		for (int i = 0; i < 4; ++i) {
			long bx = -(bbx - ax);
			long by = -(bby - ay);
			long d = cx * cx + cy * cy;
			if (d == 0) {
				ans |= bx == 0 && by == 0;
			} else {
				ans |= (cy * by + cx * bx) % d == 0 && (cx * by - cy * bx) % d == 0;
			}
			long t = ax;
			ax = ay;
			ay = t;
			ax *= -1;
		}
		println(ans ? "YES" : "NO");
	}

	private BufferedReader reader;
	private PrintWriter writer;
	private StringTokenizer tokenizer;

	private void run() {
		try {
			reader = new BufferedReader(new InputStreamReader(System.in));
			writer = new PrintWriter(System.out);
//			reader = new BufferedReader(new FileReader(TASKNAME + ".in"));
//			writer = new PrintWriter(new File(TASKNAME + ".out"));

			solve();

			reader.close();
			writer.close();
		} catch (Throwable e) {
			throw new AssertionError(e);
		}
	}

	private void print(final Object o) {
		writer.print(o);
	}

	private void println(final Object o) {
		writer.println(o);
	}

	private void printf(final String format, final Object... o) {
		writer.printf(format, o);
	}

	private double nextDouble() throws IOException {
		return Double.parseDouble(nextToken());
	}

	private int nextInt() throws IOException {
		return Integer.parseInt(nextToken());
	}

	private long nextLong() throws IOException {
		return Long.parseLong(nextToken());
	}

	private String nextToken() throws IOException {
		while (tokenizer == null || !tokenizer.hasMoreTokens()) {
			tokenizer = new StringTokenizer(reader.readLine());
		}
		return tokenizer.nextToken();
	}

	public static void main(String[] args) {
		final long startTime = System.currentTimeMillis();
		Locale.setDefault(Locale.US);
		new Main().run();
		System.err.printf("%.3f\n", (System.currentTimeMillis() - startTime) * 0.001);
	}
}
