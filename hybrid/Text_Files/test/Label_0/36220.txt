import java.io.*;
import java.util.*;

public class Main {

	void go(int R, int C, int r, int c) {
		int cx = 0;
		int cy = R * C;
		for (int i = r - 1; i < R; i += r) {
			for (int j = c - 1; j < C; j += c) {
				cx++;
				cy--;
			}
		}
		
		// x > (rc - 1) y
		// cx * x < cy * y
		
		if ((r * c - 1) * cx >= cy) {
			throw new AssertionError();
		}
		
		int x = 2 * cx * (r * c - 1) + 1;
		int y = 2 * cx;
		
		out.println("Yes");
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				if (i % r == r - 1 && j % c == c - 1) {
					out.print((-x) + " ");
				} else {
					out.print(y + " ");
				}
			}
			out.println();
		}
	}
	
	void submit() {
		int R = nextInt();
		int C = nextInt();
		int r = nextInt();
		int c = nextInt();
		if (R % r == 0 && C % c == 0) {
			out.println("No");
			return;
		}
		
		go(R, C, r, c);
	}

	void preCalc() {

	}

	void stress() {
		for (int tst = 0;; tst++) {
			int R = rand(1, 500);
			int C = rand(1, 500);
			int r = rand(1, R);
			int c = rand(1, C);
			if (R % r == 0 && C % c == 0) {
				continue;
			}
			go(R, C, r, c);
			System.err.println(tst);
		}
	}

	void test() {
		int R = 500;
		int C = 500;
		int r = 500;
		int c = 499;
		go(R, C, r, c);
	}

	Main() throws IOException {
		br = new BufferedReader(new InputStreamReader(System.in));
		out = new PrintWriter(System.out);
		preCalc();
		submit();
//		stress();
//		test();
		out.close();
	}

	static final Random rng = new Random();

	static int rand(int l, int r) {
		return l + rng.nextInt(r - l + 1);
	}

	public static void main(String[] args) throws IOException {
		new Main();
	}

	BufferedReader br;
	PrintWriter out;
	StringTokenizer st;

	String nextToken() {
		while (st == null || !st.hasMoreTokens()) {
			try {
				st = new StringTokenizer(br.readLine());
			} catch (IOException e) {
				throw new RuntimeException(e);
			}
		}
		return st.nextToken();
	}

	String nextString() {
		try {
			return br.readLine();
		} catch (IOException e) {
			throw new RuntimeException(e);
		}
	}

	int nextInt() {
		return Integer.parseInt(nextToken());
	}

	long nextLong() {
		return Long.parseLong(nextToken());
	}

	double nextDouble() {
		return Double.parseDouble(nextToken());
	}
}
