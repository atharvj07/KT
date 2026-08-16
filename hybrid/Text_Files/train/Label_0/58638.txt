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
		try {
			if (new File("input.txt").exists())
				System.setIn(new FileInputStream("input.txt"));
		} catch (SecurityException e) {
		}
		new Thread(null, new Runnable() {
			public void run() {
				try {
					new Main().run();
				} catch (Throwable e) {
					e.printStackTrace();
					exit(999);
				}
			}
		}, "1", 1 << 23).start();
	}

	BufferedReader in;
	PrintWriter out;
	StringTokenizer st = new StringTokenizer("");

	private void run() throws IOException {
		in = new BufferedReader(new InputStreamReader(System.in));
		out = new PrintWriter(System.out);

		
		long x = nextLong();
		long y = nextLong();
		long z = nextLong();
		long k = nextLong();
		
		
		long ans = 1;
		
		for (long i = 0; i < x; i++) {
			long l = k - i;
			if (l < 0)
				break;
			long s = l >> 1;
			long c2 = min(y - 1, s);
			long c3 = min(z - 1, s);
			l -= c2 + c3;
			if (c2 < y - 1) {
				c2 = min(y - 1, c2 + l);
			} else {
				c3 = min(z - 1, c3 + l);
			}
			ans = max(ans, (i + 1) * (c2 + 1) * (c3 + 1));
		}
		
		
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
