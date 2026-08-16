
import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Arrays;

public class Main {
	static InputStream is;
	static PrintWriter out;
	static String INPUT = "";

	public static void main(String[] args) throws Exception {
		new Main().run();
	}

	void solver() {
		while (true) {
			int n = ni();// ???????????°
			int m = ni();// ????????°
			int k = ni();// ????????????
			if (n == 0 && m == 0 && k == 0)
				break;
			int[] x = new int[n];
			double[] l = new double[1300];
			double[] f = new double[1300];
			double[] d = new double[1300];
			double[] ud = new double[1300];
			double[] v = new double[m];
			// ???????????????????????¨???????\???´????°´???????????????

			double[] availableTime = new double[1300];

			for (int i = 0; i < n; i++) {
				x[i] = ni() + 100;// ??????i????\???????????????????
				l[x[i]] = ni();// ??????i????°´???????????????????????????????°´???
				f[x[i]] = ni();// ??????i????????????????????????????????§??¨?°´???
				d[x[i]] = ni();// ??????i????????????????????????????????§????°´???
				ud[x[i]] = (ni() == 0 ? -1 : 1);// ??????i????\???´??¨??±??´????°´????????¢??????
				// -1?????´????\???´????????±??´????°´?????????????????¨????????????
				// 1?????´????\???´????????±??´????°´?????????????????¨????????????
				if (ud[x[i]] == 1) {
					availableTime[x[i]] = l[x[i]] / f[x[i]];
				}
			}
			for (int i = 0; i < m; i++) {
				v[i] = ni();// i?????????????????????
			}

			double[] inTime = new double[1300];
			double[] outTime = new double[1300];

			for (int i = 0; i < m; i++) {
				for (int pos = 101 - i; pos <= k + 100 + m - i; pos++) {
					inTime[pos] = Math.max(inTime[pos + 1], outTime[pos - 1] + 1 / v[i]);
					inTime[pos] = Math.max(inTime[pos], availableTime[pos]);
					outTime[pos] = Math.max(
			inTime[pos] + (ud[pos] == -1 ? l[pos] / f[pos] : (ud[pos] == 1 ? l[pos] / d[pos] : 0)),
							outTime[pos + 1]);
					availableTime[pos] = (ud[pos] == -1 ? l[pos] / d[pos] : (ud[pos] == 1 ? l[pos] / f[pos] : 0))
							+ outTime[pos];
				}
			}
			 out.println(inTime[100 + k]);
		}
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