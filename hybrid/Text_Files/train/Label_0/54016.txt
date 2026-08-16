import java.util.*;
import java.io.*;
import java.awt.geom.*;
import java.math.*;

public class Main {

	static final Scanner in = new Scanner(System.in);
	static final PrintWriter out = new PrintWriter(System.out,false);
	static boolean debug = false;

	static void solve() {
		int[] a = new int[7];
		for (int i=0; i<7; i++) {
			a[i] = in.nextInt();
		}
		long ans1 = a[1]*2;
		long ans2 = ans1;

		ans1 += a[0]/2*4;
		ans1 += a[3]/2*4;
		ans1 += a[4]/2*4;

		if (a[0] > 0 && a[3] > 0 && a[4] > 0) {
			a[0]--;
			a[3]--;
			a[4]--;
			ans2 += a[0]/2*4;
			ans2 += a[3]/2*4;
			ans2 += a[4]/2*4;
			ans2 += 6;
		}

		out.println(Math.max(ans1, ans2)/2);
	}

	public static void main(String[] args) {
		debug = args.length > 0;
		long start = System.nanoTime();

		solve();
		out.flush();

		long end = System.nanoTime();
		dump((end - start) / 1000000 + " ms");
		in.close();
		out.close();
	}

	static void dump(Object... o) { if (debug) System.err.println(Arrays.deepToString(o)); }
}