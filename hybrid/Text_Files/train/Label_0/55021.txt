import java.util.*;
import java.io.*;
import java.awt.geom.*;
import java.math.*;

public class Main {

	static final Scanner in = new Scanner(System.in);
	static final PrintWriter out = new PrintWriter(System.out,false);
	static boolean debug = false;

	static void solve() {
		int n = in.nextInt();
		int[] a = new int[n];
		for (int i=0; i<n; i++) {
			a[i] = in.nextInt();
		}

		int ans = -1;
		for (int i=0; i<n; i++) {
			for (int j=i+1; j<n; j++) {
				String s = String.valueOf(a[i]*a[j]);
				boolean f = true;
				for (int k=0; k<s.length()-1; k++) {
					if (s.charAt(k) + 1 != s.charAt(k+1)) f = false;
				}
				if (f) {
					ans = Math.max(ans, a[i]*a[j]);
				}
			}
		}
		out.println(ans);
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