import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.InputStream;

public class A {

	public static void main(String[] args) {
		InputReader in = new InputReader(System.in);
		PrintWriter out = new PrintWriter(System.out);
		A solver = new A();
		solver.solve(1, in, out);
		out.close();

	}

	public void solve(int testNumber, InputReader in, PrintWriter out) {

		int n = in.nextInt();
		
		int[] arr = new int[n];
		boolean pos = false;
		int sum = 0;
		
		for(int i = 0; i < n; i++) {
			int a = in.nextInt();
			arr[i] = a;
			if(a != 0) pos = true;
			sum += a;
			
		}
		if(!pos) {
			System.out.println("NO");
			
		}
		else {
			System.out.println("YES");
			if(sum != 0) {
				System.out.println(1);
				System.out.println(1 + " " + n);
			}
			else {
				System.out.println(2);
				for(int i = 0; i < n; i++) {
					if(sum + arr[i] != 0) {
						System.out.println(1 + " " + (i + 1));
						System.out.println((i + 2) + " " + (n));
						return;
						
					}
					
				}
			}
			
		}
		
		
	}

	static class InputReader {
		public BufferedReader reader;
		public StringTokenizer tokenizer;

		public InputReader(InputStream stream) {
			reader = new BufferedReader(new InputStreamReader(stream), 32768);
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

	}
}
