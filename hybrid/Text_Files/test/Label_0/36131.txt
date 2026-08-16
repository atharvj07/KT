import java.util.*;
import java.io.*;

public class CStupid {
	FastScanner in;
	PrintWriter out;

	double[] A, B;
	int sp = 0;

	double inter(double ai, double bi, double aj, double bj) {
		double x = (bj - bi) / (ai - aj);
		return x;
	}
	
	void add(double a, double b) {
		while (sp >= 2 && inter(A[sp - 2], B[sp - 2], A[sp - 1], B[sp - 1]) >= inter(A[sp - 1], B[sp - 1], a, b)) {
			sp--;
		}
		A[sp] = a;
		B[sp] = b;
		sp++;
	}

	double opt(double x) {
		/*double res = 0;
		for (int i = 0; i < sp; i++) {
			double val = A[i] * x + B[i];
			if (val < res) {
				res = val;
			}
		}
		return res;*/
		if (sp == 0) {
			return 0;
		}
		if (sp == 1) {
			return A[0] * x + B[0];
		}
		if (x < inter(A[0], B[0], A[1], B[1])) {
			return A[0] * x + B[0];
		}
		if (x >= inter(A[sp - 2], B[sp - 2], A[sp - 1], B[sp - 1])) {
			return A[sp - 1] * x + B[sp - 1];
		}
		int l = 0, r = sp - 1;
		while (r - l > 1) {
			int mid = (l + r) / 2;
			double x0 = inter(A[mid], B[mid], A[mid + 1], B[mid + 1]);
			if (x0 <= x) {
				l = mid;
			} else {
				r = mid;
			}
		}
		return A[l + 1] * x + B[l + 1];
	}

	public void solve() throws IOException {
		int n = in.nextInt(), k = in.nextInt();
		double[] a = new double[n];
		for (int i = 0; i < n; i++) {
			a[i] = in.nextDouble();
		}
		double[] sum = new double[n + 1];
		for (int i = 0; i < n; i++) {
			sum[i + 1] = a[i] + sum[i];
		}
		double[] sumSumDivA = new double[n + 1];
		for (int i = 0; i < n; i++) {
			sumSumDivA[i + 1] = sum[i + 1] / a[i] + sumSumDivA[i];
		}
		double[] sumAInv = new double[n + 1];
		for (int i = 0; i < n; i++) {
			sumAInv[i + 1] = 1.0 / a[i] + sumAInv[i];
		}
		double[][] dp = new double[k + 1][n + 1];
		final double inf = Double.POSITIVE_INFINITY;
		Arrays.fill(dp[0], inf);
		dp[0][0] = 0;
		A = new double[n + 1];
		B = new double[n + 1];
		// Ax + b
		for (int i = 1; i <= k; i++) {
			sp = 0;
			for (int j = 1; j <= n; j++) {
				double V = sumSumDivA[j];
				double x = sumAInv[j];
				double fv = opt(x);
				dp[i][j] = V + fv;
				if (dp[i - 1][j] != inf) {
					add(-sum[j], dp[i - 1][j] - sumSumDivA[j] + sum[j] * sumAInv[j]);
				}
			}
		}
		out.println(dp[k][n]);
	}

	public void run() {
		try {
			in = new FastScanner();
			out = new PrintWriter(System.out);

			solve();

			out.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	class FastScanner {
		BufferedReader br;
		StringTokenizer st;

		FastScanner() {
			br = new BufferedReader(new InputStreamReader(System.in));
		}

		String next() {
			while (st == null || !st.hasMoreTokens()) {
				try {
					st = new StringTokenizer(br.readLine());
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
			return st.nextToken();
		}

		int nextInt() {
			return Integer.parseInt(next());
		}

		long nextLong() {
			return Long.parseLong(next());
		}

		double nextDouble() {
			return Double.parseDouble(next());
		}
	}

	public static void main(String[] arg) {
		new CStupid().run();
	}
}