import java.io.*;
import java.math.*;
import java.util.*;

public class Main {
	Scanner sc = new Scanner(System.in);

	void debug(String a) {
		// System.out.println(a);
	}

	class unit {
		boolean cacco;
		molecule m;
		int value;

		unit(String buffer) {
			debug("u:" + buffer);
			if (buffer.startsWith("(")) {
				cacco = true;
				m = new molecule(buffer.substring(1, buffer.length() - 1));
			} else {
				if (buffer.length() == 2) {
					value = buffer.charAt(0) - 'A' + 1;
					value *= 32;
					value += buffer.charAt(1) - 'a' + 1;
				} else {
					value = buffer.charAt(0) - 'A';
				}
			}
		}

		int[] valueOf() {
			if (cacco) {
				return m.valueOf();
			} else {
				int[] ret = new int[32 * 32];
				ret[value] = 1;
				return ret;
			}
		}

	}

	String digit = "0123456789";

	// outer ()
	class group {
		unit uni;
		int num;

		group(String buffer) {
			debug("g:" + buffer);
			String n = "";
			for (char ch : buffer.toCharArray()) {
				if ('0' <= ch && ch <= '9') {
					n += ch;
				} else {
					n = "";
				}
			}
			if (n.equals("")) {
				num = 1;
			} else {

				num = Integer.valueOf(n);
			}
			debug("0:" + num);
			uni = new unit(buffer.substring(0, buffer.length() - n.length()));
		}

		int[] valueOf() {
			int[] ret = uni.valueOf();
			if (num != 1) {
				for (int i = 0; i < 32 * 32; i++) {
					ret[i] *= num;
				}
			}
			return ret;
		}

	}

	class molecule {
		LinkedList<group> list = new LinkedList<group>();

		molecule(String buffer) {
			debug("m:" + buffer);
			int depth = 0;

			String b2 = "";
			for (char ch : buffer.toCharArray()) {
				if (depth == 0) {
					if (ch == '(') {
						depth++;
						if (!b2.equals(""))
							list.add(new group(b2));
						b2 = "";
					}
					if (Character.isUpperCase(ch)) {
						if (!b2.equals(""))
							list.add(new group(b2));
						b2 = "";
					}

				} else {
					if (ch == ')') {
						depth--;
					}
					if (ch == '(') {
						depth++;
					}
				}
				b2 += ch;

			}

			if (!b2.equals("")) {
				list.add(new group(b2));
			}
		}

		int[] valueOf() {
			int[] ret = new int[32 * 32];
			for (group g : list) {
				int[] gv = g.valueOf();
				for (int i = 0; i < 32 * 32; i++) {
					ret[i] += gv[i];
				}
			}
			return ret;
		}

	}

	class sequence {
		LinkedList<molecule> list = new LinkedList<molecule>();

		sequence(String buffer) {
			debug("s:" + buffer);
			for (; buffer.indexOf('+') != -1;) {
				int index = buffer.indexOf('+');
				String a = buffer.substring(0, index);
				list.add(new molecule(a));
				buffer = buffer.substring(index + 1);
			}
			if (!buffer.isEmpty()) {
				list.add(new molecule(buffer));
			}
		}

	}

	class equation {
		sequence left;
		sequence right;

		equation(String buffer) {
			debug("e:" + buffer);
			int index = buffer.indexOf("->");

			left = new sequence(buffer.substring(0, index));
			right = new sequence(buffer.substring(index + 2,
					buffer.length() - 1));
		}

	}

	void run() {
		for (;;) {
			String buffer = sc.nextLine();
			if (buffer.equals(".")) {
				break;
			}

			equation eq = new equation(buffer);

			int[][] l = new int[eq.left.list.size()][];
			int[][] r = new int[eq.right.list.size()][];
			int n = l.length;
			int m = r.length;

			TreeSet<Integer> used = new TreeSet<Integer>();

			for (int i = 0; i < n; i++) {
				l[i] = eq.left.list.get(i).valueOf();
				for (int j = 0; j < 32 * 32; j++) {
					if (0 != l[i][j]) {
						if (!used.contains(j)) {
							used.add(j);
						}
					}
				}
				// System.out.println(Arrays.toString(l[i]));
			}

			for (int i = 0; i < m; i++) {
				r[i] = eq.right.list.get(i).valueOf();
				// System.out.println(Arrays.toString(r[i]));
				for (int j = 0; j < 32 * 32; j++) {
					if (0 != r[i][j]) {
						if (!used.contains(j)) {
							used.add(j);
						}
					}
				}
			}

			long z[][] = new long[n + m][used.size()];
			int N = n + m;
			long ans[][] = new long[N][N];

			for (int i = 0; i < N; i++) {
				ans[i][i] = 1;
			}

			int map[] = new int[32 * 32];
			int M = 0;
			for (int i = 0; i < 32 * 32; i++) {
				if (used.contains(i)) {
					map[i] = M;
					M++;
				}
			}

			for (int i = 0; i < n; i++) {
				for (int j = 0; j < 32 * 32; j++) {
					if (0 != l[i][j]) {
						z[i][map[j]] = l[i][j];
					}
				}
				// System.out.println(Arrays.toString(z[i]));
			}

			for (int i = 0; i < m; i++) {
				for (int j = 0; j < 32 * 32; j++) {
					if (0 != r[i][j]) {
						z[n + i][map[j]] = -r[i][j];
					}
				}
				// System.out.println(Arrays.toString(z[n + i]));
			}

			int i2 = 0;
			for (int i = 0; i < N && i2 < M; i++, i2++) {
				if (z[i][i2] == 0) {
					int swap = -1;
					for (int j = i + 1; j < N; j++) {
						if (z[j][i2] != 0) {
							swap = j;
							break;
						}
					}
					if (swap == -1) {
						i--;
						continue;
					}
					for (int j = 0; j < M; j++) {
						long temp = z[swap][j];
						z[swap][j] = z[i][j];
						z[i][j] = temp;
					}
					for (int j = 0; j < N; j++) {
						long temp = ans[swap][j];
						ans[swap][j] = ans[i][j];
						ans[i][j] = temp;
					}
					// System.out.println("swap"+i+" "+swap);
				}

				for (int j = i + 1; j < N; j++) {
					if (z[j][i2] != 0) {
						long fa = z[i][i2];
						long fb = z[j][i2];

						long gcd = gcd(Math.abs(fa), Math.abs(fb));
						long fa2 = fa / gcd;
						long fb2 = fb / gcd;

						// System.out.println(j+" "+Arrays.toString(z[j]));
						acc(z[j], z[i], fa2, -fb2);
						// System.out.println(j+" "+Arrays.toString(z[j])
						// + Arrays.toString(ans[j]));
						acc(ans[j], ans[i], fa2, -fb2);
					}
				}

			}
			long gcdl = Math.abs(ans[N - 1][0]);
			for (int i = 1; i < N; i++) {
				gcdl = gcd(gcdl, Math.abs(ans[N - 1][i]));
			}

			for (int i = 0; i < N; i++) {
				if (i != 0) {
					System.out.print(" ");
				}
				System.out.print(Math.abs(ans[N - 1][i] / gcdl));
			}
			System.out.println();
		}
	}

	long gcd(long a, long b) {
		if (a == 0) {
			return b;
		}
		if (b == 0) {
			return a;
		}
		if (a < b) {
			long temp = a;
			a = b;
			b = temp;
		}
		if (a % b == 0) {
			return b;
		}
		return gcd(b, a % b);
	}

	void acc(long[] a, long[] b, long c, long d) {
		for (int i = 0; i < a.length; i++) {
			a[i] = a[i] * c + b[i] * d;
		}
	}

	public static void main(String[] a) {
		Main m = new Main();
		m.run();
	}
}