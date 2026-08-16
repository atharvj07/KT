import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.NoSuchElementException;

public class Main {
	int n, m, k;
	double[][] dp;

	public void solve() {
		while (true) {
			n = nextInt();
			m = nextInt();
			k = nextInt();

			if (n + m + k == 0)
				break;

			dp = new double[n + 2][n * m + 1];
			dp[0][0] = 1;
			for (int i = 0; i < n; i++) {
				for (int j = 0; j <= n * m; j++) {
					for(int l = 1;l <= m;l++){
						if(j + l > n * m)
							continue;
						dp[i + 1][j + l] += dp[i][j] / m;
					}
				}
			}
			for(int i = 0;i <= n * m;i++){
				int j = Math.max(1, i - k);
				dp[n + 1][j] += dp[n][i];
			}
			double ans = 0.0;
			for(int i = 0;i < n * m + 1;i++){
				ans += i * dp[n + 1][i];
			}
			out.println(ans);
		}
	}

	public static void main(String[] args) {
		out.flush();
		new Main().solve();
		out.close();
	}

	/* Input */
	private static final InputStream in = System.in;
	private static final PrintWriter out = new PrintWriter(System.out);
	private final byte[] buffer = new byte[2048];
	private int p = 0;
	private int buflen = 0;

	private boolean hasNextByte() {
		if (p < buflen)
			return true;
		p = 0;
		try {
			buflen = in.read(buffer);
		} catch (IOException e) {
			e.printStackTrace();
		}
		if (buflen <= 0)
			return false;
		return true;
	}

	public boolean hasNext() {
		while (hasNextByte() && !isPrint(buffer[p])) {
			p++;
		}
		return hasNextByte();
	}

	private boolean isPrint(int ch) {
		if (ch >= '!' && ch <= '~')
			return true;
		return false;
	}

	private int nextByte() {
		if (!hasNextByte())
			return -1;
		return buffer[p++];
	}

	public String next() {
		if (!hasNext())
			throw new NoSuchElementException();
		StringBuilder sb = new StringBuilder();
		int b = -1;
		while (isPrint((b = nextByte()))) {
			sb.appendCodePoint(b);
		}
		return sb.toString();
	}

	public int nextInt() {
		return Integer.parseInt(next());
	}

	public long nextLong() {
		return Long.parseLong(next());
	}

	public double nextDouble() {
		return Double.parseDouble(next());
	}
}