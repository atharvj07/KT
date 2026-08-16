import static java.lang.Double.parseDouble;
import static java.lang.Integer.parseInt;
import static java.lang.Long.parseLong;
import static java.lang.System.exit;
import static java.util.Arrays.fill;

import java.io.*;
import java.util.*;
import java.math.*;
import java.lang.*;
import java.text.*;

public class Main {
	static BufferedReader in;
	static PrintWriter out;
	static StringTokenizer tok;
	
	final static double EPS = 1e-9;
	final static int MOD = 1000000007;
	
	static void solve() throws Exception {
		String s = next();
		int res = 0;
		int cnt = 1;
		for (int i = 0; i < s.length(); i++) {
			if (i+1 < s.length() && s.charAt(i+1) == s.charAt(i)) {
				cnt++;
			} else {
				res += cnt / 5;
				if (cnt % 5 != 0) {
					res++;
				}
				cnt = 1;
			}
		}
		out.println(res);
	}
	
	static long sqr(long x) {
		return x*x;
	}
	
	static int nextInt() throws IOException {
		return parseInt(next());
	}

	static long nextLong() throws IOException {
		return parseLong(next());
	}

	static double nextDouble() throws IOException {
		return parseDouble(next());
	}

	static BigInteger nextBigInteger() throws IOException {
		return new BigInteger(next());
	}
	
	static String next() throws IOException {
		while (tok == null || !tok.hasMoreTokens()) {
			tok = new StringTokenizer(in.readLine());
		}
		return tok.nextToken();
	}

	public static void main(String args[]) {
		try {
			in = new BufferedReader(new InputStreamReader(System.in));
			out = new PrintWriter(new OutputStreamWriter(System.out));
			solve();
			in.close();
			out.close();
		} catch (Throwable e) {
			e.printStackTrace();
			exit(1);
		}
	}
}