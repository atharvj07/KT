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
		new Main().run();
	}

	BufferedReader in;
	PrintWriter out;
	StringTokenizer st = new StringTokenizer("");

	int[] q, s, pos;

	int n, pnt;
	long res = 0;

	private void run() throws IOException {
		in = new BufferedReader(new InputStreamReader(System.in));
		out = new PrintWriter(System.out);
		n = nextInt();
		q = new int[2 * n];
		int max = 0, cntMax = 0;
		int max2 = 0, cntMax2 = 0;
		for (int i = 0; i < n; i++) {
			q[i] = nextInt();
			if (q[i] > max) {
				max2 = max;
				cntMax2 = cntMax;
				max = q[i];
				cntMax = 1;
			} else if (q[i] == max)
				cntMax++;
			else if (q[i] > max2) {
				max2 = q[i];
				cntMax2 = 1;
			} else if (q[i] == max2)
				cntMax2++;
			q[i + n] = q[i];
		}

		if (cntMax == 1)
			res += cntMax2;
		else
			res += 2 * cntMax2;
		res += 2 * (n - cntMax - cntMax2);

		s = new int[2 * n];
		pos = new int[2 * n];
		pnt = -1;
		for (int i = 0; i < 2 * n; i++) {
			while (pnt != -1 && s[pnt] < q[i]) {
				clearLevel();
			}
			s[++pnt] = q[i];
			pos[pnt] = i;
		}

		while (pnt != -1)
			clearLevel();

		out.println(res);
		in.close();
		out.close();
	}

	private void clearLevel() {
		int level = s[pnt];
		if (pos[pnt] < n) {
			long levelCnt = 0;
			while (pnt != -1 && s[pnt] == level) {
				levelCnt++;
				pnt--;
			}
			res += levelCnt * (levelCnt - 1) / 2;
		} else {
			long leftCnt = 0;
			long rightCnt = 0;
			int maxPos = pos[pnt];
//			System.out.println("maxPos = " + maxPos);
			while (pnt != -1 && s[pnt] == level && pos[pnt] > maxPos - n) {
				if (pos[pnt] >= n)
					rightCnt++;
				else
					leftCnt++;
				pnt--;
			}
//			System.out.println("level = " + level);
//			System.out.println("left = " + leftCnt);
//			System.out.println("right = " + rightCnt);
//			System.out.println("---");

			if (pnt != -1 && s[pnt] == level && pos[pnt] <= maxPos - n) {
				long levelCnt = leftCnt + rightCnt;
				res += levelCnt * (levelCnt - 1) / 2;
			} else if (pos[pnt + 1] < n)
				res += leftCnt * rightCnt + leftCnt * (leftCnt - 1) / 2;

			while (pnt != -1 && s[pnt] == level)
				pnt--;
		}
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
