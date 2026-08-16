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
		int x = in.nextInt();


		if (n == 1) {
			if (x == 1) {
				out.println("Yes");
				out.println(1);
			} else {
				out.println("No");
			}

			return;
		}

		if (n == 2) {
			if (x == 2) {
				out.println("Yes");
				for (int i=1; i<=3; i++) {
					out.println(i);
				}
			} else {
				out.println("No");
			}

			return;
		}

		if (x == 1 || x == 2*n-1) {
			out.println("No");
		} else {
			out.println("Yes");

			ArrayList<Integer> ans = new ArrayList<>();

			if (x == 2) {
				ans.add(2*n-1);
				ans.add(1);
				ans.add(2);
				ans.add(2*n-2);

				int m = n;
				int p = 3;
				for (int i=0; i<m-3; i++) {
					ans.add(0, p);
					p++;
				}

				while (p != 2*n-2) {
					ans.add(p);
					p++;
				}

			} else if (x == 2*n-2) {
				ans.add(1);
				ans.add(2*n-2);
				ans.add(2*n-1);
				ans.add(2);

				int m = n;
				int p = 3;
				for (int i=0; i<m-2; i++) {
					ans.add(0, p);
					p++;
				}
				while (p != 2*n-1) {
					ans.add(p);
					p++;
				}

			} else {
				ans.add(1);
				ans.add(x);
				ans.add(2*n-1);
				ans.add(2);

				int m = n;
				int p = 3;
				if (p == x) p++;
				for (int i=0; i<m-2; i++) {
					ans.add(0, p);
					p++;
					if (p == x) p++;
				}
				while (p != 2*n-1) {
					ans.add(p);
					p++;
					if (p == x) p++;
				}
			}


			for (int i=0; i<2*n-1; i++) {
				out.println(ans.get(i));
			}
		}
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