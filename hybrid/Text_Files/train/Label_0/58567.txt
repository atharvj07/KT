import static java.lang.Math.*;
import static java.util.Arrays.*;
import java.util.*;
import java.io.*;

public class Main {
	public static void main(String[] args) {
		try {
			System.setIn(new FileInputStream("src/aoj2104/input.txt"));
			// System.setOut(new PrintStream(new FileOutputStream("src/aoj2103/result.txt")));
		} catch (FileNotFoundException e) {
		}
		new Main().run();
	}



	Scanner sc;
	void run() {
		sc = new Scanner(System.in);
		int T = sc.nextInt();
		while (T-- >0) {
			long ans = solve();
			System.out.println(ans);
		}
	}


	long solve() {
		int n = sc.nextInt();
		int k = sc.nextInt();
		int[] x = new int[n];
		for (int i = 0; i < n; i++)
			x[i] = sc.nextInt();

		if (n == 1) {
			return 0;
		}

		int[] d = new int[n-1];
		for (int i = 1; i < n; i++) d[i-1] = x[i] - x[i-1];
		Arrays.sort(d);

		long res = 0;
		for (int i = 0; i + k - 1 < d.length; i++) {
			res += d[i];
		}
		return res;
	}

	void tr(Object... os) {
		System.err.println(deepToString(os));
	}
}