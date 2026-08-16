
import java.util.*;
import java.io.*;
import static java.util.Arrays.*;
import static java.util.Collections.*;
import static java.lang.Math.*;

public class Main {

	int INF = 1 << 28;
	//long INF = 1L << 62;
	double EPS = 1e-10;
	int d, x, y, n;
	boolean[] a, b;
	int[] p, q;

	void run() {
		Scanner sc = new Scanner(System.in);
		d = sc.nextInt();
		x = sc.nextInt();

		a = new boolean[x];
		p = new int[x];

		for (int i=0;i<x;i++) {
			a[i] = sc.next().equalsIgnoreCase("D");
			p[i] = sc.nextInt();
		}

		y = sc.nextInt();

		b = new boolean[y];
		q = new int[y];

		for (int i=0;i<y;i++) {
			b[i] = sc.next().equalsIgnoreCase("DD");
			q[i] = sc.nextInt();
		}

		n = x + 2 * y;
		mem = new int[1<<n];
//		debug(n, x, y, a, b, p, q);
		fill(mem, -1);

		System.out.println(solve(0));
	}

	int[] mem;
	int solve(int S) {
		if (mem[S] >= 0) return mem[S];
		if (Integer.bitCount(S) == d) return 0;
		int max = 0;

		for (int i=0;i<n;i++) if (((S>>i)&1) == 0) {
			if (i < x) {
				if (! a[i]) continue;
				max = max(max, solve(S|(1<<i)) + p[i]);
			}
			else {
//				debug(i, Integer.bitCount(S));
				if (i % 2 != x % 2) continue;
				if (Integer.bitCount(S) >= d - 1) continue;
				int j = i - x; j /= 2;
				if (! b[j]) continue;
				max = max(max, solve(S|(3<<i)) + q[j]);
			}
		}

		return mem[S] = max;
	}

	void debug(Object... os) {
		System.err.println(Arrays.deepToString(os));
	}

	public static void main(String[] args) {
		new Main().run();
	}
}