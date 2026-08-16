import java.util.*;
import java.io.*;
import java.lang.*;
import java.math.*;

public class A {
	public void run() throws Exception {
		FastScanner sc = new FastScanner();
		long l = sc.nextLong();
		long r = sc.nextLong();
		long k = sc.nextLong();
		ArrayList<Long> powers = new ArrayList<Long>();
		BigInteger cur = BigInteger.ONE;
		while(cur.compareTo(new BigInteger("1000000000000000000")) <= 0) {
			powers.add(cur.longValue());
			cur = cur.multiply(new BigInteger("" + k));
		}
		//System.out.println(powers);
		int idx = Collections.binarySearch(powers, l);
		if(idx < 0) idx = ~idx;
		int end = Collections.binarySearch(powers, r);
		if(end < 0) {
			end = ~end;
			end--;
		}
		boolean exists = false;
		for(int i = idx; i <= end; i++) {
			exists = true;
			System.out.print(powers.get(i) + " ");
		}
		if(!exists) {
			System.out.println(-1);
		}
	}
	static class FastScanner {
		public BufferedReader reader;
		public StringTokenizer tokenizer;

		public FastScanner() {
			reader = new BufferedReader(new InputStreamReader(System.in), 32768);
			tokenizer = null;
		}

		public String next() {
			while (tokenizer == null || !tokenizer.hasMoreTokens()) {
				try {
					tokenizer = new StringTokenizer(reader.readLine());
				} catch (IOException e) {
					throw new RuntimeException(e);
				}
			}
			return tokenizer.nextToken();
		}

		public int nextInt() {
			return Integer.parseInt(next());
		}

		public long nextLong() {
			return Long.parseLong(next());
		}

		public double nextDouble() {
			return Double.parseDouble(next());
		}

		public String nextLine() {
			try {
				return reader.readLine();
			} catch (IOException e) {
				throw new RuntimeException(e);
			}
		}

	}
	public static void main(String[] args) throws Exception {
		new A().run();
	}
}