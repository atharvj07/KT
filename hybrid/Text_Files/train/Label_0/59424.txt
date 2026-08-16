import static java.lang.Integer.parseInt;
import static java.lang.Long.parseLong;
import static java.lang.Math.max;
import static java.lang.Math.min;
import static java.lang.System.exit;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;

public class Main {

	static void solve() throws Exception {
		int n = scanInt();
		int ca = 0, ans = 0, ansInc = 1, ansInc2 = 1;
		for (int i = 0; i < n; i++) {
			int na = scanInt();
			if (na > ca) {
				ansInc2 = max(ansInc2, ansInc + na - ca);
			} else {
				ansInc2 = min(max(ansInc, ansInc2 - (ca - na)), na + 1);
				ansInc -= ca - na;
				if (ansInc <= 0) {
					++ans;
					ansInc = ansInc2;
					ansInc2 = na + 1;
				}
			}
			ca = na;
		}
		if (ansInc <= ca) {
			++ans;
		}
		out.print(ans);
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