
import java.io.*;

import java.util.*;
import java.math.*;

import static java.lang.Math.*;
import static java.util.Arrays.*;
import static java.util.Collections.*;
import static java.math.BigInteger.*;
import static java.lang.Character.*;

class AOJ1020 {
	int[] di = { +1, -1, +3, -3 };

	public void run() {
		Scanner sc = new Scanner(System.in);
		while (true) {
			int n = sc.nextInt();
			if (n == 0)
				return;
			int s = sc.next().charAt(0) - 'A';
			int t = sc.next().charAt(0) - 'A';
			int b = sc.next().charAt(0) - 'A';

			double[] prob = new double[9];
			double[][] move = new double[9][9];
			for (int i = 0; i < 9; i++)
				for (int d = 0; d < 4; d++) {
					int j = (!isValidMove(i, d) || i + di[d] == b) ? i : i + di[d];
					move[j][i] += .25;
				}

			prob[s] = 1.;
			for (int k = 0; k < n; k++) {
				double[] np = new double[9];
				for (int i = 0; i < 9; i++)
					for (int j = 0; j < 9; j++)
						np[i] += move[i][j] * prob[j];
				prob = np;
			}
			System.out.println(prob[t]);
		}
	}

	boolean isValidMove(int i, int d) {
		switch (d) {
		case 0:
			return i % 3 < 2;
		case 1:
			return i % 3 > 0;
		case 2:
			return i < 6;
		case 3:
			return i > 2;
		}
		return false;
	}
}

public class Main {
	public static void main(String... args) {
		new AOJ1020().run();
	}

	public static void debug(Object... os) {
		System.err.println(java.util.Arrays.deepToString(os));
	}
}

class Scanner {
	final java.util.Scanner sc;

	public double nextDouble() {
		return Double.parseDouble(sc.next());
	}

	public Scanner(java.io.InputStream is) {
		this.sc = new java.util.Scanner(is);
	}

	public boolean hasNext() {
		return sc.hasNext();
	}

	public String next() {
		return sc.next();
	}

	public int nextInt() {
		return Integer.parseInt(sc.next());
	}

	public String nextLine() {
		return sc.nextLine();
	}

	public long nextLong() {
		return Long.parseLong(sc.next());
	}
}