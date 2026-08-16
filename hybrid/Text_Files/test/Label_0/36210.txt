import java.awt.geom.Line2D;
import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Arrays;

public class Main{
	static InputStream is;
	static PrintWriter out;
	static String INPUT = "";

	public static void main(String[] args) throws Exception {
		new Main().run();
	}

	double INF = 10000;

	void solver() {
		while (true) {
			int w = ni();
			int n = ni();
			if(w==0&&n==0)break;
			double[][][] polygon = new double[n + 2][][];
			int[] m = new int[n + 2];
			for (int i = 0; i < n; i++) {
				m[i] = ni();
				polygon[i] = new double[m[i]][];
				for (int j = 0; j < m[i]; j++) {
					polygon[i][j] = new double[] { nd(), nd() };
				}
			}
			polygon[n] = new double[][] { { 0, 0 }, { 0, INF } };
			polygon[n + 1] = new double[][] { { w, 0 }, { w, INF } };
			m[n] = 2;
			m[n + 1] = 2;
			double[][] dis = new double[n + 2][n + 2];
			for (int i = 0; i < n + 2; i++) {
				for (int j = 0; j < n + 2; j++) {
					if (i != j)
						dis[i][j] = INF;
				}
			}
			for (int i = 0; i < n + 2; i++) {
				for (int j = i + 1; j < n + 2; j++) {
					double d = INF;
					for (int k = 0; k < m[i]; k++) {
						for (int l = 0; l < m[j]; l++) {
							d = Math.min(d, segDist(polygon[i][k], polygon[i][(k + 1) % m[i]], polygon[j][l],
									polygon[j][(l + 1) % m[j]]));
						}
					}
					dis[i][j] = dis[j][i] = Math.min(d, dis[i][j]);
				}
			}
			for (int i = 0; i < n + 2; i++) {
				for (int j = 0; j < n + 2; j++) {
					for (int k = 0; k < n + 2; k++) {
						dis[j][k] = Math.min(dis[j][k], dis[j][i] + dis[i][k]);
					}
				}
			}
			out.println(dis[n][n + 1]);
		}
	}

	double segDist(double[] v1, double[] v2, double[] v3, double[] v4) {
		double d = INF;
		d = Math.min(d, Line2D.ptSegDist(v1[0], v1[1], v2[0], v2[1], v3[0], v3[1]));
		d = Math.min(d, Line2D.ptSegDist(v1[0], v1[1], v2[0], v2[1], v4[0], v4[1]));
		d = Math.min(d, Line2D.ptSegDist(v3[0], v3[1], v4[0], v4[1], v1[0], v1[1]));
		d = Math.min(d, Line2D.ptSegDist(v3[0], v3[1], v4[0], v4[1], v2[0], v2[1]));
		return d;
	}

	void run() {
		is = INPUT.isEmpty() ? System.in : new ByteArrayInputStream(INPUT.getBytes());
		out = new PrintWriter(System.out);
		solver();
		out.flush();

	}

	static long nl() {
		try {
			long num = 0;
			boolean minus = false;
			while ((num = is.read()) != -1 && !((num >= '0' && num <= '9') || num == '-'))
				;
			if (num == '-') {
				num = 0;
				minus = true;
			} else {
				num -= '0';
			}

			while (true) {
				int b = is.read();
				if (b >= '0' && b <= '9') {
					num = num * 10 + (b - '0');
				} else {
					return minus ? -num : num;
				}
			}
		} catch (IOException e) {
		}
		return -1;
	}

	static char nc() {
		try {
			int b = skip();
			if (b == -1)
				return 0;
			return (char) b;
		} catch (IOException e) {
		}
		return 0;
	}

	static double nd() {
		try {
			return Double.parseDouble(ns());
		} catch (Exception e) {
		}
		return 0;
	}

	static String ns() {
		try {
			int b = skip();
			StringBuilder sb = new StringBuilder();
			if (b == -1)
				return "";
			sb.append((char) b);
			while (true) {
				b = is.read();
				if (b == -1)
					return sb.toString();
				if (b <= ' ')
					return sb.toString();
				sb.append((char) b);
			}
		} catch (IOException e) {
		}
		return "";
	}

	public static char[] ns(int n) {
		char[] buf = new char[n];
		try {
			int b = skip(), p = 0;
			if (b == -1)
				return null;
			buf[p++] = (char) b;
			while (p < n) {
				b = is.read();
				if (b == -1 || b <= ' ')
					break;
				buf[p++] = (char) b;
			}
			return Arrays.copyOf(buf, p);
		} catch (IOException e) {
		}
		return null;
	}

	public static byte[] nse(int n) {
		byte[] buf = new byte[n];
		try {
			int b = skip();
			if (b == -1)
				return null;
			is.read(buf);
			return buf;
		} catch (IOException e) {
		}
		return null;
	}

	static int skip() throws IOException {
		int b;
		while ((b = is.read()) != -1 && !(b >= 33 && b <= 126))
			;
		return b;
	}

	static boolean eof() {
		try {
			is.mark(1000);
			int b = skip();
			is.reset();
			return b == -1;
		} catch (IOException e) {
			return true;
		}
	}

	static int ni() {
		try {
			int num = 0;
			boolean minus = false;
			while ((num = is.read()) != -1 && !((num >= '0' && num <= '9') || num == '-'))
				;
			if (num == '-') {
				num = 0;
				minus = true;
			} else {
				num -= '0';
			}

			while (true) {
				int b = is.read();
				if (b >= '0' && b <= '9') {
					num = num * 10 + (b - '0');
				} else {
					return minus ? -num : num;
				}
			}
		} catch (IOException e) {
		}
		return -1;
	}

	static void tr(Object... o) {
		System.out.println(Arrays.deepToString(o));
	}
}