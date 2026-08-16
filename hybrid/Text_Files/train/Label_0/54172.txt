import java.io.*;
import java.util.*;
import java.math.*;

public class D implements Runnable {
	static BufferedReader in;
	static PrintWriter out;
	static StringTokenizer st;
	static Random rnd;

	final int maxFactors = (1 << 14), timeLimit = 3505;

	private void solve() throws IOException {
		long start = System.currentTimeMillis();
		int n = nextInt();
		long[] numbers = new long[n];
		for (int i = 0; i < n; i++) {
			numbers[i] = nextLong();
		}
		long result = 1;
		int minCounter = (n + 1) / 2;
		long[] factorsArr = new long[maxFactors];
		int[] factorsCounters = new int[maxFactors];
		HashMap<Long, Integer> fastFactorsCounters = new HashMap<>();
		while (!isOver(start)) {
			int baseIndex = rnd.nextInt(n);
			long base = numbers[baseIndex];
			int factorsCount = 0;
			for (long i = 1; i * i <= base; i++) {
				if (base % i == 0) {
					factorsArr[factorsCount++] = i;
					if (i * i != base) {
						factorsArr[factorsCount++] = base / i;
					}
				}
			}
			Arrays.sort(factorsArr, 0, factorsCount);
			Arrays.fill(factorsCounters, 0, factorsCount, 0);
			fastFactorsCounters.clear();
			for (int i = 0; i < factorsCount; i++) {
				fastFactorsCounters.put(factorsArr[i], i);
			}
			for (int i = 0; i < n; i++) {
				long current = getGCD(base, numbers[i]);
				++factorsCounters[fastFactorsCounters.get(current)];
			}
			for (int i = 0; i < factorsCount; i++) {
				for (int j = 0; j < i; j++) {
					if (factorsArr[i] % factorsArr[j] == 0) {
						factorsCounters[j] += factorsCounters[i];
					}
				}
			}
			for (int i = 0; i < factorsCount; i++) {
				if (factorsCounters[i] >= minCounter) {
					result = Math.max(result, factorsArr[i]);
				}
			}

		}
		out.println(result);
	}

	private boolean isOver(long start) {
		long current = System.currentTimeMillis();
		return (current - start) >= timeLimit;
	}

	private long getGCD(long a, long b) {
		while (b != 0) {
			long t = a;
			a = b;
			b = t % b;
		}
		return a;
	}

	public static void main(String[] args) {
		// final boolean oldChecker = false;
		//
		// if (oldChecker)
		// new Thread(null, new Template(), "yarrr", 1 << 24).start();
		// else
		new D().run();
	}

	public void run() {
		try {
			final String className = this.getClass().getName().toLowerCase();

			try {
				in = new BufferedReader(new FileReader(className + ".in"));
				out = new PrintWriter(new FileWriter(className + ".out"));
				// in = new BufferedReader(new FileReader("input.txt"));
				// out = new PrintWriter(new FileWriter("output.txt"));
			} catch (FileNotFoundException e) {
				in = new BufferedReader(new InputStreamReader(System.in));
				out = new PrintWriter(System.out);
			}

			rnd = new Random();

			solve();

			out.close();
		} catch (IOException e) {
			e.printStackTrace();
			System.exit(1);
		}
	}

	private String nextToken() throws IOException {
		while (st == null || !st.hasMoreTokens()) {
			String line = in.readLine();

			if (line == null)
				return null;

			st = new StringTokenizer(line);
		}

		return st.nextToken();
	}

	private int nextInt() throws IOException {
		return Integer.parseInt(nextToken());
	}

	private long nextLong() throws IOException {
		return Long.parseLong(nextToken());
	}

	private double nextDouble() throws IOException {
		return Double.parseDouble(nextToken());
	}
}