import static java.lang.Integer.parseInt;
import static java.lang.Long.parseLong;
import static java.lang.System.exit;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;

public class Main {

	static void solve() throws Exception {
		int n = scanInt();
		if ((n & -n) == n) {
			out.print("No");
			return;
		}
		out.println("Yes");
		int m = n + (n & 1) - 1;
		for (int i = 2; i <= m; i++) {
			out.println("1 " + i);
			out.println(i + " " + (n + (i ^ 1)));
		}
		out.println((n + 1) + " " + (n + 3));
		if (n != m) {
			int x = Integer.lowestOneBit(n) + 1, y = n - x + 1;
			out.println(n + " " + x);
			out.println((2 * n) + " " + y);
		}
	}

	static int scanInt() throws IOException {
		return parseInt(scanString());
	}

	static long scanLong() throws IOException {
		return parseLong(scanString());
	}

	static String scanString() throws IOException {
		while (tok == null || !tok.hasMoreTokens()) {
			tok = new StringTokenizer(in.readLine());
		}
		return tok.nextToken();
	}

	static BufferedReader in;
	static PrintWriter out;
	static StringTokenizer tok;

	public static void main(String[] args) {
		try {
			in = new BufferedReader(new InputStreamReader(System.in));
			out = new PrintWriter(System.out);
			solve();
			in.close();
			out.close();
		} catch (Throwable e) {
			e.printStackTrace();
			exit(1);
		}
	}
}